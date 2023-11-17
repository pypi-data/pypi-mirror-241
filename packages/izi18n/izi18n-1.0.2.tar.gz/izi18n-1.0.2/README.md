# izi18n [![Downloads](https://static.pepy.tech/personalized-badge/izi18n?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/izi18n)
`Simple python library for language Internationalisation`

# Install 
```shell
pip install izi18n
```

* Support
    * `JSON`
    * `.PO FILES`

# Method
* `_`
* `add_translation`
* `add_translation_by_lang`
* `get_i18n`
* `get_locale`
* `gettext`
* `init_translation`
* `load_po_file`
* `set_locale`
* `set_translations_path`
* `translate`
* `translate_by_lang`

# Usage
* `Initialisation`
```python
from izi18n import init_translation

# Set default language
# Translations_path is where locate all language translations file (JSON file only)
init_translation(language="en", translations_path="../exemples/locales")
```

* `Translate`
```python
from izi18n import translate, gettext, _

# page.facture.title is the pattern to the key you want to translate
print(translate('page.facture.title'))

# Translate template with values
# default_text is set if the pattern is not found
# **dict() is the kwargs
translate("page.facture.count", default_text="Total facture", **dict(item=5, total=20))
# OR
translate("page.facture.count", default_text="Total facture", item=5, total=20)

# Possibility to use gettext or _() instead from translate
print(gettext('page.facture.title'))
print(_('page.facture.title'))
```
* `Translate by Key or Word`
```python
from izi18n import translate

# Translate with word key
print(translate("space key"))
translate("cinego")
print(translate("space key 2.Good for me"))
```

* `Get I18n class object`
```python
from izi18n import get_i18n, get_locale

# Get ui18n Object class
# get_i18n return I18n class (Singleton)
print(get_i18n().language, " OR ", get_locale(), "\n")
print(get_i18n().translate("cinego"))
```

* `Load translation from .PO file`
```python
from izi18n import load_po_file, get_locale, gettext, translate, _

# Load po files and specify the local of the files
# Stream True it means you avoid to merged with json locales folder files
load_po_file(['app.po', 'messages.po'], "de", stream=True)
# load_po_file("cinego.po", "de")
# load_po_file("messages.po", "de")

print(get_locale())

print(translate("Dimanche"))
print(gettext("Lundi"))
print(_("Visit ${url}", url="https://github.com/cnfilms/izi18n"))
```

* `Add or edit translation`
```python
from izi18n import init_translation, add_translation, add_translation_by_lang

init_translation(language="fr", translations_path="../exemples/locales")

# Add to current local
add_translation(pattern="page.home.title", value="Bonjour")

# Use if initial language is not defined
add_translation_by_lang(lang="en", pattern="page.home.title", value="Hi!")
add_translation(pattern="page.home.docs", value="Documents", lang="en")
```