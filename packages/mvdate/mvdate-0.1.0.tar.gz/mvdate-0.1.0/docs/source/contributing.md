## Contributing

Pull requests correcting errors or expanding options are welcome. To contribute you should fork this repository to your
account and clone locally and make your changes before creating a Merge Request. You should then install the package in
editable mode with all optional dependencies. It is recommended that you use a Python Virtual Environment (my preference
for working with these is [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) but other
options abound such as [Conda](https://docs.conda.io/en/latest/), the choice is yours).

``` bash
mkvirtualenv mvdate
workon mvdate
cd path/to/cloned/mvdate
pip install -e .[dev,docs,tests]
```

### `pre-commit` and linting

This package is developed using various [linting](https://ns-rse.github.io/posts/linting/) tools which are applied
before each commit is made using the amazing [pre-commit](https://pre-commit.com). Various pre-commit hooks are
implemented and configured via the `.pre-commit-config.yaml`.

+ [pre-commit-hook](https://github.com/pre-commit/pre-commit-hooks) checks various aspects of Python, Yaml and Markdown
  files.
+ [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) lints Markdown files.
+ [Black](https://github.com/psf/black) the opinionated Python formatter.
+ [ruff](https://github.com/astral-sh/ruff) the blazing fast Python linter.
+ [mypy](https://github.com/python/mypy) for typehints checking.
+ [Pylint](https://github.com/pylint-dev/pylint) for even more Python linting.

`pre-commit` and linting are enabled in the GitLab CI pipelines. To ensure your pull request passes these you should
install and enable `pre-commit`. If you followed the steps above `pre-commit` should be installed in your Virtual
Environment. Install it with...

``` bash
pre-commit install
```

Now whenever you make a commit `pre-commit` will run and check the contributions. In some instances the hooks can
automatically fix errors, but you may find you have to correct some yourself. The output is generally informative
directing you to the relevant line and what the error is.
