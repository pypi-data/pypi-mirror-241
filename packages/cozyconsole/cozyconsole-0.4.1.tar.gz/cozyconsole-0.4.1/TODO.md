# To-do list

## Features

- Make certain colors and strings configurable. For instance, in
  `~/.config/cozyconsole.toml`:

   ```toml
   [cozyconsole.activity.colors]
   error   = "bright_red"
   success = "green"
   warning = "gold3"

   [cozyconsole.activity.status-defaults]
   error = "failed"
   success = "done"

   [cozyconsole.consolex.colors]
   error   = "bright_red"
   info    = "default"
   warning = "gold3"
   ```

- New util to render the output of pip freeze in a rich table as a preview.
  Options to update pyproject.toml.

- New utility for showing

   ```python
   >>> import rich.color
   >>> rich.color.ANSI_COLOR_NAMES
   ```

   in a table.


## Software quality

- Explore if handle_exceptions should accept a list of selected exceptions
  instead of a bool.


## Ideas that don't belong here

- Would a tool to help with asdf be useful?
