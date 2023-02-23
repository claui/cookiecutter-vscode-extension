import {
  commands,
{%- if cookiecutter.contribute_language == "y" %}
  DocumentSelector,
  languages,
  LanguageStatusItem,
{%- endif %}
} from "vscode";

import log from "./log";

{%- if cookiecutter.contribute_language == "y" %}
const languageSelector: DocumentSelector = { language: "{{ cookiecutter.first_language_slug }}" };

const statusItem: LanguageStatusItem = languages.createLanguageStatusItem(
  "{{ cookiecutter.first_language_slug }}.status.item",
  languageSelector,
);
{%- endif %}

export function activate() {
  commands.registerCommand("{{ cookiecutter.extension_slug }}.action.showLog", log.show, log);
{%- if cookiecutter.contribute_language == "y" %}
  statusItem.command = {
    command: "{{ cookiecutter.extension_slug }}.action.showLog",
    title: "Show extension log",
  };
{%- endif %}

  log.info("Extension startup successful");
  return {};
}

export function deactivate() {
  return;
}
