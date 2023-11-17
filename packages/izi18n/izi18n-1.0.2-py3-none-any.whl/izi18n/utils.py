import json
import os.path


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


def extract_language(language):
    if language:
        return language[:2].lower() if len(language) > 3 else language.lower()
    return language


def parse_po_file(po_filename):
    with open(po_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translations = []
    current_msgid = None
    current_msgstr = None

    for line in lines:
        line = line.strip()

        if line.startswith('#'):
            continue  # Skip comment lines

        if line.startswith('msgid'):
            current_msgid = line[len('msgid '):].strip('"')
        elif line.startswith('msgstr'):
            current_msgstr = line[len('msgstr '):].strip('"')

            # Add the msgid and msgstr to the list
            if current_msgid and current_msgstr:
                translations.append((current_msgid, current_msgstr))

            # Reset the values for the next entry
            current_msgid = None
            current_msgstr = None

    return translations


def po_to_json(po_filename, save=False, json_filename=None):
    # Load the .po file
    po = parse_po_file(po_filename)

    # Create an empty dictionary to store translations
    translations = {}

    # Extract translations from the .po file and store them in the dictionary
    for msgid, msgstr in po:
        if msgid and msgstr:
            translations[msgid] = msgstr

    if save:
        # Convert the dictionary to JSON and save it to a .json file
        create_file(json_filename)
        with open(json_filename, 'w') as json_file:
            json.dump(translations, json_file, ensure_ascii=False, indent=2)

    return translations


def are_dicts_equal(dict1, dict2):
    return dict1 == dict2


def create_file(file_path):
    if not os.path.exists(file_path):
        f = open(file_path, "x")
        f.close()


def create_directory_if_not_exist(directory_path):
    try:
        os.makedirs(directory_path)
    except OSError:
        print("")
