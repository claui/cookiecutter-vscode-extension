import shutil
import subprocess

shutil.rmtree('licenses')

{%- if cookiecutter.install_dependencies_now == "y" %}
commands = [
    'yarn set version {{ cookiecutter.yarn_version }}',
    'yarn install',
]
try:
    for command in commands:
        subprocess.run(command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(
        f'Yarn failed with exit code {e.returncode}.',
        'Fix any issues, then go to the '
        '{{ cookiecutter.project_slug }} directory and re-run:',
        *[
            f'    {command}'
            for command in ['nvm use'] + commands
        ],
        sep='\n',
    )
{%- endif %}
