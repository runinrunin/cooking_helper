from typing import Any
from elements_classes import Ingredient, Recipe, Order, Full_course
from context_manager import Context_manager
from utils import create_data, mess_menue, wrong_choice_loop
import os

    
def main():
    print(" *** welcome to the cooking helper ***\n")

    fc = Full_course()
    order = Order()

    script_dir = os.path.dirname(__file__)
    data_dir_name = "data"
    data_dir_path = os.path.join(script_dir, data_dir_name)

    recipes_file_name = "recipes.json"
    recipes_file_path = os.path.join(data_dir_path, recipes_file_name)
    if os.path.exists(recipes_file_path):
        print("Loading your existing recipe(s).\n")
        fc.set_from_JSON(recipes_file_path)
    else:
        print("You don't have any recipe.")
        print("A new recipes file will be created in:\n {}".format(recipes_file_path))
        print('\n')
        create_data(data_dir_path, recipes_file_path)

    order_file_name = "order.json"
    order_file_path = os.path.join(data_dir_path, order_file_name)
    if os.path.exists(order_file_path):
        print("Succesfully loading your existing order.\n")
        order.set_from_JSON(order_file_path)
    else:
        print("You don't have any order.")
        print("you will be able to set an order later.\n")    

    keep_on = True
    while keep_on:
        mess_menue(fc, data_dir_path)

        choice = input("Enter your choice (0-3):")
        print("\n")

        choice = wrong_choice_loop(choice=choice,
                                   exclude_list=["0", "1", "2", "3"],
                                   error_message="# Please, enter a choice between 0 and 3 (included)",
                                   input_message="Enter your choice (0-3):"
                                   )
        print('\n')

        if choice == "0":
            keep_on = False

        elif choice == "2":
            print("# Getting the content from the current data file in {}".format(recipes_file_path))
            print('\n')
            fc.set_from_JSON(recipes_file_path)

        elif choice == "3":
            print(" # You currently have {} recipe(s):".format(len(fc)))
            for recipe in fc:
                print(recipe)
            print('\n')

        if choice == "1":
            cm = Context_manager()
            cm.intro_message()

            if not order.exist():
                print('# No order is currently register.')
                print('# register an order first.')
                print('- You can register an order from the terminal (type 0).')
                print('- You can register an order from a json file (type 1).\n')

                order_input_choice = input('Type 0 or 1:')
                order_input_choice = wrong_choice_loop(choice=order_input_choice,
                                                       exclude_list=['0', '1'],
                                                       error_message="Register an order from the terminal (type 0) or from a json file (type 0).",
                                                       input_message='Type 0 or 1:'
                                                       )
                
                if order_input_choice == '0':
                    '''
                    TODO:
                    Implement a method to register an order from the terminal
                    '''
                    pass
                else:
                    order.set_order_from_JSON(order_file_path)
            
            print('# Do you want to include additional ingredients to the search?')
            additional_ingredients_choice = input(' - type y (yes) / n (no):')
            additional_ingredients_choice = wrong_choice_loop(choice=additional_ingredients_choice,
                                                              exclude_list=['y', 'n'],
                                                              error_message="Please, enter \"y\" for yes or \"n\" for no (without coma).",
                                                              input_message=' - type y (yes) / n (no):'
                                                              )
            print('\n')
            if additional_ingredients_choice == 'y':
                cm._add_ingredients = True

            print('# Do you want to perform an extensive search?')
            extensive_search_choice = input(' - type y (yes) / n (no):')
            extensive_search_choice = wrong_choice_loop(choice=extensive_search_choice,
                                                              exclude_list=['y', 'n'],
                                                              error_message="Please, enter \"y\" for yes or \"n\" for no (without coma).",
                                                              input_message=' - type y (yes) / n (no):'
                                                              )
            print('\n')
            if extensive_search_choice == 'y':
                cm._extensive_search = True

            print('# Do you want to include additional ingredients to the search?')
            optimal_search_choice = input(' - type y (yes) / n (no):')
            optimal_search_choice = wrong_choice_loop(choice=optimal_search_choice,
                                                              exclude_list=['y', 'n'],
                                                              error_message="Please, enter \"y\" for yes or \"n\" for no (without coma).",
                                                              input_message=' - type y (yes) / n (no):'
                                                              )
            print('\n')
            if optimal_search_choice == 'y':
                cm._optimal_search = True


            cm.create_filter()

if __name__ == "__main__":
    main()