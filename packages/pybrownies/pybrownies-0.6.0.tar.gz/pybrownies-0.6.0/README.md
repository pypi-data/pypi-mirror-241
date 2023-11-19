# pybrownies

This is a small library of utilities designed to assist in the creation and maintenance of Python projects. `brownie` performs chores like testing, linting, building, publishing. `pprintenv` shows the shell environment like printenv, but prettier. `whichpy` locates Python packages and modules (like `which` locates program files).


## Installation

A lean install installs just `pprint`, `pprintenv`, and `whichpy`:

```sh
% pip install pybrownies
```

To also get the `brownie` tool and its dependencies to help developing your project, enter

```sh
% pip install pybrownies"[dev]"
```

## Usage

### brownie

To see which `brownie` tasks are available, enter

```sh
% brownie --list
Subcommands:

  clean       Remove non-code from the project.
  covreport   Show the coverage report in the default browser.
  dist        Create the sdist and wheel for the project.
  lint        Runs pylint and flake8 on every Python package within this
              project.
  publish     Publishes the project on TestPyPI, or on PyPI with the --pypi
              option.
  test        Runs all unit tests, optionally with test coverage.
%
```

To obtain more info on what a specific task does, enter e.g.

```bash
% brownie publish -h
Usage: brownie [--core-opts] publish [--options] [other tasks here ...]

Docstring:
  Publishes the project on TestPyPI, or on PyPI with the --pypi option.

Options:
  -p, --pypi   publish on pypi.org instead of test.pypi.org
  -s, --show   show the new page in the web browser
%
```

### pprint

Renders various text file formats to the console. with syntax highlighting. Improves the readability os tructured data such as HTML, JSON, PLIST, XML. Applies syntax highlighting to source code. Displays Markdown files with styles and colors appied.

### pprintenv

Outputs the environment as a table, environment variable names in one column, their values in another. For better readability, the elements of a path list (e.g. PATH) are displayed in individual lines.

### whichpy

To locate modules and packages with `whichpy`, enter e.g.

Modules:

```bash
% whichpy shutil
/home/you/.asdf/installs/python/3.10.10/lib/python3.10/shutil.py
```

Packages:

```bash
% whichpy rich
/home/you/dev/pybrownies/.venv3.10/lib/python3.10/site-packages/rich/__init__.py
```

Modules within packages:

```bash
% whichpy rich.console
/home/you/dev/pybrownies/.venv3.10/lib/python3.10/site-packages/rich/console.py
```

## Credits

`brownie` is basically an [invoke](https://pypi.org/project/invoke/) task library. The colorful output is courtesy of [Rich](https://pypi.org/project/rich/).
