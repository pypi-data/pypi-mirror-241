from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Generic,
    TypeVar,
)

from .message import (
    Command,
    Message,
    MessageType,
    Query,
)

HandlerMessage = TypeVar("Message", bound=Message[MessageType])  # type: ignore


class MessageHandler(Generic[HandlerMessage], ABC):
    @abstractmethod
    def handle(self, message: HandlerMessage) -> MessageType:  # noqa: F841
        pass


QueryType = TypeVar("QueryType", bound=Query[MessageType])  # type: ignore


class QueryHandler(MessageHandler[QueryType], ABC):
    """
    The QueryHandler object defines the query handler based on `MessageHandler`.
    """


CommandType = TypeVar("CommandType", bound=Command[MessageType])  # type: ignore


class CommandHandler(MessageHandler[CommandType], ABC):
    """
    The CommandHandler object defines the command handler based on `MessageHandler`.
    """


Handler = TypeVar("Handler", bound=MessageHandler[HandlerMessage])  # type: ignore
