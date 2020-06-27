# Python package cookiecutter

My cookiecutter for crafting Python packages with my favorite tooling.
This has been extracted from [procrastinate](https://github.com/peopledoc/procrastinate).

Feel free to steal this and adapt it to your needs.

After generating, look for `TODO` in the code.

Features:
- Code of conduct: [Contributor Covenant](https://www.contributor-covenant.org/)
- Readme with a lot of badges to show you're cool
- GitHub Codeowners
- MIT license
- Pull request template (including contributor feedback)
- [.editorconfig](https://editorconfig.org/)
- requirements.txt that install dependencies for contributors
- setup.cfg-based metadata (minimalist setup.py):
    - classical metadata
    - project urls for nice display in PyPI
    - Classifiers with supported Python versions
    - Long description read from README.rst
    - setuptools-scm as mentionned above
    - dev/tests/docs/doc spell check dependencies as extras
    - Other tools' config is there, when possible: flake8, doc8, mypy, pytest, coverage
    - Coverage ignores classic non-statements.
- Full commitless release:
    - Each time a PR is merged, changelog information based on the PR title is being
      added to the next GitHub Release draft, using
      [release-drafter](https://github.com/release-drafter/release-drafter).
      The next version number is determined by PR labels.
    - When this draft is released, GitHub creates a tag. This tag is seen by
      [Travis](https://travis-ci.org/) who then launches a build with a pypi deploy
      stage.
    - The version of the package doesn't appear in the code. When building the package,
      the version is extracted from the latest tag, using
      [setuptools-scm](https://pypi.org/project/setuptools-scm/)
    - The whole process is documented in CONTRIBUTING.md
- [tox](https://tox.readthedocs.io/en/latest/):
    - Launching Pytest with all supported python versions
    - Formatting:
        - Code looks always the same with [black](https://github.com/psf/black) (&
          [compatible
          config](https://github.com/psf/black/blob/master/docs/compatible_configs.md))
        - Imports are sorted with [isort](https://pypi.org/project/isort/)
    - Linting:
        - Blatant mistakes & PEP8 spotted by
          [flake8](https://flake8.pycqa.org/en/latest/)
        - type annotations checked by [mypy](http://mypy-lang.org/) (with "explicit
          optional", so when you have a callable argument with a default value None,
          you still to explicitly say that it's "Optional")
        - isort
        - black
        - Manifest.in is always correct, thanks to
          [check-manifest](https://pypi.org/project/check-manifest/)
- [Sphinx](https://www.sphinx-doc.org/en/master/) documentation skeleton:
    - Daniele Procida's [4 sections doc](https://documentation.divio.com/)
    - A glossary
    - Reads the main page from README.rst, the contribution page from CONTRIBUTING.rst
    - (soon) Automated changelog using GitHub Releases
    - Default role is any, meaning most inter-links can be achieved with simple
      backtick-enclosed references.
    - optional spell checker, with a dedicated extra-dictionary when you need to invent
      words
    - doc8
    - warnings treated as errors in the build. This saves lives.
    - `.readthedocs.yml`
- Skeleton code:
    - Dunder metadata in the package, read using
      [importlib-metadata](https://pypi.org/project/importlib-metadata/) (for py3.6
      compatibility)
    - cli module using [click](https://click.palletsprojects.com/en/7.x/) (added in
      entrypoints), includes verbosity and version, and expection handling
    - Base exceptions, docstring used as default message
- [Pytest](https://docs.pytest.org/en/latest/):
    - Coverage: [pytest-cov](https://pypi.org/project/pytest-cov/) and
        [CodeCov](https://codecov.io/)
    - Mocking: [pytest-mock](https://pypi.org/project/pytest-mock/)
    - A skeleton for tests with conftest, unit, integration and acceptance tests
    - Initial tests for the skeleton code, to start with 100% coverage already
    - Test can be launched without any arguments (`pytest`). Launch low-level tests
      first. Perfecto for use with `pytest --sw`.

Planned improvements:
- Click is nice, but maybe we can find better. I'd like to evaluate
  [cleo](https://github.com/sdispater/cleo) and put some colors on!
- Switch to poetry ?
- Setup.cfg formatter: [setup-cfg-fmt](https://pypi.org/project/setup-cfg-fmt/)
- [nox](https://nox.thea.codes/en/stable/) instead of
  [tox](https://tox.readthedocs.io/en/latest/)
- Testing this cookiecutter
- Travis to GitHub Actions, maybe
