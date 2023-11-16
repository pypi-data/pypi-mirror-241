import asyncio
import logging
import time
from typing import Awaitable, Callable, Coroutine, Dict
from typing import Any

from aiogram import BaseMiddleware
from aiogram.client.bot import Bot
from aiogram.client.session.middlewares.base import BaseRequestMiddleware, NextRequestMiddlewareType
from aiogram.methods import Response, TelegramMethod
from aiogram.methods.base import TelegramType
from aiogram.types import Message, TelegramObject

from aiogram_prometheus.collectors import MessageMiddlewareAiogramCollector, SessionMiddlewareAiogramCollector

logger = logging.getLogger('aiogram_prometheus')


class ReceivedEventsLoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        start_time = time.time()

        try:
            res = await handler(event, data)

        except asyncio.CancelledError as ex:
            raise ex

        except BaseException as ex:
            elapsed_time = time.time() - start_time
            logger.warning(
                'error event dump',
                extra={
                    'event_type': event.__class__.__name__,
                    'event_bot_id': event.bot.id,
                    'event_bot_username': getattr(event.bot._me, 'username', 'None'),
                    'event_elapsed_time': elapsed_time,
                    'exception': ex,
                },
            )

            raise ex

        elapsed_time = time.time() - start_time
        logger.debug(
            'event dump',
            extra={
                'event_type': event.__class__.__name__,
                'event_bot_id': event.bot.id,
                'event_bot_username': getattr(event.bot._me, 'username', 'None'),
                'event_elapsed_time': elapsed_time,
            },
        )

        return res


class MetricMessageMiddleware(BaseMiddleware):
    collector: MessageMiddlewareAiogramCollector

    def __init__(self, collector: MessageMiddlewareAiogramCollector) -> None:
        self.collector = collector

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        start_time = time.time()

        try:
            res = await handler(event, data)

        except BaseException as ex:
            delta_time = time.time() - start_time
            self.collector.add_event(event, False, delta_time)
            raise ex

        delta_time = time.time() - start_time
        self.collector.add_event(event, True, delta_time)
        return res


class MetricRequestMiddleware(BaseRequestMiddleware):
    def __init__(self, collector: SessionMiddlewareAiogramCollector) -> None:
        self.collector = collector

    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[TelegramType],
        bot: Bot,
        method: TelegramMethod[TelegramType],
    ) -> Coroutine[Any, Any, Response[TelegramType]]:
        start_time = time.time()

        try:
            response = await make_request(bot, method)

        except asyncio.CancelledError as ex:
            raise ex

        except BaseException as ex:
            delta_time = time.time() - start_time
            self.collector.add_request(bot, method, None, delta_time, ex)
            raise ex

        delta_time = time.time() - start_time
        self.collector.add_request(bot, method, response, delta_time)
        return response
