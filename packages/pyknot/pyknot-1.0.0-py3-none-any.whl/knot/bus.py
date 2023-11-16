from __future__ import annotations

from abc import ABCMeta
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types import (
        Message,
        MessageHandler,
        MessageType,
    )


@dataclass(slots=True)
class MessageBus:
    messages: dict[Message, MessageHandler]

    def dispatch(self, message: Message[MessageType]) -> MessageType:
        message_type = type(message)
        handler = self.messages.get(message_type)
        if not handler:
            raise ValueError(f"Handler for message {message_type} is not registered")

        instantiated_handler = handler() if isinstance(handler, ABCMeta) else handler
        return instantiated_handler.handle(message)
