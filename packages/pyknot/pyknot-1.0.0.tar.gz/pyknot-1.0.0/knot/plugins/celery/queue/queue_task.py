from celery import shared_task
from dependency_injector.wiring import (
    Provide,
    inject,
)

from knot.bus import MessageBus
from knot.types import Message

from .module_path import import_module_by_path


@shared_task(bind=True)
@inject
def dispatch_queue_task(
    self,
    message_class: str,
    message_dto: dict,
    message_bus: MessageBus = Provide["message_bus"],
) -> None:
    message_cls = import_module_by_path(message_class)
    if not issubclass(message_cls, Message):
        raise ValueError(f"Deserializable {message_cls} data")

    message = message_cls(**message_dto)
    return message_bus.dispatch(message=message)


queue_dispatcher_module = __name__
