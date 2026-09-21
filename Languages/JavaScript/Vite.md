https://vite.dev

A front-end build tool / bundler. Designed for speed and instant feedback. It does this by not bundling application code during development.

Can be extended via plugins.

[[#Overview]]
[[#Commands]]

---
## Overview 

Development
- Serves source files directly as native ES modules.
- The browser only loads what it needs.
- Converts code into [[JavaScript]] as it is needed.

Production
- Bundles your source code together.
- Outputs optimized static assets in a `dist/` folder ready for deployment.
- Uses Rollup by default to bundle and optimize the application for production.

Hot Module Replacement
- Serves code locally during development.
- Modified source code is shown instantly, no need for a full page reload.
- Updates only the affected modules, preserving application state where possible.

---
## Commands

Using [[NPM]]

Install as a development dependency (`-D` is shorthand for `--save-dev`)

```
npm install -D vite
```

To use

```
npx vite
```

---