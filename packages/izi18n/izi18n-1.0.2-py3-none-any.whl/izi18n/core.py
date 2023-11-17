from izi18n.i18n import I18n

_i18n = I18n()


def get_i18n():
    """
    Returns the `izi18n.i18n` object class
    """
    return _i18n


def init_translation(language, translations_path):
    """
    Init translation language and translation directory
    """
    _i18n.set_translations_path(translations_path)
    _i18n.set_language(language)


def set_translations_path(translations_path):
    """
    Change the translation directory
    """
    _i18n.set_translations_path(translations_path)


def add_translation(pattern, value, lang=None):
    """
    Add new or edit exiting translation
    """
    if lang:
        add_translation_by_lang(lang, pattern, value)
    else:
        _i18n.add_translation(pattern, value)


def add_translation_by_lang(lang, pattern, value):
    """
    Add new or edit exiting translation by specifying the language to avoid call `set_locale`
    """
    _lang = _i18n.language
    _i18n.set_language(lang)
    _i18n.add_translation(pattern, value)
    _i18n.set_language(_lang)


def set_locale(locale):
    """
    Change translation language
    """
    _i18n.set_language(locale)


def get_locale():
    """
    Get current locale language
    """
    return _i18n.language


def translate(*args, **kwargs):
    """
    Translate by pattern or key or text.
    Support default_text if not find and support **kwargs to format translation
    """
    return _i18n.pluralize(*args, **kwargs)


def translate_by_lang(lang, *args, **kwargs):
    """
    Translate by language avoid change the locale language
    """
    _lang = _i18n.language
    _i18n.set_language(lang)
    _text = translate(*args, **kwargs)
    _i18n.set_language(_lang)
    return _text


def load_po_file(po_filenames: any, language, stream=True):
    """
    Load translation from po file
    """
    if isinstance(po_filenames, list):
        for _po_file in po_filenames:
            _i18n.load_translations_from_po_file(_po_file, language, stream)
    if isinstance(po_filenames, str):
        _i18n.load_translations_from_po_file(po_filenames, language, stream)


def _(*args, **kwargs):
    """
    Translate by pattern or key or text.
    Support default_text if not find and support **kwargs to format translation
    """
    return translate(*args, **kwargs)


def gettext(*args, **kwargs):
    """
    Translate by pattern or key or text.
    Support default_text if not find and support **kwargs to format translation
    """
    return translate(*args, **kwargs)
