"""Local extension with custom functions."""

from uuid import uuid4

from jinja2 import Environment
from jinja2.ext import Extension


class CustomFunctionsExtension(Extension):  # pylint: disable=abstract-method
    """Custom additions to Jinja’s global-function space."""

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        # Generate UUIDs in Jinja
        environment.globals["uuidgen"] = uuid4
