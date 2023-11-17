from izi18n import init_translation, add_translation, add_translation_by_lang

init_translation(language="fr", translations_path="../exemples/locales")

add_translation(pattern="page.home.title", value="Bonjour")
# Use if initial language is not defined
add_translation_by_lang(lang="en", pattern="page.home.title", value="Hi!")
add_translation(pattern="page.home.docs", value="Documents", lang="en")
