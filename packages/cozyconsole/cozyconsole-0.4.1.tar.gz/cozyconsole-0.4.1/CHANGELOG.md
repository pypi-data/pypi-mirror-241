# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Version numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## 0.4.1 - 2023-10-18

### Added

- Support for Python 3.12.

## 0.4.0 - 2023-05-03

### Added

- Experimental support for Python 3.12 (3.12.0a7).

### Changed

- Tested against Rich v12.0.0. Previously, Rich v13.0.0 or later was required.

## 0.3.0 - 2023-04-16

### Added

- Ubuntu and Windows (Git Bash) are now supported. (Only MacOS was supported
  prior to this version.)

### Removed

- Removed support for Python 3.7
- Removed `pprintenv` again. It did not belong here and was moved into
  pybrownies.

## 0.2.0 - 2023-03-11

### Added

- `pprintenv` outputs the shell environment as a table which is optimized for human reading.

### Removed

- The ConsoleX instance `console` was deleted from consolex.py. It is
  recommended that packages which use ConsoleX create a console.py module for the sole purpose of creation a `console` instance for the whole package.


## 0.1.0 - 2023-02-25

The code in this version was repackaged from another, private repository. It has been used in other packages by this developer since Mar 13 2022.

### Added

- The `ConsoleX` class extends `rich.console.Console` with methods to write console markup into a string, and to strip console markup from a string; handy during unit testing. It also has error() and warning() methods to avoid having to hardcode error and warning colors in every such message.
- The `Activity` class uses minimal code to provide feedback on what a program is doing at the moment, when it is finished doing that, and whether it resulted in success or failure.
