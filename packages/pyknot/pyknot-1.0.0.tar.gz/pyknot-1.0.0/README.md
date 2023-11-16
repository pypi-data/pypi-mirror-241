# py-knot

This repository offers a message bus system tailored for integration with [python-dependency-injector
](https://github.com/ets-labs/python-dependency-injector/tree/master). It efficiently manages command and query dispatching and supports dependency injection, enhancing application decoupling, organization, and maintainability.

## **Installation**

The source code is currently hosted on GitHub at: https://github.com/Retr0327/py-knot

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/pyknot/).

- pip

  ```bash
  pip install pyknot
  ```

- poetry
  ```bash
  poetry add pyknot
  ```

## **Usage**

### 1. Fundamental Implementation

1. Define messages:

   Create specific command or query messages by extending `Command` or `Query` classes.

   ```python
   from dataclasses import dataclass
   from knot import Command

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int
   ```

2. Define handlers:

   Implement `CommandHandler` or `QueryHandler` for handling defined messages.

   ```python
   from dataclasses import dataclass
   from knot import Command, CommandHandler

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
       def handle(self, message: TestCommand) -> ReturnType:
           ... # do something
   ```

3. Register handlers:

   Register handlers to `MessageBus` by using `register_handler` method.

   ```python
   from dataclasses import dataclass
   from knot import (
        Command,
        CommandHandler,
        MessageBus,
        register_handlers,
    )

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
       def handle(self, message: TestCommand) -> ReturnType:
           ... # do something


   messages = register_handlers((TestCommandHandler,))
   message_bus = MessageBus(messages=messages)
   ```

4. Dispatch Messages:

   Utilize `MessageBus` to dispatch messages within your application

   ```python
   from dataclasses import dataclass
   from knot import (
        Command,
        CommandHandler,
        MessageBus,
        register_handlers,
    )

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
      a: int
      b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
      def handle(self, message: TestCommand) -> ReturnType:
          ... # do something


   messages = register_handlers((TestCommandHandler,))
   message_bus = MessageBus(messages=messages)
   message_bus.dispatch(TestCommand(a=1, b=2))
   ```

### 2. Integration with Dependency Injection

> please make sure you have installed [python-dependency-injector
> ](https://github.com/ets-labs/python-dependency-injector/tree/master)

1. Set Up Dependency Injection Container

   ```python
   from dataclasses import dataclass
   from dependency_injector import (
       containers,
       providers,
       )

   from knot import (
       Command,
       CommandHandler,
       MessageBus,
       register_handlers,
   )
   from knot.plugins.di import handlers_to_factories

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
       def handle(self, message: TestCommand) -> ReturnType:
           return message.as_dict()


   messages = register_handlers((TestCommandHandler,))


   class MessageBusContainer(containers.DeclarativeContainer):
       message_bus = providers.Singleton(
           MessageBus,
           messages=providers.Dict(handlers_to_factories(messages)),
       )
   ```

   In this container, you'll manage your dependencies, including the message bus. The key function here is `handlers_to_factories`, transforming the handlers into factory providers that are compatible with the dependency injection framework.

2. Wire Dependencies and Dispatch Command

   Wire the dependencies and dispatch commands through the message bus, and inject the message bus to whereever you need it.

   ```python

   from dependency_injector.wiring import inject, Provide

   @inject
   def test(
       message_bus: MessageBus = Provide["message_bus"],
   ):
       return message_bus.dispatch(TestCommand(a=1, b=2))

   if __name__ == "__main__":
       container = MessageBusContainer()
       container.wire(modules=[__name__])
       test()
   ```

### 3. Extension as a Celery Plugin

> please ensure that your application is already configured to work with [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)

`py-knot` can be extended to work seamlessly with [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html), enabling the dispatching of messages to a task queue. This extension is particularly useful for applications that require asynchronous processing or distributed task execution.

1. Extend `MessageBus` for Celery Integration

   Change:

   ```python
   from knot import MessageBus
   ```

   to

   ```python
   from knot.plugins.celery import MessageBus
   ```

2. Wire `queue_dispatcher_module` to the DI Container

   Wiring `queue_dispatcher_module` to the DI container makes the `dispatch_queue` method accessible as a dependency.

   ```python
   from dataclasses import dataclass

   from dependency_injector import (
       containers,
       providers,
   )
   from dependency_injector.wiring import (
       Provide,
       inject,
   )

   from knot import (
       Command,
       CommandHandler,
       register_handlers,
   )
   from knot.plugins.celery import (
       MessageBus,
       queue_dispatcher_module,
   )
   from knot.plugins.di import handlers_to_factories

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
       def handle(self, message: TestCommand) -> ReturnType:
           return message.as_dict()


   messages = register_handlers((TestCommandHandler,))


   class MessageBusContainer(containers.DeclarativeContainer):
       message_bus = providers.Singleton(
           MessageBus,
           messages=providers.Dict(handlers_to_factories(messages)),
       )


   @inject
   def test(
       message_bus: MessageBus = Provide["message_bus"],
   ):
       return message_bus.dispatch_queue(TestCommand(a="a", b="b"))


   if __name__ == "__main__":
       container = MessageBusContainer()
       container.wire(modules=[__name__, queue_dispatcher_module])
       test()

   ```

## Contact Me

If you have any suggestion or question, please do not hesitate to email me at retr0327.dev@gmail.com.
