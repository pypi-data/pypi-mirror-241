# Learn Python Packaging

[![codecov][codecov-badge-image]][codecov-badge-url]
[![DeepSource][deepsource-badge-image]][deepsource-badge-url]
[![Documentation Status][read-the-docs-badge-image]][read-the-docs-badge-url]

[![code-quality workflow][code-quality-workflow-badge-image]][code-quality-workflow-badge-url]
[![docs workflow][docs-workflow-badge-image]][docs-workflow-badge-url]
[![format workflow][format-workflow-badge-image]][format-workflow-badge-url]
[![lint workflow][lint-workflow-badge-image]][lint-workflow-badge-url]
[![release workflow][release-workflow-badge-image]][release-workflow-badge-url]
[![test workflow][test-workflow-badge-image]][test-workflow-badge-url]

[![pre-commit][pre-commit-badge-image]][pre-commit-badge-url]
[![Ruff][ruff-badge-image]][ruff-badge-url]

[![Code style: black][black-badge-image]][black-badge-url]
[![Docstring formatter: docformatter][docformatter-badge-image]][docformatter-badge-url]
[![Imports: isort][isort-badge-image]][isort-badge-url]

[![security: bandit][bandit-badge-image]][bandit-badge-url]
[![linting: pylint][pylint-badge-image]][pylint-badge-url]

[![Docstring style: numpy][numpydoc-badge-image]][numpydoc-badge-url]

- [x] ~~Create Python Package~~
- [x] ~~Build Wheel~~
- [x] ~~Release Wheel~~
- [x] ~~Setup Github Actions~~
- [x] ~~Host Documentation~~
- [x] ~~Hypotheses Testing~~
- [x] ~~Pydantic Validation~~
- [x] ~~Support Expressions~~
- [ ] Bump Workflow

## Tools Used

- Development
    - [codespell](https://github.com/codespell-project/codespell)
    - [Nox](https://github.com/wntrblm/nox)
    - [pre-commit](https://github.com/pre-commit/pre-commit)
    - [Ruff](https://github.com/astral-sh/ruff)
- Formatting
    - [autoflake](https://www.github.com/PyCQA/autoflake)
    - [Black](https://github.com/psf/black)
    - [blacken-docs](https://github.com/adamchainz/blacken-docs)
    - [docformatter](https://github.com/PyCQA/docformatter)
    - [isort](https://pycqa.github.io/isort/)
    - [pyproject-fmt](https://github.com/tox-dev/pyproject-fmt)
    - [pyupgrade](https://github.com/asottile/pyupgrade)
- Linting
    - [Bandit](https://bandit.readthedocs.io/)
    - [Flake8](https://github.com/pycqa/flake8)
    - [interrogate](https://interrogate.readthedocs.io/)
    - [Mypy](http://www.mypy-lang.org/)
    - [pydocstyle](https://www.pydocstyle.org/en/stable/)
    - [Pylint](https://github.com/PyCQA/pylint)
    - [Pyright for Python](https://github.com/RobertCraigie/pyright-python)
    - [validate-pyproject](https://github.com/abravalheri/validate-pyproject/)
    - [Vulture](https://github.com/jendrikseipp/vulture)
- Testing
    - [Coverage.py](https://github.com/nedbat/coveragepy)
    - [Hypothesis](https://hypothesis.works/)
    - [pytest](https://docs.pytest.org/en/latest/)
- Documentation
    - [Furo](https://github.com/pradyunsg/furo)
    - [Read the Docs](https://readthedocs.org/)
    - [Sphinx](https://www.sphinx-doc.org/)
    - [sphinx-copybutton](https://github.com/executablebooks/sphinx-copybutton)

[bandit-badge-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-badge-url]: https://github.com/PyCQA/bandit

[black-badge-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-badge-url]: https://github.com/psf/black

[code-quality-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/code-quality.yml/badge.svg
[code-quality-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/code-quality.yml/

[codecov-badge-image]: https://codecov.io/gh/yarnabrina/learn-python-packaging/branch/main/graph/badge.svg?token=BG1ECA7E14
[codecov-badge-url]: https://codecov.io/gh/yarnabrina/learn-python-packaging

[docformatter-badge-image]: https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg
[docformatter-badge-url]: https://github.com/PyCQA/docformatter

[deepsource-badge-image]: https://deepsource.io/gh/yarnabrina/learn-python-packaging.svg/?label=active+issues&token=tfsfTm2RCqlPTgF3dN31q-0e
[deepsource-badge-url]: https://deepsource.io/gh/yarnabrina/learn-python-packaging/?ref=repository-badge

[docs-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/docs.yml/badge.svg
[docs-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/docs.yml/

[format-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/format.yml/badge.svg
[format-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/format.yml/

[isort-badge-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-badge-url]: https://pycqa.github.io/isort/

[lint-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/lint.yml/badge.svg
[lint-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/lint.yml/

[numpydoc-badge-image]: https://img.shields.io/badge/%20style-numpy-459db9.svg
[numpydoc-badge-url]: https://numpydoc.readthedocs.io/en/latest/format.html

[pre-commit-badge-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[pre-commit-badge-url]: https://github.com/pre-commit/pre-commit

[pylint-badge-image]: https://img.shields.io/badge/linting-pylint-yellowgreen
[pylint-badge-url]: https://github.com/PyCQA/pylint

[read-the-docs-badge-image]: https://readthedocs.org/projects/learn-python-packaging/badge/?version=latest
[read-the-docs-badge-url]: https://learn-python-packaging.readthedocs.io/en/latest/?badge=latest

[release-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/release.yml/badge.svg
[release-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/release.yml/

[ruff-badge-image]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff-badge-url]: https://github.com/astral-sh/ruff

[test-workflow-badge-image]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/test.yml/badge.svg
[test-workflow-badge-url]: https://github.com/yarnabrina/learn-python-packaging/actions/workflows/test.yml/
