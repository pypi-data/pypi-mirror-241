# TODOs

## Features

- Read configuration from pyproject.toml.
- Respect the [tool.coverage.html] setting.
- Add a task which performs pre-flight checks prior to publishing or
  tagging, such as
  - Check the __version__ in the packages __init__.py.
  - Check if it's the same as the newest verion in CHANGELOG.md.
  - Check if the most recent commit is tagged with that version number, too.
  - Check the Development Status classifier in pyproject.toml.
  - Check the Trove classifiers against the `trove-classifiers` package.
- `bro publish` aborts if the package version is x.y.z - remember, once
  uploaded to Test PyPI, the version number is burned and cannot be used again. Therefore, ensure version numbers such as x.y.za1 or x.y.z.dev1.
- `bro publish --pypi` aborts if the package version is _not_ x.y.z.
- Add a [tool.pybrownies] table to pyproject.toml. Allow to customize some
  settings.
- If the project has a tasks.py or tasks/__init__.py in the project, allow to
  integrate it.
- Long term: consider supporting alternative build backend, linters other than
  pylint and flake8. Also extra CLI options (like pytest "addopts") for tools.
- Add an init task which installs required dependencies accordingly.
