# {{ cookiecutter.extension_display_name }}

{{ cookiecutter.extension_description }}

## What it does

(tbd)

## License

{% if cookiecutter.extension_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.extension_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
