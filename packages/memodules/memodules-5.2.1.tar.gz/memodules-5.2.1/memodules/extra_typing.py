"""It provides an extra class that has no function and can only be used for type hints.\n
何の機能も無い、型ヒントだけに使えるエクストラなクラスを提供するやで。"""
from typing import TypeVar, Generic
__all__ = [
    'SupportIndex',
    'SupportPath',
]
_AT = TypeVar('_AT')  # T は任意の型を表す型変数


class TestType:
    @classmethod
    def __class_getitem__(cls, *item):
        cls.__annotations__ = {'testarg': 'testtype[str]'}


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
