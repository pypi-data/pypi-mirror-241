import logging
from typing import Iterable
from typing import Any, Optional

import aiogram
from aiogram import Bot, Dispatcher
from aiogram.methods import Response, SendMessage, TelegramMethod
from aiogram.types import Message, TelegramObject
from prometheus_client import Counter, Histogram
from prometheus_client.metrics_core import GaugeMetricFamily, InfoMetricFamily, Metric
from prometheus_client.registry import Collector

logger = logging.getLogger('app')


class DispatcherAiogramCollector(Collector):
    dp: Dispatcher

    def __init__(self, dp: Dispatcher, prefix: str = 'aiogram_') -> None:
        self.dp = dp
        self.prefix = prefix

        self.aiogram_info_metric = InfoMetricFamily(
            'aiogram',
            'Info about aiogram',
            value={
                'version': aiogram.__version__,
                'api_version': aiogram.__api_version__,
            },
        )

        self.dispatcher_info_metric = InfoMetricFamily(
            f'{self.prefix}_dispatcher',
            'Info about aiogram dispatcher',
            value={
                # 'version': self.dp.errors,
                # 'api_version': aiogram.__api_version__,
            },
        )

    def collect(self) -> Iterable[Metric]:
        yield self.aiogram_info_metric

        c = GaugeMetricFamily(
            f'{self.prefix}_observers',
            'Aiogram`s Dispatcher`s observers',
            labels=['name'],
        )

        c.add_metric(['shutdown'], len(self.dp.shutdown.handlers))
        c.add_metric(['startup'], len(self.dp.startup.handlers))

        for observer_name, observer in self.dp.observers.items():
            c.add_metric([observer_name], len(observer.handlers))

        yield c

        yield InfoMetricFamily(
            f'{self.prefix}_fsm',
            'Info about aiogram`s dispatcher`s fsm',
            {
                'storage': self.dp.fsm.storage.__class__.__name__,
                'strategy': self.dp.fsm.strategy.__class__.__name__,
                'events_isolation': str(self.dp.fsm.events_isolation),
            },
        )


class BotAiogramCollector(Collector):
    bot: Bot

    def __init__(self, bot: Bot, prefix: str = 'aiogram_') -> None:
        self.bot = bot
        self.prefix = prefix

    def collect(self) -> Iterable[Metric]:
        bot_user = self.bot._me

        if bot_user is None:
            return

        yield InfoMetricFamily(
            f'{self.prefix}_bot',
            'Info about bot',
            {
                'id': str(self.bot.id),
                'username': str(bot_user.username),
                'is_bot': str(bot_user.is_bot),
                'first_name': str(bot_user.first_name),
                'last_name': str(bot_user.last_name),
                'language_code': str(bot_user.language_code),
                'is_premium': str(bot_user.is_premium),
                'added_to_attachment_menu': str(bot_user.added_to_attachment_menu),
                'can_join_groups': str(bot_user.can_join_groups),
                'can_read_all_group_messages': str(bot_user.can_read_all_group_messages),
                'supports_inline_queries': str(bot_user.supports_inline_queries),
                'parse_mode': str(self.bot.parse_mode),
                'disable_web_page_preview': str(self.bot.disable_web_page_preview),
                'protect_content': str(self.bot.protect_content),
            },
        )


class SendedMessagesAiogramCollector(Collector):
    prefix: str
    messages_counter: Counter

    LABELS = ['bot_username', 'chat_id']

    def __init__(self, prefix: str = 'aiogram_') -> None:
        self.prefix = prefix

        self.messages_counter = Counter(
            f'{self.prefix}_sended_messages',
            'Aiogram`s sended messages',
            self.LABELS,
            registry=None,
        )

    def add_messages(self, bot: Bot, message: SendMessage):
        labels = [
            bot._me.username,
            message.chat_id,
        ]

        self.messages_counter.labels(*labels).inc()

    def collect(self) -> Iterable[Metric]:
        yield from self.messages_counter.collect()


class ReceivedMessagesAiogramCollector(Collector):
    prefix: str
    messages_counter: Counter

    LABELS = ['bot_username', 'chat_id', 'sender_id', 'is_audio', 'is_file', 'is_reply']

    def __init__(self, prefix: str = 'aiogram_') -> None:
        self.prefix = prefix

        self.messages_counter = Counter(
            f'{self.prefix}_received_messages',
            'Aiogram`s received messages',
            self.LABELS,
            registry=None,
        )

    def add_messages(self, bot: Bot, message: Message):
        labels = [
            bot._me.username,
            message.chat.id,
            message.from_user.id,
            'is_audio' if message.audio is not None else 'none',
            'is_file' if message.media_group_id is not None else 'none',
            'is_reply' if message.reply_to_message is not None else 'none',
        ]

        self.messages_counter.labels(*labels).inc()

    def collect(self) -> Iterable[Metric]:
        yield from self.messages_counter.collect()


class MessageMiddlewareAiogramCollector(Collector):
    prefix: str
    events_histogram: Histogram
    LABELS = ['event_type', 'bot_username', 'chat_id', 'sender_id', 'status']

    def __init__(self, prefix: str = 'aiogram_') -> None:
        self.prefix = prefix

        self.received_messages_collector = ReceivedMessagesAiogramCollector()

        self.events_histogram = Histogram(
            f'{self.prefix}_events',
            'Aiogram`s events',
            self.LABELS,
            registry=None,
        )

    def add_event(self, event: TelegramObject, success: bool, executing_time: float):
        labels = [
            event.__class__.__name__,
            event.bot._me.username,
            None,
            None,
            'success' if success else 'error',
        ]

        if isinstance(event, Message):
            labels = [
                event.__class__.__name__,
                event.bot._me.username,
                event.chat.id,
                event.from_user.id,
                'success' if success else 'error',
            ]

        self.events_histogram.labels(*labels).observe(executing_time)

        if isinstance(event, Message):
            self.received_messages_collector.add_messages(event.bot, event)

    def collect(self) -> Iterable[Metric]:
        yield from self.events_histogram.collect()
        yield from self.received_messages_collector.collect()


class SessionMiddlewareAiogramCollector(Collector):
    prefix: str
    requests_histogram: Histogram
    LABELS = ['method_type', 'bot_username', 'error']

    def __init__(self, prefix: str = 'aiogram_') -> None:
        self.prefix = prefix

        self.sended_messages_collector = SendedMessagesAiogramCollector()

        self.requests_histogram = Histogram(
            f'{self.prefix}_requests',
            'Aiogram`s requests',
            self.LABELS,
            registry=None,
        )

    def add_request(
        self,
        bot: Bot,
        method: Optional[TelegramMethod[Any]],
        response: Optional[Response[Any]],
        executing_time: float,
        error: Optional[BaseException] = None,
    ):
        if bot._me is None:
            return

        labels = [
            method.__class__.__name__,
            bot._me.username,
            error.__class__.__name__,
        ]

        self.requests_histogram.labels(*labels).observe(executing_time)

        if isinstance(method, SendMessage):
            self.sended_messages_collector.add_messages(bot, method)

    def collect(self) -> Iterable[Metric]:
        yield from self.requests_histogram.collect()
        yield from self.sended_messages_collector.collect()
