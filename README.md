# cookiecutter-vscode-extension

This is the source code repository for
`cookiecutter-vscode-extension`, a
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Visual Studio code extensions which focuses on
long-term maintainability and a reliable setup.

## About this document

This is the **user documentation** for the Cookiecutter template.  
If you’re a **contributor**, see: [CONTRIBUTING.md](./CONTRIBUTING.md)  
For **license information,** see the bottom of this document.

## About this template

### Goals

`cookiecutter-vscode-extension` is an opinionated Cookiecutter
template for VS Code extensions with a focus on:

- **long-term maintainability** of the generated project; and

- **reliability** through step-by-step instructions, enabling users
  to build, run, and work on the generated VS Code extensions on
  diverse platforms.

### What you put in

The template allows you to specify:

- display name, slug and short description for the VS Code
  extension;

- a project slug, which will be the name of your project directory
  and repository (and typically has a `vscode-` prefix);

- both an author name and a copyright holder name;

- a project license (Apache 2.0 or proprietary license);

- the minimum major/minor version for the target VS Code engine;

- the language that your extension will contribute to VS Code; and

- your username on the Visual Studio Marketplace, and whether or not
  you’re going to publish your extension there; and

- your GitHub username where the source code repository will live
  (optional).

### What you get out of it

The Cookiecutter template will give you:

- a `package.json` in the project root directory, which declares
  essential development dependencies and useful Yarn scripts;

- an `extension` subdirectory, which is the root of the packaged
  extension;

- the main Typescript module `extension/src/extension.ts`, which
  contains the primary hooks for the extension, `activate` and
  `deactivate`;

- a `time` module, which contains convenience functions;

- an `extension/tsconfig.json` file to configure the TypeScript
  compiler;

- an `extension/.vscodeignore` file, which instructs the extension packager
  to exclude unneeded files;

- an `extension/package.json` file with configuration settings
  meant to be consumed mainly by VS Code;

- a `.gitattributes` file;

- a `.gitignore` file;

- an `.editorconfig` file;

- a `.nvmrc` file to lock the Node.js platform version;

- a `README.md` file in the project root directory, aimed at
  contributors to the extension;

- a user-facing `extension/README.md` file, which will be published
  alongside the packaged extension;

- a `LICENSE` file in the project root directory;

- a user-facing copy of the license at `extension/LICENSE.txt`,
  which will be published alongside the packaged extension; and

- settings for Visual Studio Code integration.

## Using cookiecutter-vscode-extension

### System requirements

To use this Cookiecutter template, you need:

1. A system-wide Python installation.

2. Cookiecutter version 2.1 or newer.

3. The JavaScript version manager `nvm`.

4. The JavaScript package manager `yarn`.

### Checking your system-wide Python installation

Make sure you have Python 3.7 or higher installed on your system
and available in your PATH.

To check, run:

```
python --version
```

If that fails, try:

```
python3 --version
```

Proceed after you’ve confirmed one of those to work.

### Installing Cookiecutter

To install Cookiecutter, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-vscode-extension
```

### Alternative usage

If you use `cookiecutter-vscode-extension` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```
abbreviations:
    vscode: https://github.com/claui/cookiecutter-vscode-extension.git
```

Then, to generate a project, run:

```
cookiecutter vscode
```

### Working on the generated VS Code extension

See the generated `README.md` file.

### Contributing to this Cookiecutter template

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Copyright (c) 2022 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
