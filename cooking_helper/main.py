from utils import create_directory_in_current_dir, create_recipes_file

def main() -> None:
    recipe_folder_name = 'recipe_folder'
    create_directory_in_current_dir(recipe_folder_name)
    create_recipes_file(recipes_folder=recipe_folder_name)

    

if __name__=='__main__':
    main() 