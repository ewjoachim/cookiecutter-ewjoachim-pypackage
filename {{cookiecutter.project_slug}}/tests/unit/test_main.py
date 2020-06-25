import pytest

from {{ cookiecutter.package_name }} import __main__


@pytest.mark.parametrize("name, called", [("something", False), ("__main__", True)])
def test_main(mocker, name, called):
    cli = mocker.patch("{{ cookiecutter.package_name }}.cli.cli")
    __main__.main(name)
    assert cli.called is called
