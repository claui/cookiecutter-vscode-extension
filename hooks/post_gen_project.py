import shutil
import subprocess

shutil.rmtree('licenses')

{%- if cookiecutter.contribute_language == "n" %}
shutil.rmtree('extension/examples')
shutil.rmtree('extension/share')
{%- endif %}

{%- if cookiecutter.install_dependencies_now == "y" %}
def print_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-', sep='\n')

commands = [
    'yarn set version stable',
    'yarn plugin import https://mskelton.dev/yarn-outdated/v3',
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
