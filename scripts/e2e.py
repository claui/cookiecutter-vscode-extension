"""End-to-end test"""

import subprocess
from tempfile import mkdtemp

from cookiecutter.main import cookiecutter
from .settings import PROJECT_ROOT


def run() -> None:
    """Runs the end-to-end test."""
    target_path_name = cookiecutter(
        str(PROJECT_ROOT),
        no_input=True,
        output_dir=mkdtemp(suffix=".e2e", prefix="cookiecutter."),
        extra_context={
            "extension_display_name": "Flubber",
            "first_language_display_name": "Flubberfile",
            "first_language_filename_pattern": "*.flub",
            "extension_license": "Proprietary",
            "marketplace_publisher_id": "end_to_end_test",
        },
    )
    print(target_path_name)
    subprocess.run("yarn package", check=True, cwd=target_path_name, shell=True)
