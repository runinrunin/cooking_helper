from attrs import define, field
from typing import Set, Dict, Any, Type
from cooking_helper.utils import NotJsonFileError, is_json_file, validate_json
import json

class NameMismatchError(ValueError):
    pass

@define(kw_only=True)
class Ingredient:
   
    name: str 
    quantity: float
    core: bool = field(default=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "core": self.core,
            "quantity": self.quantity
        }
    
    def _compare_names(self, other: Type["Ingredient"]) -> None:
        if self.name != other.name:
            raise NameMismatchError(f"Ingredient names do not match. You try to compare {self.name} and {other.name}")
    
    def more_than(self, other: Type["Ingredient"]) -> bool:
        try:
            self._compare_names(other)
        except NameMismatchError as e:
            print(e)
        if self.quantity >= other.quantity:
            return True
        return False
    
    def less_than(self, other: Type["Ingredient"]) -> bool:
        return not self.more_than(other)


@define(kw_only=True)
class Recipe:
    
    name: str
    ingredients: Set[Ingredient] = field(factory=set)
    core_ingredients: Set[Ingredient] = field(factory=set, init=False)

    def __post_init__(self) -> None:
        self.set_core_ingredients()

    def set_core_ingredients(self) -> None:
        for ingredient in self.ingredients:
            if ingredient.core:
                self.core_ingredients.add(ingredient)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients]
        }

@define
class Fullcourse:

    recipes: set[Recipe] = field(factory=set, init=False)

    def load_from_json(self, file_path: str) -> None:
        try: 
            is_json_file(file_path)
        except NotJsonFileError as e:
            print(e)
        with json.loads(file_path) as f:
            for json_object in f:
                if validate_json(json_object):
                    self.recipes.add(json_object)

    def search_recipes_by_name(self, recipe_name: str) -> set[Recipe]:
        selected_recipe = set()
        for recipe in self.recipes:
            if recipe.name==recipe_name:
                selected_recipe.add(recipe)
        return selected_recipe

    def delete_recipes_by_name(self, recipe_name: str) -> None:
        self.recipes = self.recipes - self.search_recipes_by_name(recipe_name)

    
    def add_recipe(self, recipe: Recipe) -> None:
        self.recipes.add(recipe)

    def delete_recipe(self, recipe) -> None:
        if recipe in self.recipes:
            self.recipes.remove(recipe)