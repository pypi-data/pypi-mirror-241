from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    get_args,
    get_origin,
)

from .types import MessageHandler

if TYPE_CHECKING:
    from collections.abc import Iterable

    from .types import (
        Handler,
        Message,
    )


def register_handlers(
    handlers: Iterable[type[Handler]],
) -> dict[Message, MessageHandler]:
    """The register_handlers function registers the handlers for the message types.

    Args:
        handlers (Iterable[type[Handler]]): the handlers to register.
    Returns:
        a dict
    """

    factory = {}
    for handler in handlers:
        for origin_base in handler.__orig_bases__:
            origin = get_origin(origin_base)
            is_valid_type = origin and issubclass(origin, MessageHandler)
            if not is_valid_type:
                raise ValueError(
                    f"Handler {handler} does not specify a valid message type"
                )
            message_type = get_args(origin_base)[0]
            factory[message_type] = handler

    return factory
