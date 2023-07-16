import os
import shutil
import subprocess

shutil.rmtree('licenses')

{%- if cookiecutter.contribute_language == "n" %}
shutil.rmtree('extension/examples')
os.remove('extension/share/{{ cookiecutter.first_language_slug }}.tmLanguage.json')
os.remove('extension/share/language-configuration.json')
{%- endif %}

{%- if cookiecutter.dedicated_library_workspace == "n" %}
shutil.rmtree('./{{ cookiecutter.extension_slug }}')
{%- endif %}

git_commands = [
    'git init -q',
    'git add .',
    {%- if cookiecutter.contribute_language == "y" %}
    'git reset -q extension/examples extension/share/*.json',
    'git add -N extension/examples extension/share/*.json',
    {%- endif %}
    'git reset -q extension/README.md',
    'git add -N extension/README.md',
    {%- if cookiecutter.dedicated_library_workspace == "y" %}
    'git reset -q {{ cookiecutter.extension_slug }}/src {{ cookiecutter.extension_slug }}/test',
    'git add -N {{ cookiecutter.extension_slug }}/src {{ cookiecutter.extension_slug }}/test',
    {%- endif %}
]

for git_command in git_commands:
    subprocess.run(git_command, check=True, shell=True)

{%- if cookiecutter.install_dependencies_now == "y" %}
def print_formatted(message: str) -> None:
    width = max((len(line) for line in message))
    print('', width * '-', *message, width * '-', sep='\n')

install_commands = [
    'yarn set version stable',
    'yarn plugin import https://mskelton.dev/yarn-outdated/v3',
    'yarn install',
    'yarn clean-install',
    'git add .yarn .yarnrc.yml package.json yarn.lock',
]

try:
    for install_command in install_commands:
        subprocess.run(install_command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print_formatted([
        f'Shell command failed with exit code {e.returncode}.',
        'Go to the {{ cookiecutter.project_slug }}'
            ' directory and re-run:',
        *[
            f'    {command}'
            for command in ['nvm use'] + install_commands
        ],
    ])
{%- endif %}
