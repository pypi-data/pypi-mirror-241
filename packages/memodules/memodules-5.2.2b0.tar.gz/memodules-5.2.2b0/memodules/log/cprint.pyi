from .cprint import blue
from ..extra_typing import (
    ColorStdOut,
)
from typing import (
    Callable,
    Generic,
    TypeVar,
    get_args,
    Any,
)
__all__ = [
    # const
    'Color',

    # functions
    # #custom
    'cprint',

    # #presets
    'blue',
    'gray',
    'green',
    'magenta',
    'red',
    'turquoise',
    'yellow',

    # #decoration
    'border',
]
_AT = TypeVar('_AT')


def cprint(*args: _AT,
           color: str,
           undo_when_exit: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Color of Custom`"
def gray(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Gray Color`"
def red(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Red Color`"
def green(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Green Color`"
def yellow(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Yellow Color`"
def blue(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Blue Color`"
def magenta(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Magenta Color`"
def turquoise(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Turquoise Color`"
def border(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
    "Print to Console in `Border String`"


class _Args(Generic[_AT]):
    __args = '*values'
    __parameters: Any
    __paramspec_tvars: Any

    @property
    def __args__(self):
        return '*values: _AT'
    
    @__args__.setter
    def __args__(self, value):
        self.__args = value

    @property
    def __parameters__(self):
        return self.__parameters
    
    @__parameters__.setter
    def __parameters__(self, value):
        self.__parameters = value

    @property
    def _paramspec_tvars(self):
        return self.__paramspec_tvars
    
    @_paramspec_tvars.setter
    def _paramspec_tvars(self, value):
        self.__paramspec_tvars = value


_args = _Args()
class Color:
    "Constant of 'cprint' Function"
    # region difinition
    def _blue(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Blue Color`"
    def _gray(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Gray Color`"
    def _green(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Green Color`"
    def _magenta(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Magenta Color`"
    def _red(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Red Color`"
    def _turquoise(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Turquoise Color`"
    def _yellow(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Yellow Color`"
    def _border(*values: _AT, default: bool = True) -> ColorStdOut[_AT]:
        "Print to Console in `Border String`"
    # endregion
    class _gs:
        __name__ = '*values'
        __args__ = '*values'
        __parameters__ = '*values'
        __repr__ = '*values'
        __reduce__ = '*values'
        __getitem_inner__ = '*values'
    blue: Callable[[_gs], ColorStdOut[_AT]]
    gray: _gray
    green: _green
    magenta: _magenta
    red: _red
    turquoise: _turquoise
    yellow: _yellow
    border: _border


if __name__ == '__main__':
    blue('test', 'to', 'debug')
    Color.border
