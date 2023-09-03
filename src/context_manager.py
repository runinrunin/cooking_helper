from typing import Any
from elements_classes import Full_course
from utils import lists_match
import os




class Filter:
        '''
        A function would be better, no?
        '''
        def __init__(self, extended_search=False, consider_additonal=False, optimal_search=False):
            
            self._optimal_search = optimal_search
            self._extended_search = not (optimal_search or not extended_search)
            self._consider_additonals = consider_additonal

        def __call__(self, order, full_course):
             pass
        
        def optimal_search(self, order, full_course):              
             pass
        
        def extended_search(self, order, full_course):
            recipes = set()
            if self.consider_additonals:
                  ingredients = full_course._ingredients_to_recipes
            else:
                  ingredients = full_course._cores_to_recipes
            for ingredient in order._ingredients:
                 if ingredient in ingredients:
                  recipes.add(recipe for recipe in ingredients[ingredient])    
            return recipes
                  
        
        def search(self, order, full_course):
            considered_recipes = set()

            if self._consider_additionals:
                order_ingredients = order._ingredients
                recipes_ingredients_dict = full_course._ingredient_to_recipe
                if not lists_match(set(recipes_ingredients_dict.keys()), order_ingredients):
                     pass
                else:
                    considered_ingredients = set(recipes_ingredients_dict.keys()).intersection(set(order_ingredients))
                    for ingredient in considered_ingredients:
                        for recipe in recipes_ingredients_dict[ingredient]:
                            if lists_match(order_ingredients, full_course._recipes[recipe]._ingredients):
                                    considered_recipes.add(recipe)

            else:
                order_ingredients = order._cores
                recipes_ingredients_dict = full_course._cores_to_recipes
                if not lists_match(set(recipes_ingredients_dict.keys()), order_ingredients):
                    pass
                else:
                    considered_ingredients = set(recipes_ingredients_dict.keys()).intersection(set(order_ingredients))
                    for ingredient in considered_ingredients:
                        for recipe in recipes_ingredients_dict[ingredient]:
                            if lists_match(order_ingredients, full_course._recipes[recipe]._ingredients):
                                    considered_recipes.add(recipe)
            return considered_recipes

class Context_manager:

    '''
    filters options are:
    - extended_search: If True, does a union search of all recipes that contain one or multiples core ingredient of the order.
                       If False, does a search restricted to recipes that contains only ingredients in the order.
    - consider_additonal: If True, the recipes that does not contains the additional ingredients are sorted out.
    - optimal_search: If true, the software will gives the optimal set of recipe using all possible ingredients for the correct 
                      quantities. 
                      By setting optimal_search = True, the extended_search option is set to False, and the output is yet filtered.
                      For ingredients where quantity is set to None, the program consider there is an infinite amount of those ingredients
    '''

    def __init__(self, recipes_file, order_path):
        self.recipes_file = recipes_file
        self.order_path = order_path

        self._add_ingredients = False
        self._extensive_search = False
        self._optimal_search = False
        self._filter = None

    def create_filter(self):
        self._filter = Filter(optimal_search=self._optimal_search,
                              extended_search=self._extensive_search,
                              consider_additonal=self._add_ingredients
                              )

    def intro_message(self):
        print("# What kind of search do you want to perform?")
        print(" - including additional ingredients: You want to include the additional ingredients in the search.")
        print(" - extensive search: You want to search every recipes where the ingredient of the order are present in.")
        print(" - Optimal search: You want to perform an optimal search.") 
        print("                   It will gives you a set of recipe that use as much ingredient you have in the order as possible.")
        print("ex:\n The default search is set with {including additional = True} and {extensive search = False}.")
        print("This search will give you all recipes where all core ingredients of the recipe is present in the order.")
        print(" # If {optimal_search = True}, then extensive_search will be set to False")
        print('\n')


    def search_recipes(full_course, order, filter=Filter()):
        consider_recipes = filter(full_course, order)
        return consider_recipes