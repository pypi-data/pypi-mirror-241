# pylint: disable = missing-function-docstring, missing-module-docstring

from importlib.metadata import version
import os
from pathlib import Path
import shutil
import sys

import pytest
import semver

from cozyconsole.markdownpatcher import console, main, MarkdownPatcher
import cozyconsole.markdownpatcher


rich_version = semver.Version.parse(version('rich'))


@pytest.mark.skipif(rich_version.major < 13,
                    reason='The test requires Rich V13')
def test_patch():
    # pylint: disable=protected-access, import-outside-toplevel
    curr_path = Path().cwd().resolve()
    test_path = Path(__file__).parent.resolve()
    try:
        from rich.markdown import __file__ as md_module
        os.chdir(test_path)
        shutil.copy(md_module, 'markdown_copy.py')
        mock_path = test_path / 'markdown_copy.py'
        cozyconsole.markdownpatcher.markdown_module_path = str(mock_path)
        # The markdownpatcher will work on the copy now.
        mdpatcher = MarkdownPatcher()
        mdpatcher.ingest_code()
        # if this fails it means that the current venv contains a patched
        # markdown.py.
        assert mdpatcher.justification == '"center"'
        if '''Confirm that when the program is called without args the
              correct current justificationm is returned.''':
            with console.capture() as capture:
                sys.argv = ['proggie']
                main()
            output = capture.get()
            result = console.destyle(output)
            assert 'currently set to \'"center"\'' in result
        if '''Verify that the patch will not be re-applied.''':
            with console.capture() as capture:
                sys.argv = ['proggie', '-j', 'center']
                main()
            output = capture.get()
            result = console.destyle(output)
            #print(f'{result=}')
            assert 'already uses "center"' in result
        if '''Verify that the patch will be applied.''':
            with console.capture() as capture:
                sys.argv = ['proggie', '-j', 'left']
                main()
            output = capture.get()
            errors = console.destyle(output)
            assert not errors
            mdpatcher.ingest_code()
            assert '"left"' in mdpatcher.justification
    finally:
        Path('markdown_copy.py').unlink()
        os.chdir(curr_path)
    # print(f'{test_path=}')
    # print(f'{cozyconsole.markdownpatcher.markdown_module_path=}')
