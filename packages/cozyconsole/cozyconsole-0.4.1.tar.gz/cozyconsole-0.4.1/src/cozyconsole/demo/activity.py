
'''
Demonstrates the various features of the cozyconsole.activity module.
'''

from math import sqrt
from random import uniform
from textwrap import dedent
from time import sleep

from rich.markdown import Markdown

from cozyconsole.consolex import ConsoleX
from cozyconsole.activity import Activity

console = ConsoleX()


def python_prompt(linefeed: bool = False):
    '''Simulates a Python prompt.'''
    console.write('>>> ')
    sleep(0.3)
    if linefeed:
        console.write('\n')


def shell_prompt(linefeed: bool = False):
    '''Simulates a shell prompt.'''
    console.write('[b cyan]~/dev/demo[/] (venv) [b]$[/] ')
    sleep(0.3)
    if linefeed:
        console.write('\n')


def slow_print(text: str, endl: str = '',
               min_interval: float = 0.05, max_interval: float = 0.1):
    '''Simulates typing letter for letter.'''
    for char in text:
        console.write(char)
        sleep(uniform(min_interval, max_interval))
    console.write(endl)


def slow_print_line_color(line):
    '''
    Simulates typing word for word. This allows Rich to apply
    color-coding.
    '''
    # Write the Python interpreter prompt.
    if line.startswith('>>> ') or line.startswith('... '):
        console.write(line[0:4])
        line = line[4:]
    sleep(0.3)
    # Write any indent.
    indent = len(line) - len(line.lstrip())
    console.write(' ' * indent)
    # Write the rest of the line word for word.
    for word in line.split():
        sleep(0.1)
        console.write(word)
        sleep(0.2)
        console.write(' ')
    console.write('\n')


def slow_print_python_code(codetext, color=True):
    '''Simulates typing some lines of code into a Python interpreter.'''
    for line in dedent(codetext).strip().splitlines():
        if color:
            slow_print_line_color(line)
        else:
            slow_print(line)
            console.write('\n')


def demo_activity():   # noqa: C901
    # pylint: disable = too-many-statements, using-constant-test, line-too-long
    '''Demos the various features of the Activity class.'''
    if '''Demo the basic features.''':
        console.print(
            Markdown('# Progress and status feedback using the Activity class')
        )
        sleep(1)
        shell_prompt()
        slow_print('venvx create .venv', endl='\n')
        with Activity('Creating virtual environment [b].venv[/]') as act:
            sleep(1)
            act.success = True
        with Activity('Checking if an upgrade is available for [b]pip[/]') as act:   # noqa: E501
            sleep(1)
            act.result = 'yes' if True else 'no'
            act.success = True
        with Activity('Updating [b]pip[/] from v22.3.1 to [b]v23.0.1[/]') as act:   # noqa: E501
            sleep(1)
            act.success = True
        with Activity('Checking if any scripts require patches') as act:
            sleep(0.7)
            act.warning = 'yes'
            act.success = True
        with Activity('Fixing the shebang in [b]activate.csh[/]') as act:
            sleep(0.5)
            act.success = True
        with Activity('Fixing the VIRTUAL_ENV setting in [b]activate[/]') as act:   # noqa: E501
            sleep(0.5)
            act.success = True
        with Activity('Checking if any scripts require patches') as act:
            sleep(0.7)
            act.result = 'no'
            act.success = True
        shell_prompt()
        slow_print('ls -la', endl='\n')
        console.print('drwxr-xr-x   user  group    ./')
        console.print('drwxr-xr-x   user  group    ../')
        console.print('drwxr-xr-x   user  group    .venv/')
        shell_prompt()
        sleep(1)
        slow_print('venvx create .venv', endl='\n')
        with Activity('Creating virtual environment [b].venv[/]') as act:
            sleep(0.2)
        console.print('The folder [b].venv[/] already exists.\n')

    console.print(
        Markdown('# Handling exceptions with the Activity class')
    )

    if '''Demo letting the exception propagate.''':
        shell_prompt()
        slow_print('python3', endl='\n')
        python_prompt()
        slow_print('# Option 1: The caller handles any exceptions.',
                   endl='\n')
        codetext = '''
            >>> from rich.console import Console
            >>> from cozyconsole.activity import Activity
            >>> console = Console()
            >>> try:
            >>>     with Activity('Opening missing file vanished.txt',
            ...                    handle_exceptions=False) as act:
            ...         with open('vanished.txt'):
            ...             pass
            ... except FileNotFoundError:
            ...     console.print('Please find and restore vanished.txt.')
            ... except:
            ...     console.print_exception(show_locals=True)
            ... finally:
            ...     raise SystemExit()
            ...
        '''
        slow_print_python_code(codetext)
        sleep(0.5)
        try:
            with Activity('Opening missing file vanished.txt',
                          handle_exceptions=False) as act:
                with open('vanished.txt', encoding='utf-8'):
                    pass
        except FileNotFoundError:
            console.print('Please find and restore vanished.txt.')
        except Exception:   # pylint: disable = broad-exception-caught
            console.print_exception(show_locals=True)
        # python_prompt()
        # console.print()
        shell_prompt()

    sleep(2)

    if '''Demo handling the exception with a traceback.''':
        console.print()
        shell_prompt()
        slow_print('python3', endl='\n')
        python_prompt()
        # sleep(2)
        slow_print('# Option 2: The Activity class handles exceptions, '
                   'and shows a traceback.', endl='\n')
        codetext = '''
            >>> from cozyconsole.activity import Activity
            >>> with Activity('Trying something imaginary',
            ...               handle_exceptions=True,
            ...               show_tracebacks=True) as act:
            ...     result = math.sqrt(-1)
            ...
        '''
        slow_print_python_code(codetext)
        sleep(0.5)
        with Activity('Trying something imaginary',
                      handle_exceptions=True, show_tracebacks=True) as act:
            sqrt(-1)
        python_prompt()
        slow_print('exit()', endl='\n')
        shell_prompt()

    sleep(2)

    if '''Demo handling the exception, don't show a traceback.''':
        console.print()
        shell_prompt()
        slow_print('python3', endl='\n')
        python_prompt()
        slow_print('# Option 3: Let the Activity class handle exceptions '
                   'silently.', endl='\n')
        codetext = '''
            >>> from urllib.request import urlopen
            >>> from cozyconsole.activity import Activity
            >>> with Activity('Checking if server is up',
            ...               handle_exceptions=True,
            ...               show_exception_message=False,
            ...               show_tracebacks=False) as act:
            ...     act.warning = 'server is down'
            ...     # This will throw urllib.error.URLError:
            ...     with urlopen('http://192.168.1.1/myservice012304120',
            ...                  timeout=0.5) as response:
            ...         response.read()
            ...     # This code won't be reached.
            ...     act.result = 'OK'
            ...     act.success = True
            ...
        '''
        slow_print_python_code(codetext)
        sleep(0.5)
        with Activity('Checking if server is up',
                      handle_exceptions=True, show_tracebacks=False,
                      show_exception_message=False) as act:
            # pylint: disable = import-outside-toplevel
            from urllib.request import urlopen
            act.warning = 'server is down'
            # This will throw urllib.error.URLError:
            with urlopen('http://192.168.1.1/myservice012304120',
                         timeout=0.5) as response:
                response.read()
            # This code won't be reached.
            act.result = 'OK'
            act.success = True
        python_prompt()
        slow_print('exit()', endl='\n')
        shell_prompt(True)

    sleep(1)
    console.print(
        Markdown('#')
    )
