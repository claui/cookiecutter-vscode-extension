import {
  commands,
{%- if cookiecutter.contribute_language == "y" %}
  DocumentSelector,
{%- endif %}
  ExtensionContext,
{%- if cookiecutter.contribute_language == "y" %}
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

interface ExtensionPackageJson {
  "displayName": string,
  "version": string,
}

function packageJson(context: ExtensionContext): ExtensionPackageJson {
  return context.extension.packageJSON as ExtensionPackageJson;
}

export function activate(context: ExtensionContext) {
  commands.registerCommand("{{ cookiecutter.extension_slug }}.action.showLog", log.show, log);
{%- if cookiecutter.contribute_language == "y" %}
  statusItem.command = {
    command: "{{ cookiecutter.extension_slug }}.action.showLog",
    title: "Show extension log",
  };
{%- endif %}

  const { version } = packageJson(context);
  log.info(`Extension v${version} startup successful`);
  return {};
}

export function deactivate() {
  return;
}
