from abc import ABC
from dataclasses import (
    asdict,
    dataclass,
)
from typing import (
    Generic,
    TypeVar,
)

MessageType = TypeVar("MessageType")


class Message(Generic[MessageType], ABC):
    """The Message object defines the interface of a message (command or query)."""

    def as_dict(self):
        return asdict(self)


@dataclass
class Query(Message[MessageType], ABC):
    """
    The Query object defines the interface of a query.
    """


@dataclass
class Command(Message[MessageType], ABC):
    """The Command object defines the interface of a command."""
