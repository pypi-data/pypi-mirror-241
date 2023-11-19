
'''
ConsoleX is a thin extension of rich.console.Console. It just adds
a few conveniences such as the ability to print into a string ot to
remove control codes from a string.
'''

import re

from rich.console import Console
from rich.theme import Theme
from rich.text import Text

# Styles used by Console can be seen like this
# % python3 -m rich.default_styles
# and modified like this
# from rich.default_styles import DEFAULT_STYLES
# from rich.style import Style
# DEFAULT_STYLES['red'] = Style(color='green')
# Note that justification is not part of style definitions.


class ConsoleX(Console):
    '''
    ConsoleX is a thin extension of rich.console.Console. It just adds
    a few conveniences.
    '''

    # Standard colors:
    # https://rich.readthedocs.io/en/stable/appendix/colors.html#appendix-colors
    _CUSTOM_THEME = Theme({
        'info'   : 'none',         # noqa: E203
        'warning': 'gold3',
        'error'  : 'bright_red',   # noqa: E203
    })
    # Reg ex to strip ANSI escape codes from texts:
    _DESTYLE_REX = re.compile(r'\x1b[^m]*m')

    def __init__(self, **kwargs):
        super().__init__(theme=ConsoleX._CUSTOM_THEME, **kwargs)

    def error(self, message: str) -> None:
        '''Outputs a message formatted to indicate an error.'''
        super().print(message, style='error')

    def warning(self, message: str) -> None:
        '''Outputs a message formatted to indicate a warning.'''
        super().print(message, style='warning')

    def write(self, somestring: str, **kwargs) -> None:
        '''Outputs the text in the argument to the terminal without
           LF or CR.'''
        super().print(somestring, end='', **kwargs)

    def swrite(self, somestring: str, **kwargs) -> str:
        '''Formats the console markup in the argument and returns the
           resulting string.'''
        with self.capture() as capture:
            self.write(somestring, **kwargs)
        return capture.get()

    def destyle(self, text):
        '''
        Removes styling from captured rich.console output.
        Useful for unit testing.
        '''
        # return self._DESTYLE_REX.sub('', text)
        # Try this for a while. One difference I noticed is that the
        # code below strips off newlines at the end of the text.
        return Text.from_ansi(text).plain
