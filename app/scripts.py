import os
import sys
from typing import Optional


def add_blueprint(blueprint_name: str) -> Optional[str]:
    """Create blueprint folder and starter files with matching name provided"""
    if not blueprint_name.isidentifier():
        return 'Error: Blueprint name specified is not a valid variable name'

    try:
        os.mkdir(f'blueprints/{blueprint_name}')
    except FileExistsError:
        print('Error: Blueprint not created.Directory with matching name found.')
        return None

    # add blueprint to base init file
    with open('blueprints/__init__.py', 'a') as blueprint_init:
        blueprint_init.write(f'from app.blueprints.{blueprint_name} import *\n')

    os.chdir(f'blueprints/{blueprint_name}')

    # Create init file
    # TODO: Validate project structure hasn't changed
    with open('__init__.py', 'w') as init_file:
        init_file.write(f'from app.blueprints.{blueprint_name}.views import {blueprint_name}\n')
        init_file.close()

    # Create templates folder
    os.makedirs(f'templates/{blueprint_name}')

    # Create Blueprint
    with open('views.py', 'w') as views_file:
        lines = ["from flask import Blueprint\n\n",
                 f"{blueprint_name} = Blueprint('{blueprint_name}', __name__, template_folder='templates')\n\n"]
        views_file.writelines(lines)
        views_file.close()


if __name__ == '__main__':
    command_function_map = {
        'addblueprint': 'add_blueprint'
    }
    command, argument = sys.argv[1], sys.argv[2]
    if command in command_function_map:
        locals()[command_function_map[command]](argument)
    else:
        print(f'Invalid command name - **{command}**')
