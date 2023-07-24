#!/usr/bin/env node

import esbuild from 'esbuild'
import copyStaticFiles from 'esbuild-copy-static-files'

await esbuild.build({
  entryPoints: ['work/tsc-out/extension.js'],
  bundle: true,
  external: ['vscode'],
  platform: 'node',
  outdir: 'build/',
  plugins: [
    copyStaticFiles({
      src: 'share/dist/',
      dest: 'build/',
    }),
    {%- if cookiecutter.contribute_language == "y" %}
    copyStaticFiles({
      src: 'share/language/',
      dest: 'build/language/',
    }),
    {%- endif %}
    copyStaticFiles({
      src: 'LICENSE.txt',
      dest: 'build/LICENSE.txt',
    }),
    copyStaticFiles({
      src: 'README.md',
      dest: 'build/README.md',
    }),
  ],
})
