import logging
import os
from pathlib import Path, PurePath
import shutil
import subprocess
import sys

from cookiecutter.config import get_user_config

logger = logging.getLogger(__name__)

logger.info('Saving replay file for redport')
config_dict = get_user_config()
template_name = '{{ cookiecutter._repo_dir.split('/')[-1] }}'
target_replay_path = Path('.redport') / 'cookiecutter_replay'
target_replay_path.mkdir(exist_ok=True)
shutil.copy(
    (PurePath(config_dict['replay_dir']) / template_name).with_suffix('.json'),
    target_replay_path,
)

shutil.rmtree('licenses')

{%- if cookiecutter.contribute_language == "n" %}
shutil.rmtree('extension/examples')
os.remove('extension/share/language/{{ cookiecutter.first_language_slug }}.tmLanguage.json')
os.remove('extension/share/language/language-configuration.json')
{%- endif %}

{%- if cookiecutter.dedicated_library_workspace == "n" %}
shutil.rmtree('./{{ cookiecutter.extension_slug }}')
{%- endif %}

git_commands = [
    'git init -q',
    'git add .',
    {%- if cookiecutter.contribute_language == "y" %}
    'git reset -q extension/examples extension/share/language',
    'git add -N extension/examples extension/share/language',
    {%- endif %}
    'git reset -q extension/README.md',
    'git add -N extension/README.md',
    {%- if cookiecutter.dedicated_library_workspace == "y" %}
    'git reset -q {{ cookiecutter.extension_slug }}/src {{ cookiecutter.extension_slug }}/test',
    'git add -N {{ cookiecutter.extension_slug }}/src {{ cookiecutter.extension_slug }}/test',
    {%- endif %}
]

for git_command in git_commands:
    subprocess.run(
        git_command, check=True, shell=True, stdout=sys.stderr,
    )

{%- if cookiecutter.install_dependencies_now == "y" %}
def sysexit_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-',
        file=sys.stderr, sep='\n')
    sys.exit()

install_commands = [
    'yarn init -2',
    'git checkout package.json',
    'yarn set version 4',
    'yarn plugin import https://go.mskelton.dev/yarn-outdated/v4',
    'yarn install',
    'yarn clean-install',
    'git add .yarn .yarnrc.yml package.json yarn.lock',
]

try:
    for install_command in install_commands:
        subprocess.run(
            install_command, check=True, shell=True, stdout=sys.stderr,
        )
except subprocess.CalledProcessError as e:
    sysexit_formatted([
        f'Shell command failed with exit code {e.returncode}.',
        'Go to the {{ cookiecutter.project_slug }}'
            ' directory and re-run:',
        *[
            f'    {command}'
            for command in ['nvm use'] + install_commands
        ],
    ])
{%- endif %}
