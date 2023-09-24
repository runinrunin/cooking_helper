from cooking_helper.elements import Ingredient, Recipe

def create_right_recipe():
    print('Create an expected recipe')
    return Recipe(name='braised_banana', ingredients=frozenset((Ingredient(name="banana", quantity=1., core=True),
                                                               Ingredient(name='rhum', quantity=0.3, core=True),
                                                               Ingredient(name='sugar', quantity=0.3, core=True),
                                                               Ingredient(name='vanilla', quantity=0.1, core=False)
    )))

def create_wrong_recipe1():
    print('create an unexpectec recipe. A list is given to the ingredients attribute.')
    return Recipe(name='braised_banana', ingredients=[Ingredient(name="banana", quantity=1., core=True),
                                        Ingredient(name='rhum', quantity=0.3, core=True),
                                        Ingredient(name='sugar', quantity=0.3, core=True),
                                        Ingredient(name='vanilla', quantity=0.1, core=False)
    ]                                             
    )

def create_wrong_recipe2():
    print('create an unexpectec recipe. A int is given to the name attribute.')
    return Recipe(name=43, ingredients=frozenset((Ingredient(name="banana", quantity=1., core=True),
                                                               Ingredient(name='rhum', quantity=0.3, core=True),
                                                               Ingredient(name='sugar', quantity=0.3, core=True),
                                                               Ingredient(name='vanilla', quantity=0.1, core=False)
    )))

