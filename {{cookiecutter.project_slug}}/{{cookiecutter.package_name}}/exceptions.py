# TODO

class {{ cookiecutter.top_level_exception_class }}(Exception):
    """
    Unexpected {{ cookiecutter.project_name }} error.
    """

    def __init__(self, message=None):
        if not message:
            message = self.__doc__
        super().__init__(message)
