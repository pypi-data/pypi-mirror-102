from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Generic,
    Iterator,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from typing_extensions import final

# Single-sourcing the version number with poetry:
# https://github.com/python-poetry/poetry/pull/2366#issuecomment-652418094
try:
    __version__ = __import__("importlib.metadata").metadata.version(__name__)
except ModuleNotFoundError:  # pragma: no cover
    __version__ = __import__("importlib_metadata").version(__name__)

__all__ = [
    "Just",
    "Maybe",
    "Nothing",
    "flatten",
    "maybe_from_optional",
]

T = TypeVar("T", covariant=True)
U = TypeVar("U", covariant=True)
V = TypeVar("V")


# Why not the Rust-like Option(Some/None) terminology?
#     (1) it's confusing with Optional
#     (2) `None` is reserved in Python
class _MaybeMixin(Generic[T], Sequence[T]):
    """Collection of methods supported by both
    :class:`~cans.Just` and :class:`~cans.Nothing`.
    """

    __slots__ = ()

    def __init__(self) -> None:
        raise TypeError(
            "Can't instantiate Maybe directly. "
            "Use the factory methods `of` and `from_optional` instead."
        )

    def unwrap(self) -> T:
        """Unwrap the value in this container.
        If there is no value, :class:`TypeError` is raised.

        Example
        -------

        >>> Just(6).unwrap()
        6
        >>> Nothing().unwrap()
        Exception: TypeError()

        Tip
        ---

        Only use this if you're absolutely sure that there is a value.
        If not, use :meth:`~cans._MaybeMixin.unwrap_or` instead.
        Or, use :meth:`~cans._MaybeMixin.expect`
        for a more descriptive message.
        """
        raise NotImplementedError()

    def unwrap_or(self, _default: V) -> Union[T, V]:
        """Unwrap the value in this container.
        If there is no value, return the given default.

        Example
        -------

        >>> Just(8).unwrap_or("foo")
        8
        >>> Nothing().unwrap_or("foo")
        "foo"
        """
        raise NotImplementedError()

    def expect(self, _msg: str) -> T:
        """Unwrap the value in this container.
        If there is no value, raise an AssertionError with message

        >>> Just(9).expect("What on earth?")
        9
        >>> Nothing().expect("What did you expect?")
        Exception: AssertionError("What did you expect?")
        """
        raise NotImplementedError()

    def is_just(self) -> bool:
        """True if this `Maybe` contains a value

        Example
        -------

        >>> Just(2).is_just()
        True
        >>> Nothing().is_just()
        False

        """
        raise NotImplementedError()

    def is_nothing(self) -> bool:
        """True if this `Maybe` does not contain a value

        Example
        -------

        >>> Just(2).is_nothing()
        False
        >>> Nothing().is_nothing()
        True

        """
        raise NotImplementedError()

    def map(self, _func: Callable[[T], U]) -> "Maybe[U]":
        """Apply a function to the value inside the `Maybe`,
        without unwrapping it.

        Example
        -------

        >>> Just("hello").map(str.upper)
        Just("HELLO")
        >>> Nothing().map(abs)
        Nothing()

        """
        raise NotImplementedError()

    def filter(self, _func: Callable[[T], bool]) -> "Maybe[T]":
        """Keep the value inside only if it satisfies the given predicate.

        Example
        -------

        >>> Just("9").filter(str.isdigit)
        Just("9")
        >>> Just("foo").filter(str.isdigit)
        Nothing()
        >>> Nothing().filter(str.isdigit)
        Nothing()
        """
        raise NotImplementedError()

    def zip(self, _other: "Maybe[U]") -> "Maybe[Tuple[T, U]]":
        """Combine two values in a tuple, if both are present.

        Example
        -------

        >>> Just(8).zip(Just(2))
        Just((8, 2))
        >>> Just(7).zip(Nothing())
        Nothing()
        >>> Nothing().zip(Just(3))
        Nothing()
        >>> Nothing().zip(Nothing())
        Nothing()
        """
        raise NotImplementedError()

    def flatmap(self, _func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        """Apply a function (which returns a maybe)
        to the value inside the ``Maybe``.
        Then, flatten the result.

        Example
        -------

        >>> def first(s) -> Maybe:
        ...     try:
        ...          return Just(s[0])
        ...     except LookupError:
        ...          return Nothing()
        ...
        >>> Just([9, 4]).flatmap(first)
        Just(9)
        >>> Just([]).flatmap(first)
        Nothing()
        >>> Nothing().flatmap(first)
        Nothing()
        """
        raise NotImplementedError()

    def as_optional(self) -> Optional[T]:
        """Convert the value into an possibly-None value.

        Example
        -------

        >>> Just(6).as_optional()
        6
        >>> Nothing().as_optional()
        None

        """
        raise NotImplementedError()

    def setdefault(self, _v: V) -> "Maybe[Union[T, V]]":
        """Set a value if one is not already present.

        Example
        -------

        >>> Just(6).setdefault(7)
        Just(6)
        >>> Nothing().setdefault(3)
        Just(3)

        """
        raise NotImplementedError()

    def and_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        """
        Perform a logical AND operation.
        Returns the first Nothing, or the last of the two values.

        Tip
        ---

        Available as the :meth:`~cans._MaybeMixin.and_` method
        as well as the ``&`` operator.

        Example
        -------

        >>> Just(5) & Just(9)
        Just(9)
        >>> Just(5).and_(Just(9))
        Just(9)
        >>> Just(9) & Nothing()
        Nothing()
        >>> Nothing() & Just(8)
        Nothing()

        """
        raise NotImplementedError()

    __and__ = and_

    def or_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        """Perform a logical OR operation.
        Return the first Just, or the last of the two values.

        Tip
        ---

        Available as the :meth:`~cans._MaybeMixin.or_` method
        as well as the ``|`` operator.

        Example
        -------

        >>> Just(5) | Just(9)
        Just(5)
        >>> Just(5).or_(Just(9))
        Just(5)
        >>> Just(9) | Nothing()
        Just(9)
        >>> Nothing() | Just(8)
        Just(8)
        >>> Nothing() | Nothing()
        Nothing()
        """
        raise NotImplementedError()

    __or__ = or_

    def __iter__(self) -> Iterator[T]:
        """Iterate over the contained item, if present.

        Example
        -------

        >>> list(Just(5))
        [5]
        >>> list(Nothing())
        []
        """
        raise NotImplementedError()

    def __contains__(self, _v: object) -> bool:
        """Check if the item is contained in this object.

        Example
        -------

        >>> 5 in Just(5)
        True
        >>> 4 in Just(8)
        False
        >>> 1 in Nothing()
        False
        """
        raise NotImplementedError()

    def __len__(self) -> int:
        """The number of items contained (0 or 1)

        Example
        -------

        >>> len(Just(5))
        1
        >>> len(Nothing())
        0
        """
        raise NotImplementedError()

    @overload
    def __getitem__(self, _i: int) -> T:
        ...

    @overload
    def __getitem__(self, _i: slice) -> "Maybe[T]":
        ...

    def __getitem__(self, _i: Union[int, slice]) -> Union[T, "Maybe[T]"]:
        """Get the item from this container by index.
        Part of the :class:`~collections.abc.Sequence` API.

        Behaves similarly to a list of one or zero items.

        Example
        -------

        >>> Just(6)[0]
        6
        >>> Just(8)[8]
        Exception: IndexError
        >>> Nothing()[0]
        Exception: IndexError
        ...
        >>> Just(6)[:]
        Just(6)
        >>> Just(2)[:9:4]
        Just(2)
        >>> Just(7)[2:]
        Nothing()
        >>> Nothing()[:]
        Nothing()
        >>> Nothing()[2:9:5]
        Nothing()
        """
        raise NotImplementedError()


@final
@dataclass(frozen=True, repr=False)
class Just(_MaybeMixin[T]):
    """The version of :class:`~cans.Maybe` which contains a value.

    Example
    -------

    >>> a: Maybe[int] = Just(-8)
    >>> a.map(abs).unwrap()
    8

    """

    __slots__ = ("_value",)

    _value: T

    def unwrap(self) -> T:
        return self._value

    def unwrap_or(self, _default: V) -> Union[T, V]:
        return self._value

    def expect(self, _msg: str) -> T:
        return self._value

    def is_just(self) -> bool:
        return True

    def is_nothing(self) -> bool:
        return False

    def map(self, _func: Callable[[T], U]) -> "Maybe[U]":
        return Just(_func(self._value))

    def filter(self, _func: Callable[[T], bool]) -> "Maybe[T]":
        return self if _func(self._value) else _NOTHING

    def zip(self, _other: "Maybe[U]") -> "Maybe[Tuple[T, U]]":
        return (
            Just((self._value, _other.unwrap()))
            if _other.is_just()
            else _NOTHING
        )

    def flatmap(self, _func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        return flatten(self.map(_func))

    def as_optional(self) -> Optional[T]:
        return self._value

    def setdefault(self, _v: V) -> "Maybe[Union[T, V]]":
        return self

    def and_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        return _other

    __and__ = and_

    def or_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        return self

    __or__ = or_

    def __repr__(self) -> str:
        return f"Just({self._value})"

    def __iter__(self) -> Iterator[T]:
        yield self._value

    def __contains__(self, _v: object) -> bool:
        return self._value == _v

    def __len__(self) -> int:
        return 1

    def __bool__(self) -> bool:
        return True

    def __getstate__(self) -> tuple:
        return (self._value,)

    def __setstate__(self, state: tuple) -> None:
        object.__setattr__(self, "_value", state[0])

    @overload
    def __getitem__(self, _i: int) -> T:
        ...

    @overload
    def __getitem__(self, _i: slice) -> "Maybe[T]":
        ...

    def __getitem__(self, _i: Union[int, slice]) -> Union[T, "Maybe[T]"]:
        if isinstance(_i, slice):
            return self if _i.indices(1)[:2] == (0, 1) else _NOTHING
        elif _i == 0:
            return self._value
        else:
            raise IndexError("Only index 0 can be retrieved from container.")


@final
@dataclass(frozen=True)
class Nothing(_MaybeMixin[T]):
    """The version of :class:`~cans.Maybe` which does not contain a value.

    Example
    -------

    >>> a: Maybe[int] = Nothing()
    >>> a.map(abs).unwrap_or("nope")
    "nope"

    """

    __slots__ = ()

    def unwrap(self) -> T:
        raise TypeError("Cannot unwrap an empty `Maybe`.")

    def unwrap_or(self, _default: V) -> Union[T, V]:
        return _default

    def expect(self, _msg: str) -> T:
        raise AssertionError(_msg)

    def is_just(self) -> bool:
        return False

    def is_nothing(self) -> bool:
        return True

    def map(self, _func: Callable[[T], U]) -> "Maybe[U]":
        return _NOTHING

    def filter(self, _func: Callable[[T], bool]) -> "Maybe[T]":
        return _NOTHING

    def zip(self, _other: "Maybe[U]") -> "Maybe[Tuple[T, U]]":
        return _NOTHING

    def flatmap(self, _func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        return _NOTHING

    def as_optional(self) -> Optional[T]:
        return None

    def setdefault(self, _v: V) -> "Maybe[Union[T, V]]":
        return Just(_v)

    def and_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        return _NOTHING

    __and__ = and_

    def or_(self, _other: "Maybe[U]") -> "Maybe[Union[T, U]]":
        return _other

    __or__ = or_

    def __iter__(self) -> Iterator[T]:
        return _EMPTY_ITERATOR

    def __contains__(self, _v: Any) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def __bool__(self) -> bool:
        return False

    def __getstate__(self) -> tuple:
        return ()

    def __setstate__(self, state: tuple) -> None:
        pass

    @overload
    def __getitem__(self, _i: int) -> T:
        ...

    @overload
    def __getitem__(self, _i: slice) -> "Maybe[T]":
        ...

    def __getitem__(self, _i: Union[int, slice]) -> Union[T, "Maybe[T]"]:
        if isinstance(_i, slice):
            return _NOTHING
        else:
            raise IndexError("No items in this container.")


# Q: Why declare this as a union, and not a base class?
# A: So that mypy can properly infer that there are only two variants,
#    and thus handle conditionals and pattern matching accordingly.
Maybe = Union[Just[T], Nothing[T]]
"""
A container which contains either one item, or none.
Use :class:`~cans.Just` and :class:`~cans.Nothing` to express
these two variants.
When type annotating, only use :data:`~cans.Maybe`.

>>> a: Maybe[int] = Just(5)
>>> b: Maybe[str] = Nothing()
...
>>> def parse(s: str) -> Maybe[int]:
...     try: return Just(int(s))
...     except ValueError: return Nothing()
...
>>> def first(m: list[T]) -> Maybe[T]:
...     return Just(m[0]) if m else Nothing()
...
>>> parse("42")
Just(42)
>>> first([])
Nothing()

Various methods are available (documented in :class:`~cans._MaybeMixin`)
which you can use to operate on the value, without repeatedly unpacking it.

>>> first(["-5", "6", ""]).flatmap(parse).map(abs)
Just(5)
>>> first([]).flatmap(parse).map(abs).unwrap_or("Nothing here...")
"Nothing here..."

In Python 3.10+, you can use pattern matching to deconstruct
a :class:`~cans.Maybe`.

>>> match first(["bob", "henry", "anita"]).map(str.title):
...     case Just(x):
...         print(f'Hello {x}!')
...     case Nothing()
...         print('Nobody here...')
"Hello Bob!"

:class:`~cans.Maybe` also implements the
:class:`~collections.abc.Sequence` API,
meaning it acts kind of like a list with one or no items.
Thus, it works nicely with :mod:`itertools`!

>>> from itertools import chain
>>> list(chain.from_iterable(map(parse, "a4f59b")))
[4, 5, 9]
"""

_NOTHING: Maybe = Nothing()
_EMPTY_ITERATOR: Iterator = iter(())


def flatten(m: "Maybe[Maybe[T]]") -> "Maybe[T]":
    """Flatten two nested maybes.

    Example
    -------

    >>> flatten(Just(Just(5)))
    Just(5)
    >>> flatten(Just(Nothing()))
    Nothing()
    >>> flatten(Nothing())
    Nothing()
    """
    return m.unwrap() if m.is_just() else m  # type: ignore


def maybe_from_optional(_v: Optional[T]) -> "Maybe[T]":
    """Create a maybe container from the given value, which may be ``None``.
    In that case, it'll be an empty Maybe.

    Example
    -------

    >>> maybe_from_optional(5)
    Just(5)
    >>> maybe_from_optional(None)
    Nothing()
    """
    return _NOTHING if _v is None else Just(_v)
