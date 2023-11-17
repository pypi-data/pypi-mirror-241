import os
import subprocess
import logging
from yaspin import yaspin
from yaspin.spinners import Spinners

from ..interpreters.code import language_map
from .temporary_file import cleanup_temporary_file, create_temporary_file

def get_language_file_extension(language_name):
    """
    Get the file extension for a given programming language.

    Args:
        language_name (str): The name of the programming language.

    Returns:
        str: File extension associated with the language.
    """
    language = language_map.get(language_name.lower())
    return language.file_extension if language and language.file_extension else None

def get_language_proper_name(language_name):
    """
    Get the proper name for a given programming language.

    Args:
        language_name (str): The name of the programming language.

    Returns:
        str: The proper name of the language.
    """
    language = language_map.get(language_name.lower())
    return language.proper_name if language and language.proper_name else None

def scan_code(code, language, interpreter):
    """
    Scan code with semgrep for a specified programming language.

    Args:
        code (str): The code to be scanned.
        language (str): The programming language of the code.
        interpreter: The interpreters object with configuration settings.

    Returns:
        bool: True if scan was successful, False otherwise.
    """
    temp_file = create_temporary_file(code, get_language_file_extension(language), verbose=interpreter.debug_mode)
    temp_path = os.path.dirname(temp_file)
    file_name = os.path.basename(temp_file)

    if interpreter.debug_mode:
        logging.info(f"Scanning {language} code in {file_name}")

    try:
        command = ["cd", temp_path, "&&", "semgrep", "scan", "--config", "auto", "--quiet", "--error", file_name]
        with yaspin(text="  Scanning code...").green.right.binary as loading:
            scan = subprocess.run(command, shell=False)

        if scan.returncode == 0:
            language_name = get_language_proper_name(language)
            logging.info(f"No issues were found in this {language_name} code.")
        else:
            logging.error(f"Issues found during the scan of {language} code.")
        return scan.returncode == 0
    except Exception as e:
        logging.error(f"Could not scan {language} code: {e}")
        return False
    finally:
        cleanup_temporary_file(temp_file, verbose=interpreter.debug_mode)
