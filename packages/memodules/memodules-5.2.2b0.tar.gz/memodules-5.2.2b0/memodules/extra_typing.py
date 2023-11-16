"""It provides an extra class that has no function and can only be used for type hints.\n
何の機能も無い、型ヒントだけに使えるエクストラなクラスを提供するやで。"""
from typing import TypeVar, Generic
__all__ = [
    'ColorStdOut',
    'StdOut',
    'SupportIndex',
    'SupportPath',
]
_AT = TypeVar('_AT')  # T は任意の型を表す型変数


class _NotIterable:
    """Mixin to prevent iteration, without being compatible with Iterable.

    That is, we could do:
        def __iter__(self): raise TypeError()
    But this would make users of this mixin duck type-compatible with
    collections.abc.Iterable - isinstance(foo, Iterable) would be True.

    Luckily, we can instead prevent iteration by setting __iter__ to None, which
    is treated specially.
    """

    __slots__ = ()
    __iter__ = None


class StdOut(Generic[_AT]):
    '<TypeHints to indicate that it will be printed to the console>'
    def __str__(self) -> str:
        return '<type hints StdOut>'

    def __repr__(self) -> str:
        return self.__doc__


class ColorStdOut(StdOut, Generic[_AT]):
    def __str__(self) -> str:
        return '<type hints ColorStdOut>'


class SupportIndex(Generic[_AT]):
    def __init__(self, value: _AT):
        self.value = value

    def get_value(self) -> _AT:
        return self.value


class SupportPath(Generic[_AT]):
    def __init__(self, value: _AT):
        self.value = value

    def get_value(self) -> _AT:
        return self.value
