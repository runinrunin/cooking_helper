from elements_classes import Ingredient, Recipe, Order, Full_course

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

    class Filters:
        def __init__(self, extended_search=False, consider_additonal=False, optimal_search=False):
            
            self.optimal_search = optimal_search
            self.extended_search = not (optimal_search or not extended_search)
            self.consider_additonals = consider_additonal


    def search_recipes(full_course, order, filters=None):
        consider_recipes = []
        return consider_recipes
    
def main():
    pass

if __name__ == "__main__":
    main()