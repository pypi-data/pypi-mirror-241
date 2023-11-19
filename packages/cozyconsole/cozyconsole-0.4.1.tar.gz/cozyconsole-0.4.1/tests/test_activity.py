# pylint: disable = missing-function-docstring
# pylint: disable = missing-module-docstring
# pylint: disable = using-constant-test

import time

import pytest
from rich.text import Text

from cozyconsole.activity import Activity
from cozyconsole.consolex import ConsoleX


# We need to use the console instance in the Activity instance to be able to
# capture the latter's output in the test cases below. Further, on Windows,
# That console instance must be recreated as shown here:
import cozyconsole.activity
cozyconsole.activity.console = ConsoleX(color_system='truecolor',
                                        force_terminal=True)
console = cozyconsole.activity.console
# This allows the tests to succeed when they are run by tox in Git Bash on Windows.
# Without the option there will by no terminal and therefore no color.
# The options are not required on Linux and MacOS, but their presence does no
# harm, either.


def do_something(go_boom: str = None):
    time.sleep(0.01)
    if go_boom:
        raise RuntimeError(go_boom)


def test_successful():
    if '''Using the default completion "- done:''':
        with console.capture() as capture:
            with Activity('A successful operation') as act:
                do_something()
                act.success = True
        colored = capture.get()
        plain = console.destyle(colored)
        assert '\x1b[38;5;78m - done\x1b[0m' in colored
        assert 'A successful operation... - done' == plain
        # Note that the actual screen output shows "..." only during the
        # operation.
    if '''Using a custom completion word''':
        with console.capture() as capture:
            with Activity('A successful operation') as act:
                do_something()
                act.result = 'nice'
                act.success = True
        colored = capture.get()
        plain = console.destyle(colored)
        assert '\x1b[38;5;78m - nice\x1b[0m' in colored


def test_unsuccessful():
    with console.capture() as capture:
        with Activity('An unsuccessful operation'):
            do_something()
    colored = capture.get()
    plain = console.destyle(colored)
    # print(f'{colored=}')
    # print(f'{plain=}')
    assert '\x1b[91m - failed\x1b[0m' in colored
    assert 'An unsuccessful operation... - failed' == plain


def test_warning():
    with console.capture() as capture:
        with Activity('A warning') as act:
            do_something()
            act.warning = 'attention!'
    colored = capture.get()
    plain = console.destyle(colored)
    assert '\x1b[38;5;178m - attention!\x1b[0m' in colored
    assert 'A warning... - attention!' == plain


def test_exception():
    with console.capture() as capture:
        with Activity('Exception with a stack trace'):
            do_something(go_boom='expected failure')
    out = capture.get()
    plain = Text.from_ansi(out).plain
    assert 'Traceback' in plain
    assert 'RuntimeError: expected failure' in plain


def test_exception_no_traceback():
    with console.capture() as capture:
        with Activity('Exception without a stack trace',
                      show_tracebacks=False):
            do_something(go_boom='expected failure')
    colored = capture.get()
    assert '\x1b[91m - failed\x1b[0m' in colored
    assert 'Traceback' not in colored
    assert 'RuntimeError: expected failure' not in colored


def test_unhandled_exception():
    with console.capture() as capture:
        with pytest.raises(FileNotFoundError):
            with Activity('Doomed to fail', handle_exceptions=False):
                raise FileNotFoundError()
    colored = capture.get()
    assert '\x1b[91m - failed\x1b[0m' in colored
    assert 'Doomed to fail' in colored
