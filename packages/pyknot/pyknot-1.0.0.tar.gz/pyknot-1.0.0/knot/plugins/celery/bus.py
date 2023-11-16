from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from knot.bus import MessageBus as _MessageBus

from .queue import dispatch_queue_task

if TYPE_CHECKING:
    from knot.types import (
        Message,
        MessageType,
    )


@dataclass(slots=True)
class MessageBus(_MessageBus):
    def dispatch_queue(self, message: Message[MessageType]) -> MessageType:
        message_dto = message.as_dict()
        message_type = type(message)
        queue_payload = (
            f"{message_type.__module__}.{message_type.__name__}",
            message_dto,
        )
        return dispatch_queue_task.apply_async(queue_payload)
