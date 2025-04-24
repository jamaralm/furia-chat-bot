import os 
import importlib
from pathlib import Path

def register_handlers(app):
    command_path = Path(__file__).parent / 'commands'

    for file in os.listdir(command_path):
        if file.endswith('.py') and not file.startswith('__'):
            module_name = file[:-3]
            module_path = f"app.handlers.commands.{module_name}"
            module = importlib.import_module(module_path)

            if hasattr(module, 'get_handler'):
                app.add_handler(module.get_handler())