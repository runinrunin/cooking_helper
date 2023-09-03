import json

'''
ingredient : str
Order : Object
Recipe : Object
Full_course : Object

Request are given by the client and its data are store in a json file

Order: Store the ingredients of an order request given by the client in two categories:
       Core ingredients and additional ingredients.

Recipe: Store the recipe's name of a recipe request given by the client.
        Store the ingredients of a recipe request given by the client in two categories:
        Core ingredients and additional ingredients.

Full_course: Store the different recipes that are in the system.
             Client can give a list of recipes form a json file.
             Store a dict mapping ingredients to corresponding recipes' name.
             Store a dict mapping core ingredients to corresponding recipes' name.
             Store a dict mapping additional ingredients to corresponding recipes' name.

JSON files must have the following structure:

[
  {
    "name": "Recipe 1",
    "core_ingredients": ["ingredient 1", "ingredient 2"],
    "additional_ingredients": ["ingredient 3", "ingredient 4"]
  },
  {
    "name": "Recipe 2",
    "core_ingredients": ["ingredient 5", "ingredient 6"],
    "additional_ingredients": ["ingredient 7", "ingredient 8"]
  }
]

TODO:
- If the client adds a new recipe that share the same name as an already existing recipe, 
  finding a mechanism to stop the existing recipe from being overwritten. 
- Storing the different elements in SQL database would be better
- Giving a unique id to each recipe. This id is given at the recipe creation.
- With the recipe Id, a recipe can be searched, overwrite, or deleted.
'''

class Order:
    '''
    attributes:
        self._cores is a set of core_ingredient (str)
        self._adds is a set of additional_ingredient (str)
    '''
    def __init__(self, core_ingredients, add_ingredients):
        self._cores = set(core_ingredients)
        self._adds = set(add_ingredients)
        self._ingredients = self._cores + self._adds
    
    def __len__(self):
        return len(self._cores) + len(self._adds)
    
    def __repr__(self):
        return 'Order(cores ingredients: {}, additionals ingredients: {})'.format(self._cores, self.adds)

    def get_cores(self):
        return self._cores
    
    def get_adds(self):
        return self._adds
    
    def set_order_from_JSON(self, order_file):
        pass

    def exists():
        '''
        TODO
        '''
        return False
    

class Recipe:
    '''
    attributes:
        self.name is a str
        self._cores is a set of core_ingredient (str)
        self._adds is a set of additional_ingredient (str)
    '''
    def __init__(self, name, core_ingredients, add_ingredients):
        self.name = name
        self._cores = core_ingredients
        self._adds = add_ingredients
        self._ingredients = set(core_ingredients) + set(add_ingredients)
    
    def __len__(self):
        return len(self._cores) + len(self._adds)
    
    def __repr__(self):
        cores = self.get_cores()
        adds = self.get_adds()
        return '{} is made with (cores ingredients: {}, additionals ingredients: {})'.format(self.name, cores, adds)

    def get_cores(self):
        return self._cores
    
    def get_adds(self):
        return self._adds
    
    def __eq__(self, other):
        return set(self) == set(other)

class Full_course:
    '''
    attributes:
        self._recipes maps a recipe_name (str) to the Recipe's object
        self._ingredients_to_recipes maps an ingredient_name (str) to a recipe_name
        self._cores_to_recipes maps an core_ingredient_name (str) to a recipe_name
        self._adds_to_recipes maps an additional_ingredient_name (str) to a recipe_name

    TODO:
    Add context message.
    Example, when calling fc.delete_recipe()
    '''
    def __init__(self):
        self._recipes = {}
        self._ingredients_to_recipes = {}
        self._cores_to_recipes = {}
        self._adds_to_recipes = {}

    def __len__(self):
        return len(self._recipes)
    
    def __iter__(self):
        return (i for i in self._recipes)

    def add(self, recipe):
        self._recipes[recipe.name] = recipe
        for ingredient in recipe.get_cores():
            self._ingredients_to_recipes.setdefault(ingredient, []).append(recipe.name)
            self._cores_to_recipes.setdefault(ingredient, []).append(recipe.name)
        for ingredient in recipe.get_adds():
            self._ingredients_to_recipes.setdefault(ingredient, []).append(recipe.name)
            self._adds_to_recipes.setdefault(ingredient, []).append(recipe.name)

    def set_from_JSON(self, recipes_file):
        with open(recipes_file) as f:
            data = json.load(f)

        for recipe in data:
            self.set(recipe['name'],
                     recipe['core_ingredients'],
                     recipe['add_ingredients'])
    
    def set(self, recipe_name, core_ingredients, add_ingredients):
        self.remove(recipe_name)
        self.add(Recipe(name=recipe_name,
                        core_ingredients=core_ingredients,
                        add_ingredients=add_ingredients))
    
    def write_on_JSON(self, recipe_file):
        data = []
        for recipe in self._recipes:
            data.append({'name': self._recipes[recipe]['name'],
                         'core_ingredients': self._recipes[recipe]['core_ingredients'],
                         'add_ingredients': self._recipes[recipe]['add_ingredients']})
        with open(recipe_file, 'W') as f:
            json.dump(data, f)
        
    def remove(self, recipe_name):
        if recipe_name in self._recipes:
            del self._recipes[recipe_name]
            for ingredient in self._ingredients_to_recipes:
                if recipe_name in self._ingredients_to_recipes[ingredient]:
                    self._ingredients_to_recipes[ingredient].remove(recipe_name)
            for ingredient in self._cores_to_recipes:
                if recipe_name in self._core_to_recipes[ingredient]:
                    self._cores_to_recipes[ingredient].remove(recipe_name)
            for ingredient in self._adds_to_recipes:
                if recipe_name in self._adds_to_recipes[ingredient]:
                    self._adds_to_recipes[ingredient].remove(recipe_name)
                

