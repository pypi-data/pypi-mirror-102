# MkDocs static i18n plugin

![mkdocs-static-i18n pypi version](https://img.shields.io/pypi/v/mkdocs-static-i18n.svg)

*An MkDocs plugin that helps you support multiple language versions of your site / documentation.*

The `mkdocs-static-i18n` plugin allows you to support multiple languages of your documentation by adding static translation files to your existing documentation pages.

Multi language support is just **one `.<language>.md` file away**!

If you want to see how it looks, [check out the demo documentation here](https://ultrabug.github.io/mkdocs-static-i18n/).

*Like what you :eyes:? Give it a :star:!*

## Language detection logic

This plugin is made to be as simple as possible and will generate a default version of your website + one per configured language on the `<language>/` path.

- the `default` version will use any `.md` documentation file first and fallback to any `.<default_language>.md` file found
- the `/<language>` language versions will use any `.<language>.md` documentation file first and fallback to any `.<default_language>.md` file before fallbacking to any default `.md` file found

Since demonstrations are better than words, [check out the demo documentation here](https://ultrabug.github.io/mkdocs-static-i18n/) which showcases the logic.

## Installation

Just `pip install mkdocs-static-i18n`!

## Configuration

Supported parameters:

- **default_language** (mandatory): [ISO-639-1](https://en.wikipedia.org/wiki/ISO_639-1) (2-letter) string
- **languages** (mandatory): mapping of **ISO-639-1 (2-letter) language code**: **display value**
- **material_alternate** (default: true): boolean - [see this section for more info](#using-mkdocs-material-site-language-selector)

```
plugins:
  - i18n:
      default_language: en
      languages:
        en: English
        fr: Français
```

## Example output

Using the configuration above on the following `docs/` structure will build the following `site/` (leaving out static files for readability):

```
docs
├── index.fr.md
├── index.md
├── topic1
│   ├── index.en.md
│   └── index.fr.md
└── topic2
    ├── index.en.md
    └── index.md
```

```
site
├── en
│   ├── index.html
│   ├── topic1
│   │   └── index.html
│   └── topic2
│       └── index.html
├── fr
│   ├── index.html
│   ├── topic1
│   │   └── index.html
│   └── topic2
│       └── index.html
├── index.html
├── topic1
│   └── index.html
└── topic2
    └── index.html
```

### Not building a dedicated version for the default language

If you do not wish to build a dedicated `<language>/` path for the `default_language` version of your documentation, **simply do not list it on the `languages`** list. See issue #5 for more information.

The following configuration:

```
plugins:
  - i18n:
      default_language: en
      languages:
        fr: Français
```

Applied on the following structure:

```
docs
├── index.fr.md
├── index.md
├── topic1
│   ├── index.en.md
│   └── index.fr.md
└── topic2
    ├── index.en.md
    └── index.md
```

Will build:

```
site
├── fr
│   ├── index.html
│   ├── topic1
│   │   └── index.html
│   └── topic2
│       └── index.html
├── index.html
├── topic1
│   └── index.html
└── topic2
    └── index.html
```

## Compatibility with other plugins

This plugin is compatible with the following mkdocs plugins:

- [MkDocs Material](https://github.com/squidfunk/mkdocs-material): the `search` plugin text will be switched automatically to the right language depending on the version you're browsing and the `language selector` will automatically be setup for you (requires mkdocs-material>=7.1.0)
- [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin): the page ordering is preserved on the language specific versions of your site

## Adding a language selector on your documentation header

### Using mkdocs-material site language selector

Starting version 7.1.0, [mkdocs-material supports a site language selector](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/#site-language-selector) configuration.

The `mkdocs-static-i18n` plugin will detect if you're using `mkdocs-material` and, if its version is at least `7.1.0`, **will enable and configure the site language selector automatically for you** unless you specified your own `extra.alternate` configuration!

If you wish to disable that feature, simply set the `material_alternate` option to `false`:

```
plugins:
  - i18n:
      default_language: en
      languages:
        en: English
        fr: Français
      material_alternate: false
```


### Writing a custom language switcher

Let's take `mkdocs-material` as an example and say we would like to add two buttons to allow our visitors to switch to their preferred language.

The following explanation is showcased in the demo website and you can find the files in this very repository:

- [mkdocs.yml](https://github.com/ultrabug/mkdocs-static-i18n/tree/main/mkdocs.yml)
- [theme_overrides](https://github.com/ultrabug/mkdocs-static-i18n/tree/main/theme_overrides)

We need to add a `custom_dir` to our `theme` configuration:

```
theme:
  name: material
  custom_dir: theme_overrides
```

Then override the `header.html` to insert something like:

```
    {% if "i18n" in config.plugins %}
      <div style="margin-left: 10px; margin-right: 10px;">
          {% include "partials/i18n_languages.html" %}
      </div>
    {% endif %}
```

And add a `i18n_languages.html` that could look like this:

```
{% for lang, display in config.plugins.i18n.config.languages.items() -%}
    <div style="display: inline-block; margin-right:5px;"><a href="/{{ lang }}/">{{ display }}</a></div>
{% endfor %}
```

The resulting files should be placed like this:

```
theme_overrides
└── partials
    ├── header.html
    └── i18n_languages.html
```

## See it in action!

- [On this repository demo website](https://ultrabug.github.io/mkdocs-static-i18n/)
- [On my own website: ultrabug.fr](https://ultrabug.fr)

## Contributions welcome!

Feel free to ask questions, enhancements and to contribute to this project!
