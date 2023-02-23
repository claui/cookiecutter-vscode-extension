import { window } from "vscode";

export default window.createOutputChannel("{{ cookiecutter.extension_display_name }}", { log: true });
