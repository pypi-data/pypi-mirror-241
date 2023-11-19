# cozyconsole

## Caveat

This package exists to support my other projects. Those may require breaking changes in here. Consequently, cozyconsole may never become "stable", never reach v1.0.0. Considering how little is in here at the moment, it is probably not worth your time.

## If you are still reading

cozyconsole currently contains:

`cozyconsole.consolex.ConsoleX` is a trivial wrapper around  `rich.console.Console`. It exists to avoid code duplication anti-patterns in my other projects.

`cozyconsole.activity.Activity` is a context manager for operations that run for a few seconds each. It displays a message while a piece of code is executing. When the execution is complete, its status is shown.

```python
from time import sleep
from cozyconsole.activity import Activity
with Activity("Updating dependencies") as act:
   sleep(3)   # simulating the actual code
   act.success = True
```

This displays

```sh
Collecting dependencies...
```

until the code finishes (here: 3 seconds), then updates that to show

```sh
Collecting dependencies - done
```

Activity can handle warnings, errors, and expections in various ways. Run

```bash
% python3 -m cozyconsole.demo
```

to see more.

## Ideas for v0.5.0 and beyond

- Evaluate if Activity should use `rich.status`.
- Activity and ConsoleX error and warning colors should be configurable via a TOML config file.
- A Rich-based horizontal barchart "widget".

## Credits

[Rich](https://pypi.org/project/rich/)
