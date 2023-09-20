from typing import Set, Dict, Any, List
from elements_classes import Recipe, Ingredient, FullCourse
from utils import set_match

fc = FullCourse
fc.

# TODO
# If I change the Ingredient and Recipe classes, then I must rewrite this code.

def adding_recipes_to_selection(ingredient_name: str, fullcourse: FullCourse) -> set[str]:
    recipes_names = fullcourse.ingredients_to_recipes[ingredient_name]
    return set("TODO")

def compare_ingredient(ingredient1: Ingredient, ingredient2: Ingredient) -> bool:
    i1_in_i2 = False
    if ingredient1.name == ingredient2.name:
        if ingredient1.core == ingredient2.core:
            if ingredient2.quantity <= ingredient1.quantity:
                i1_in_i2 = True
    return i1_in_i2


def filter_recipes_by_ingredients(ingredients: Set[Ingredient], fullcourse: FullCourse, mode='basic') -> set[Recipe]:
    ''' if mode="evrything":
             Basic filtering that keep all recipes that have at least one ingredient in the submitted ingredients.
        if mode="restricted":
             Basic filtering that keep all recipes that have no more ingredients than the submitted ingredients.
        if mode=None:
            Advanced filtering that filter recipe according to the type of ingredient, and the quantities.'''
    selected_recipes_name = set()
    ingredients_names = set(ingredient.name for ingredient in ingredients)

    for ingredient_name in ingredients_names:
        if ingredient_name.name in fullcourse.ingredients_to_recipes.k:
            selected_recipes_name = selected_recipes_name.union(fullcourse.ingredients_to_recipes[ingredient_name])
    selected_recipes = set(recipe for recipe in fullcourse.recipes if recipe.name in selected_recipes_name)

    if mode=="basic":
        return selected_recipes

    for recipe in selected_recipes:
        if not set_match(ingredients_names, set(ingredient.name for ingredient in recipe.ingredients)):
            selected_recipes.remove(recipe)

    if mode=="restricted":
        return selected_recipes
    
    # This triple loop is awfull...
    for recipe in selected_recipes:
        for ingredient_in_recipe in recipe.ingredients:
            for ingredient in ingredients:
                if not compare_ingredient(ingredient, ingredient_in_recipe):
                    selected_recipes.remove(recipe)

    return selected_recipes


def filter_recipes_by_ingredients(ingredients: Set[Ingredient], fullcourse: FullCourse, only_core=True, correct_quantities=True) -> List[Recipe]:
    selected_recipes = set()
    if only_core:
        for ingredients in ingredients:
            selected_recipes = selected_recipes.union(fullcourse.)