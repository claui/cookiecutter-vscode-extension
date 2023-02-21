import {
  ExtensionContext,
{%- if cookiecutter.contribute_language == "y" %}
  LanguageStatusItem,
{%- endif %}
  commands,
{%- if cookiecutter.contribute_language == "y" %}
  languages,
{%- endif %}
  window,
{%- if cookiecutter.contribute_language == "y" %}
  DocumentSelector,
{%- endif %}
} from "vscode";

import Logger from "./logger";

import { getCurrentTimestamp } from "./time";

const outputChannel = window.createOutputChannel("{{ cookiecutter.extension_display_name }}");

{%- if cookiecutter.contribute_language == "y" %}
const languageSelector: DocumentSelector = { language: "{{ cookiecutter.first_language_slug }}" };
{%- endif %}

const log: Logger = {
  debug: function (...args) {
    this.log("DEBUG", ...args);
  },
  error: function (...args) {
    this.log("ERROR", ...args);
  },
  info: function (...args) {
    this.log("INFO", ...args);
  },
  log: function (level: string, ...args: unknown[]) {
    const timestamp = getCurrentTimestamp();
    outputChannel.appendLine(`${timestamp} [${level}] ${args.join(" ")}`);
  },
};

{% if cookiecutter.contribute_language == "y" -%}
const statusItem: LanguageStatusItem = languages.createLanguageStatusItem(
  "{{ cookiecutter.first_language_slug }}.status.item",
  languageSelector
);
{%- endif %}

export function activate(context: ExtensionContext) {
  commands.registerCommand("{{ cookiecutter.extension_slug }}.action.showLog", () => {
    outputChannel.show();
  });
{%- if cookiecutter.contribute_language == "y" %}
  statusItem.command = {
    command: "{{ cookiecutter.extension_slug }}.action.showLog",
    title: "Show extension log",
  };
{%- endif %}

  return {};
}

export function deactivate() {
  return undefined;
}
