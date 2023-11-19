# pylint: disable = missing-function-docstring, missing-module-docstring

from cozyconsole.consolex import ConsoleX


console = ConsoleX(force_terminal=True)
# The force_terminal option is required to allow tests run by tox in Git Bash
# on Windows to succeed. Without the option there will by no terminal and
# therefore no color.


def test_output():
    with console.capture() as capture:
        console.error('error')
        console.warning('warning')
        console.write('message')
    text = capture.get()
    assert len(text.split('\n')) == 3
    assert not text.endswith('\n')
    #with open('output.txt', 'w') as fp:
    #    fp.write(text)
    assert '\x1b[91merror' in text          # in bright_red
    assert '\x1b[38;5;178mwarning' in text  # in dark_orange
    assert '\033[0m' in text                # off


def test_sprint():
    text = console.swrite('Some [red]red[/] and [bold cyan]bold cyan[/] text.')
    assert '\x1b[31mred' in text
    assert '\x1b[1;36mbold cyan' in text


def test_destyle():
    text = console.swrite('[red]red[/] and [bold cyan]bold cyan')
    destyled = console.destyle(text)
    assert '\x1b[31mred' not in destyled
    assert '\x1b[1;36mbold cyan' not in destyled
    assert '\033[0m' not in destyled
    assert 'red and bold cyan' == destyled
