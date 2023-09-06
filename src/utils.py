import os

def create_data(data_dir_path, data_file_path):
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)
        open(data_dir_path, 'w').close()

    elif not os.path.exists(data_file_path):
        open(data_file_path, 'w').close()

def mess_menue(full_course, data_dir_path):
    print(" ===== You are in the main menue. =====")
    print("# You currently have {} recipe(s) register.".format(len(full_course)))
    print("# What would you like to do?")
    print(" - type 1 if you want to pass an Order.")
    print(" - type 2 if you want to update from the json file in {}.".format(data_dir_path))
    print(" - type 3 if you want to print the list of recipe.")
    print(' - type 0 if you want to leave.')
    print("\n")

def wrong_choice_loop(choice, exclude_list, error_message=None, input_message=None):
    while choice not in exclude_list:
            if isinstance(error_message, str):
                print(error_message)
            if isinstance(input_message, str):
                choice = input(input_message)
            else:
                choice = input('Enter input')
    return choice

def lists_match(list1, list2):
    return len(list2) == len(set(list2).intersection(list1)) 