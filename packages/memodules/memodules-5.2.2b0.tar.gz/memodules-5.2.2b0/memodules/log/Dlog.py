from ..extra_typing import (
    ColorStdOut,
    StdOut,
)
from dataclasses import dataclass, 
from functools import wraps
from typing import (
    NamedTuple,
    Callable,
    TypeVar,
    Any,
)
from .cprint import (
    Color,
    blue,
    border,
    gray,
    green,
    magenta,
    red,
    turquoise,
    yellow,
)
__all__ = [
    'DebugPrint',
    'log',
]
_FT = TypeVar('_FT')
_WF = TypeVar('_WF')


def log(cfunc: _FT = None, /,
        *,
        color: Color = Color.blue,
        show_call: bool = True,
        show_args: bool = True,
        show_returns: bool = True) -> _WF:
    "it is developing"
    @wraps(cfunc)
    def decorator(func: _FT) -> _WF:
        @wraps(func)
        def wrapper(*args, **kwargs) -> _WF:
            show = ''
            if show_call:
                show += f'call: {func.__name__}'
            if show_args:
                if show_call:
                    show += '\n'
                show += f'args: {args}, {kwargs}'
            if show_call or show_args:
                color(show)
            show = ''
            result = func(*args, **kwargs)
            if show_returns:
                show += f'returns: {result}'
                color(show)
            return result
        return wrapper

    if cfunc is not None:
        return decorator(cfunc)

    return decorator


class DebugPrint:
    def __init__(self, debug_flg: bool, newline_number: int = 3):
        """デバッグ用ログをデバッグフラグがTrueならcall構文で指定した引数の内容を色違いでコンソール出力してくれるクラス\n
        出力する項目をnewline_number個ごとに改行して出力を見やすくする"""
        self.debug = debug_flg
        self.nl_num = newline_number

    def __call__(self, *args):
        """examples:
            >>> debug = DebugPrint(True)
            >>> debug('debug', 'to', 'example')
            (light green)debug: debug, to, example
            >>> debug = DebugPrint(True, newline_number = 2)
            >>> debug('debug', 'to', 'example')
            debug: debug, to,
            \texample"""
        nt = '\n\t'
        spc = ' '
        if self.debug:
            for i in range(len(args)):
                if i == 0:
                    content = args[i]
                else:
                    mid_entry = nt if i % self.nl_num == 0 else spc
                    content = f'{content},{mid_entry}{args[i]}'

            print(f'\033[92mdebug: {content}\033[0m')
