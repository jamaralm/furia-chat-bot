import os 
import importlib
from pathlib import Path

def register_handlers(app):
    base_path = Path(__file__).parent
    handle_dirs = ['commands', 'callbacks']

    for dir_name in handle_dirs:
        full_path = base_path / dir_name
        for file in os.listdir(full_path):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                module_path = f"app.handlers.{dir_name}.{module_name}"  # corrigido aqui
                module = importlib.import_module(module_path)

                if hasattr(module, 'get_handler'):
                    app.add_handler(module.get_handler())