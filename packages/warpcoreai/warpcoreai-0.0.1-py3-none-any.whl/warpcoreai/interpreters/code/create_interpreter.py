from .language_map import language_map


def create_code_interpreter(config):
    # Case in-sensitive
    language = config["language"].lower()

    try:
        code_interpreter = language_map[language]
        return code_interpreter(config)
    except KeyError:
        raise ValueError(f"Unknown or unsupported language: {language}")
