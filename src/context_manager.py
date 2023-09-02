from typing import Any
import os




class Filter:
        '''
        Une fonction ne reait-elle pas plus simple ?
        '''
        def __init__(self, extended_search=False, consider_additonal=False, optimal_search=False):
            
            self.optimal_search = optimal_search
            self.extended_search = not (optimal_search or not extended_search)
            self.consider_additonals = consider_additonal

        def __call__(self, *args: Any, **kwds: Any) -> Any:
             pass

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