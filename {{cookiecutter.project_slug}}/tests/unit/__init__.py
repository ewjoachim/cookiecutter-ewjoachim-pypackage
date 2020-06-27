from {{ cookiecutter.package_name }} import exceptions

def test_base_exception():
    class TestException(exceptions.{{ cookiecutter.top_level_exception_class }}):
        """Foo"""

    assert str(TestException) == "Foo"
