from __future__ import annotations

from typing import TYPE_CHECKING

from dependency_injector import providers

from knot.types import MessageHandler

if TYPE_CHECKING:
    from dependency_injector.providers import Factory

    from knot.types import Message


def handlers_to_factories(
    messages: dict[Message, MessageHandler]
) -> dict[Message, Factory[MessageHandler]]:
    """The handlers_to_factories function converts dict values to factory providers.

    Args:
        messages (dict[Message, MessageHandler]): the messages to convert.
    Returns:
        a dict
    """

    for key, value in messages.items():
        messages[key] = providers.Factory(value)
    return messages
