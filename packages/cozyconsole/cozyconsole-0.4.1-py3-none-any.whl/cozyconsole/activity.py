
'''
Activity is a context manager for providing user feedback during the
runtime of a console application.
'''

from .consolex import ConsoleX

console = ConsoleX()


class Activity:
    # pylint: disable=too-many-instance-attributes
    '''
    Activity is a context manager for providing user feedback during the
    runtime of a console application.
    '''
    @staticmethod
    def __cursor_back(num: int) -> None:
        print(f'\033[{num}D', end='')

    styles = {
        'success': 'sea_green3',
        'warning': 'gold3',
        'failure': 'bright_red',
    }

    def __init__(self, message: str,
                 pass_suffix: str = 'done',
                 fail_suffix: str = 'failed',
                 handle_exceptions: bool = True,
                 show_exception_message: bool = True,
                 show_tracebacks: bool = True):
        self._message = message
        self._pass_suffix = pass_suffix
        self._fail_suffix = fail_suffix
        self._handle_exceptions = handle_exceptions
        self._show_exception_message = show_exception_message
        self._show_tracebacks = show_tracebacks
        self._success = False
        self._warning = None
        self._result  = None

    def __enter__(self):
        console.write(f'{self._message}...', highlight=False)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__cursor_back(3)
        result = self._pass_suffix if self._success else self._fail_suffix
        color = (Activity.styles['success']
                 if self._success
                 else Activity.styles['failure'])
        if self._result:
            result = self._result
        if self._warning:
            result = self._warning
            color = Activity.styles['warning']
        console.print(f'[{color}] - {result}')

        if exc_value and self._handle_exceptions:
            if self._show_tracebacks:
                console.print_exception(show_locals=True)
            elif self._show_exception_message:
                console.error(exc_value)
            self._result = exc_value
            return True

        return self._handle_exceptions

    # pylint: disable=missing-function-docstring

    @property
    def success(self) -> bool:
        return self._success
    @success.setter   # noqa: E301
    def success(self, value: bool):
        self._success = value

    @property
    def warning(self) -> str:
        return None
    @warning.setter   # noqa: E301
    def warning(self, value: str):
        self._warning = value

    @property
    def result(self) -> str:
        return None
    @result.setter   # noqa: E301
    def result(self, value: str):
        self._result = value
