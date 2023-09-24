from attrs import define, field, validators, Attribute
from typing import Dict, Any, Type, FrozenSet
from .utils import NotJsonFileError, is_json_file, validate_json
import json

def positive_number(istance: type, attribute: Attribute, value: float) -> None:
    '''Custom check wether an attribute of an instance has a positive number assigned to it.'''
    class_name = istance.__class__.__name__
    if value <= 0:
        raise ValueError(f'{class_name} {attribute.name} must be greter than zero.')

class NameMismatchError(ValueError):
    pass

@define(frozen=True)
class Ingredient:
   
    name: str = field(
        validator=[validators.instance_of(str)], eq=str.lower)
    quantity: float = field(converter=float,
        validator=[validators.instance_of(float), positive_number])
    core: bool = field(
        validator=[validators.instance_of(bool)], default=False)

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


@define(frozen=True)
class Recipe:
    
    name: str = field(
        validator=[validators.instance_of(str)], eq=str.lower)
    ingredients: FrozenSet[Ingredient] = field(
        validator=[validators.instance_of(FrozenSet)], hash=True)
    core_ingredients: FrozenSet[Ingredient] = field(init=False)

    def __post_init__(self) -> None:
        self.set_core_ingredients()

    def set_core_ingredients(self) -> None:
        self.core_ingredients = frozenset([ingredient for ingredient in self.ingredients if ingredient.core])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients]
        }

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Recipe):
            return (self.name, self.ingredients) == (__value.name, __value.ingredients)
        
    def __hash__(self) -> int:
        return hash((self.name, self.ingredients))

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

    def delete_recipe(self, recipe: Recipe) -> None:
        if recipe in self.recipes:
            self.recipes.remove(recipe)