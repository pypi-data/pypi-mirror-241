# utilities/__init__.py

import importlib
import os


class UtilsLoader:
    def __init__(self):
        # Usa un percorso relativo qui
        utils_path = os.path.dirname(__file__)
        for filename in os.listdir(utils_path):
            if filename.endswith('.py') and not filename.startswith(('_', 'utils_loader')):
                module_name = filename[:-3]
                module = importlib.import_module(f'.{module_name}', package='utilities')
                setattr(self, module_name, module)


utils = UtilsLoader()
