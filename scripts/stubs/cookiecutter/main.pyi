# pylint: disable=missing-function-docstring, missing-module-docstring, too-many-arguments, unused-argument

from typing import Dict, Optional, Union
from typing_extensions import Literal, LiteralString

def cookiecutter(
    template: str,
    checkout: Optional[str] = None,
    no_input: bool = False,
    extra_context: Optional[Dict[str, str]] = None,
    replay: Optional[bool] = None,
    overwrite_if_exists: bool = False,
    output_dir: str = ".",
    config_file: Optional[str] = None,
    default_config: bool = False,
    password: Optional[str] = None,
    directory: Optional[str] = None,
    skip_if_file_exists: bool = False,
    accept_hooks: bool = True,
) -> Union[bytes, LiteralString, Literal["."]]: ...
