
'''
This is a hack which patches the rich.markdown module. It changes the
text alignment of H2 and higher headings from "center" to "left", and
back.
'''

from argparse import ArgumentParser
import os
import re

from rich.markdown import __file__ as markdown_module_path

from cozyconsole.consolex import ConsoleX

PATCH_IS_INCOMPATIBLE_WITH_RICH_MSG = (
    'This code works with Rich v13.3.2. It does not work with the '
    'version of Rich currently installed.'
)

console = ConsoleX()


class MarkdownPatcher:   # MarkdownModule
    '''
    Patches the rich,markdown moudule. The lustification of H2, H3, and
    so forth headings is changed from centered to left-aligned. H1
    headings remain centered. It is also possible to restore the markdown
    module to its original state.
    '''
    _full_text: str         # content of the file
    _heading_section: str   # just the source code text of class Heading
    _start_index: int       # index with full_text where class Heading starts
    _end_index: int         # index with full_text where class Heading ends

    @property
    def justification(self):
        '''Returns the current text.justify setting for headings.'''
        return self._current_justification

    def __init__(self):
        self._module_path = markdown_module_path
        self._current_justification = None

    def ingest_code(self):
        '''
        Parses rich.markdown.py.
        '''
        self._read_code()
        self._find_heading_section()
        self._get_justification()

    def apply_patch(self, from_alignment, to_alignment):
        '''
        Modifies the justification of H2 and higher Markdown headings.
        '''
        original = f'text.justify = {from_alignment}\n'
        replacement = f'text.justify = {to_alignment}\n'
        # print(f'{original=}')
        # print(f'{replacement=}')
        found = self._heading_section.find(original) > 0
        if not found:
            console.print('Could not find the code to patch.')
            return
        self._patch_and_write_code(original, replacement)

    def _read_code(self):
        '''Load the rich.markdown source code.'''
        if (self._module_path.startswith('/opt') or
            self._module_path.startswith('/usr')):   # noqa: E129
            # Meaningless on Windows of course :(
            console.warning('The Rich markdown module is installed in a '
                            'shared location. Leaving it alone, and running '
                            'away scared.')
            return
        if not os.access(self._module_path, os.W_OK):
            console.print('You do not have permissions to overwrite '
                        f'{self._module_path}.')   # noqa: E128
            return
        with open(self._module_path, encoding='utf-8') as md:
            self._full_text = md.read()

    def _patch_and_write_code(self, original, replacement):
        '''Replace the current justification setting and save the file.'''
        new_code = self._heading_section.replace(original, replacement)
        with open(self._module_path, 'w', encoding='utf-8') as md:
            # pylint disable = invalid-name
            md.write(self._full_text[0:self._start_index])
            md.write(new_code)
            md.write(self._full_text[self._end_index:])
        self._current_justification = replacement

    def _find_heading_section(self):
        '''Locate the code for class Heading.'''
        rex1 = re.compile(r'^class (.+)\(.+\):$', flags=re.M)
        classnames = rex1.findall(self._full_text)
        classdefs  = list(rex1.finditer(self._full_text))
        classindex = classnames.index('Heading')
        codestart = classdefs[classindex].start()
        codeend   = classdefs[classindex+1].start()
        self._heading_section = self._full_text[codestart:codeend]
        self._start_index = codestart
        self._end_index = codeend

    def _get_justification(self):
        '''Find the current justification setting.'''
        rex = re.compile(r'^\s*text\.justify\s+=\s+(.+)$', flags=re.M)
        found = rex.findall(self._heading_section)
        self._current_justification = found[0] if found else None


def on_justify(args):
    '''
    This gets called by argparse if the -j|--justify switch is in the
    command line. It toggles the justify setting for H2 and higher
    headings, depending on the --justify argument.
    '''
    if not markdownPatcher.justification:
        console.print(PATCH_IS_INCOMPATIBLE_WITH_RICH_MSG)
        return
    options = {
        'center': '"center"',
        'left': '"center" if self.tag == "h1" else "left"'
    }
    if markdownPatcher.justification == options[args.justify]:
        console.print(f'rich.markdown already uses "{args.justify}" to '
                      'justify "H2" and greater headings.')
        return
    if args.justify == 'center':
        markdownPatcher.apply_patch(options['left'], options['center'])
    elif args.justify == 'left':
        markdownPatcher.apply_patch(options['center'], options['left'])


def main():
    '''Main loop.'''
    global markdownPatcher   # pylint: disable = global-statement

    parser = ArgumentParser(
        description=('Apply or undo a patch to the markdown module in Rich. '
                     'The patch causes all headings except "H1" to be '
                     'rendered left-aligned instead of centered.')
    )
    parser.add_argument('-j', '--justify',
                        choices=['center', 'left'],
                        default=None,
                        type=str,
                        help=('which justification to use for headings "H2" '
                              'and up'),
    )   # noqa: E124

    markdownPatcher = MarkdownPatcher()
    markdownPatcher.ingest_code()

    parser.set_defaults(func=on_justify)
    args = parser.parse_args()

    if not args.justify:
        if not markdownPatcher.justification:
            console.print(PATCH_IS_INCOMPATIBLE_WITH_RICH_MSG)
            return
        console.print("The justification method for \"H2\" and above headings "
                     f"is currently set to '{markdownPatcher.justification}'.")   # noqa: E128
        return

    args.func(args)


if __name__ == "__main__":
    main()
