import {
  ExtensionContext,
  LanguageStatusItem,
  commands,
  languages,
  window,
  DocumentSelector,
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
  log: function (level: string, ...args: any[]) {
    const timestamp = getCurrentTimestamp();
    outputChannel.appendLine(`${timestamp} [${level}] ${args.join(" ")}`);
  },
};

{%- if cookiecutter.contribute_language == "y" %}
const statusItem: LanguageStatusItem = languages.createLanguageStatusItem(
  "{{ cookiecutter.first_language_slug }}.status.item",
  languageSelector
);
{%- endif %}

export function activate(context: ExtensionContext) {
  commands.registerCommand("{{ cookiecutter.extension_slug }}.action.showLog", () => {
    outputChannel.show();
  });
  statusItem.command = {
    command: "{{ cookiecutter.extension_slug }}.action.showLog",
    title: "Show extension log",
  };

  return {};
}

export function deactivate() {}
