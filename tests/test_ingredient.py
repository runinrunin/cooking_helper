from cooking_helper.elements import Ingredient

def create_correct_ingredient() -> Ingredient:
    print('creating an expected ingredient')
    ingredient = Ingredient(name="banana", quantity=1.)
    print(ingredient)
    return ingredient

def create_wrong_ingredient1():
    print('creating an ingredient with unexpected inputs')
    ingredient = Ingredient(name=43, quantity=1.)
    print(ingredient)
    return ingredient

def create_wrong_ingredient2():
    print('creating an ingredient with unexpected inputs')
    ingredient = Ingredient(name='banana', quantity=[16, 21])
    print(ingredient)
    return ingredient

def change_ingredient(ingredient: Ingredient):
    print(f'changing attributes in {ingredient}')
    ingredient.name = 'Apple'
    ingredient.quantity = 1.
    ingredient.core = True
    print(f'after change: {ingredient}')