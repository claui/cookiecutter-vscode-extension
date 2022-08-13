import shutil
import subprocess

shutil.rmtree('licenses')

{%- if cookiecutter.install_dependencies_now == "y" %}
def print_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-', sep='\n')

commands = [
    'yarn set version {{ cookiecutter.yarn_version }}',
    'yarn install',
]

try:
    for command in commands:
        subprocess.run(command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print_formatted([
        f'Yarn failed with exit code {e.returncode}.',
        'Go to the {{ cookiecutter.project_slug }}'
            ' directory and re-run:',
        *[
            f'    {command}'
            for command in ['nvm use'] + commands
        ],
    ])
{%- endif %}
