from izi18n import _, init_translation, translate, set_locale, get_i18n, get_locale, load_po_file, gettext

init_translation(language="en", translations_path="../exemples/locales")

print(translate("page.facture.title"))
set_locale("fr_FR")
print(translate("page.facture.title"))

# Get ui18n Object class
print(get_i18n().language, " OR ", get_locale(), "\n")
print(get_i18n().translate("cinego"))

print(translate("page.facture.count", default_text="Total facture", **dict(item=5, total=20)))
# Translate with space key
print(translate("space key"))
print(translate("space key 2.Good for me"), "\n")

# load_po_file("app.po", "de")
# load_po_file("messages.po", "de")
load_po_file(['app.po', 'messages.po'], "de", stream=True)

print("-" * 50)
print("Current local:", get_locale(), "\n")
print(translate("Dimanche"))
print(gettext("Lundi"))
print(_("Enter a comma separated list of user names."))
print(_("Visit ${url}", url="https://github.com/cnfilms/izi18n"))
print("-" * 50)

print(translate("blabla"))
