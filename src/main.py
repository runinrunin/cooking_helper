class Ingredient:
    def __init__(self, name, core=None, quantity=None):
        self.name = name
        self.core = core
        self.quantity = quantity

    def __eq__(self, __value: object) -> bool:
        pass

class Order:
    '''
    An Order is a list of ingredient pass by the client. The context manager will parse it to give a list of recipes.
    Each Order is define by the list of ingredients it is composed.
    '''
    def __init__(self, items):
        self._items = items

    def __getitem__(self, position):
        return self._items[position]
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        cores = self.get_cores()
        adds = self.get_adds()
        return 'Order(cores ingredients: {}, additionals ingredients: {})'.format(cores, adds)

    def get_cores(self):
        cores = []
        for item in self._items:
            if item.core:
                cores.append(item)
        return cores
    
    def get_adds(self):
        adds = []
        for item in self._items:
            if not item.core:
                adds.append(item)
        return adds
    

class Recipe:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_cores(self):
        cores = []
        for item in self.items:
            if item.core:
                cores.append(item)
        return cores
    
    def get_adds(self):
        adds = []
        for item in self.items:
            if not item.core:
                adds.append(item)
        return adds

class Full_course:
    def __init__(self):
        self.recipes = {}
        self.ingredients_to_recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe
        for ingredient in recipe.items:
            self.ingredients_to_recipes.setdefault(ingredient.name, []).append(recipe.name)

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