from tests.test_ingredient import create_correct_ingredient, change_ingredient
from tests.test_recipe_init import create_right_recipe, create_wrong_recipe1, create_wrong_recipe2

if __name__=='__main__':
    print('*** Testing Recipe instantiation ***')
    rigt_recipe = create_right_recipe()
    wrong_reipe = create_wrong_recipe1()
    
