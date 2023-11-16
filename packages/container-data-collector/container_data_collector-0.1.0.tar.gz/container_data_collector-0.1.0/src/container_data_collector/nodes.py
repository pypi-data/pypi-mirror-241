"""Nodes of the Query `Tree`."""

from collections.abc import Callable, Container, Hashable
from dataclasses import KW_ONLY, dataclass, field
from enum import IntEnum, auto, unique
from typing import Any, Generic, Protocol

from container_data_collector.common_typevars import Inner, Outer
from container_data_collector.context import Context


@unique
class State(IntEnum):
    """State at which node processing is completed."""
    SUCCESS = auto()
    REJECT = auto()


@dataclass(slots=True)
class Result(Generic[Outer, Inner]):
    """Result of node processing."""
    state: State


class Node(Protocol):
    """Atomic unit of the Query `Tree`. Each node takes an object processed by
    previous node and the current context to know how process this object.
    The `Result` of the processing has some `State`, that can trigger some events
    in the previous node.
    """
    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        ...

    def connect_with(self, *args: "Node") -> None:
        ...


@dataclass(slots=True, eq=False, match_args=False)
class PseudoRoot:
    """Pseudo root `Node` of the Query `Tree`."""
    next_nodes: list[Node] = field(default_factory=list, init=False)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        for node in self.next_nodes:
            result = node.process(obj, context)
            match result.state:
                case State.SUCCESS:
                    continue
                case State.REJECT:
                    return result
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        self.next_nodes.extend(args)


@dataclass(slots=True, eq=False, match_args=False)
class Element:
    """`Node` that represents one of the elements collecting during tree traversal.
    Position tells the inserter function what position the element has in it.
    Next node may point to additional filters, e.g., can this element be used or not.
    """
    pos: int
    _: KW_ONLY
    next_node: Node | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        if self.pos < 1:
            msg = "The position of the element must be greater than zero."
            hint = f"Instead, pos={self.pos} is given."
            raise ValueError(msg + "\n" + hint)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        if self.next_node:
            result = self.next_node.process(obj, context)
            match result.state:
                case State.SUCCESS:
                    pass
                case State.REJECT:
                    return result

        context.apply_element(obj, pos=self.pos)
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        if len(args) != 1:
            raise ValueError("The Element node can have only one node.")
        self.next_node = args[0]


@dataclass(slots=True, eq=False, match_args=False)
class Group:
    """`Node` that represents one of the keys by which the elements will be grouped.
    Level tells what level of grouping this key is related. Factory tells how
    to make the key hashable if it is not. Next node may point to additional
    filters, e.g., can this key be used or not.
    """
    level: int
    _: KW_ONLY
    factory: Callable[[Any], Hashable] | None = field(default=None)
    next_node: Node | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        if self.level < 1:
            msg = "The level of the group must be greater than zero."
            hint = f"Instead, level={self.level} is given."
            raise ValueError(msg + "\n" + hint)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        if self.factory is not None:
            obj = self.factory(obj)
        if self.next_node:
            result = self.next_node.process(obj, context)
            match result.state:
                case State.SUCCESS:
                    pass
                case State.REJECT:
                    return result

        context.create_group(obj, pos=self.level)
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        if len(args) != 1:
            raise ValueError("The Group node can have only one node.")
        self.next_node = args[0]


@dataclass(slots=True, eq=False, match_args=False, kw_only=True)
class Include:
    """`Node` that takes an object from the previous node and checks it.
    If it is not contained in the `any_of` container or it doesn't pass
    the check of the `validator` `Callable` object, the whole branch until
    the closest `ForEach` node will be rejected.

    If both `any_of` and `validator` are not defined, the node processing
    has no effect.
    """
    any_of: Container[Any] | None = field(default=None)
    validator: Callable[[Any], bool] | None = field(default=None)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        if self.any_of is not None and obj not in self.any_of:
            return Result(State.REJECT)
        if self.validator is not None and not self.validator(obj):
            return Result(State.REJECT)
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        class_name = self.__class__.__name__
        msg = f"The terminal node '{class_name}' is a leaf, so it can't have any attached nodes."
        raise NotImplementedError(msg)


@dataclass(slots=True, eq=False, match_args=False, kw_only=True)
class Exclude:
    """`Node` that takes an object from the previous node and checks it.
    If it is contained in the `any_of` container or it passes the check of
    the `invalidator` `Callable` object, the whole branch until the closest
    `ForEach` node will be rejected.

    If both `any_of` and `invalidator` are not defined, the node processing
    has no effect.
    """
    any_of: Container[Any] | None = field(default=None)
    invalidator: Callable[[Any], bool] | None = field(default=None)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        if self.any_of is not None and obj in self.any_of:
            return Result(State.REJECT)
        if self.invalidator is not None and self.invalidator(obj):
            return Result(State.REJECT)
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        class_name = self.__class__.__name__
        msg = f"The terminal node '{class_name}' is a leaf, so it can't have any attached nodes."
        raise NotImplementedError(msg)


@dataclass(slots=True, eq=False, match_args=False, kw_only=True)
class At:
    """`Node` that takes an object from the previous node and treats it as
    a `Mapping` object, gets the value by key and propogates this value to
    the next nodes.
    """
    next_nodes: list[Node] = field(default_factory=list, init=False)
    key: Hashable

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        value = obj[self.key]
        for node in self.next_nodes:
            result = node.process(value, context)
            match result.state:
                case State.SUCCESS:
                    continue
                case State.REJECT:
                    return result
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        self.next_nodes.extend(args)


@dataclass(slots=True, eq=False, match_args=False, kw_only=True)
class ForEach:
    """`Node` that takes an object from the previous node and treats it
    as an `Iterable` object, iterates over it, and propogates each result
    to the next nodes.
    """
    next_nodes: list[Node] = field(default_factory=list, init=False)

    def process(self, obj: Any, context: Context[Outer, Inner]) -> Result[Outer, Inner]:
        for value in obj:
            for node in self.next_nodes:
                node.process(value, context)
        return Result(State.SUCCESS)

    def connect_with(self, *args: Node) -> None:
        self.next_nodes.extend(args)
