import json
import os
from pathlib import Path
from typing import Dict 

class NotJsonFileError(Exception):
    pass

def create_directory_in_current_dir(directory_name: str) -> None:
    current_directory = Path(__file__).parent.absolute()
    new_directory_path = current_directory / directory_name

    try:
        new_directory_path.mkdir()
        print(f"Directory '{directory_name}' created in '{current_directory}'")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists in '{current_directory}'")

def check_if_recipes_file_exists(directory_name: str) -> bool:
    current_directory = Path(__file__).parent.absolute()
    recipes_directory_path = current_directory / directory_name
    recipes_file = recipes_directory_path / "recipes.json"

    try: 
        recipes_directory_path.exists
    except FileExistsError:
        print(f"Diretory {recipes_directory_path} does not exists. Create th directory first.")
        return False
    return True

def is_json_file(file_path):
    path = Path(file_path)
    if path.suffix.lower() != ".json":
        raise NotJsonFileError(f"{file_path} is not a JSON file.")
    

def create_recipes_file(directory_name: str) -> None:
    current_directory = Path(__file__).parent.absolute()
    recipes_directory_path = current_directory / directory_name
    recipes_file = recipes_directory_path / "recipes.json"

    try: 
        recipes_file.touch()
        print(f"Recipe file created in {recipes_file}.")
    except FileExistsError:
        print(f"{recipes_file}, the recipe file already exists.")


    

def validate_json(json_object: Dict) -> bool:
    """
    Returns True if the JSON object is in the expected form, False otherwise.
    """
    expected_keys = ['name', 'ingredients']
    unexpected_keys = set(json_object.keys()) - set(expected_keys)
    if len(unexpected_keys) > 0:
        return False
    
    # Check name field
    if not isinstance(json_object['name'], str):
        return False
    
    # Check ingredients field
    if not isinstance(json_object['ingredients'], list):
        return False
    for ingredient in json_object['ingredients']:
        if not isinstance(ingredient, dict):
            return False
        expected_ingredient_keys = ['name', 'quality', 'quantity']
        unexpected_ingredient_keys = set(ingredient.keys()) - set(expected_ingredient_keys)
        if len(unexpected_ingredient_keys) > 0:
            return False
        if not isinstance(ingredient['name'], str):
            return False
        if not isinstance(ingredient['quality'], bool):
            return False
        if not isinstance(ingredient['quantity'], float):
            return False
    
    return True

def set_match(set1, set2) -> bool:
    return len(set2) == len(set(set2).intersection(set1))


def messages(select: int) -> None:
    ''' I am on python 3.9, I don't have access to match statement. '''
    if select == 1:
        msg = '*** welcome to python cooking helper ***' \
              'I can help you plan your meals. Give me a list of recipes in the json file in data, or type it later.'
