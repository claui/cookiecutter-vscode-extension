"""Local extension with custom functions."""

from jinja2 import Environment
from jinja2.ext import Extension

from . import git


class CustomGlobalsExtension(Extension):  # pylint: disable=abstract-method
    """Custom additions to Jinja’s globals space."""

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        environment.globals["template_git_commit"] = git.commit_hash()

        environment.globals["template_git_remote_url"] = \
            git.current_remote_url()
