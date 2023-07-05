import requests
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# This is a class that describes the database
class Recipe(Base):
    __tablename__ = 'recipe'

    # Columns of the database
    recipe_name = Column('recipe name', String, primary_key=True)  # name of the recipe
    recipe_url = Column('recipe url', String)  # url of the recipe
    ingredients = Column('ingredients', String)  # ingredients used in the recipe

    def __init__(self, recipe_name, recipe_url, ingredients):
        self.recipe_name = recipe_name
        self.recipe_url = recipe_url
        self.ingredients = ingredients

    def __repr__(self):
        return f'\nRecipe: {self.recipe_name}\n URL: {self.recipe_url}\nIngredients:{self.ingredients}'


# creates the engine and runs it
engine = create_engine('sqlite:///project1_db.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# dictionary for the menu
d = {}


def main():
    print("Welcome to the Recipe Finder!")
    choice = input("Would you like to:\n1. Look at saved recipes\n2. Find a new recipe\nEnter 1 or 2: ")

    if choice == "1":
        show_saved_recipes()
    elif choice == "2":
        find_new_recipe()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def show_saved_recipes():
    results = session.query(Recipe).all()
    if results:
        print('Saved Recipes:')
        print(results)
    else:
        print("No saved recipes found.")

def find_new_recipe():
    app_id = "bd853ae1"
    app_key = "8c82c5e3565f991053475e31185e39d0	"

    while True:
        ingredients = [input("Enter the ingredients you have at your disposal (separated by commas): ")]

        search_recipes(app_id, app_key, ingredients)
        # url_picker()

        choice = input("Do you want to input different ingredients? (y/n): ")
        if choice.lower() != 'y':
            url_picker()
            break

def search_recipes(app_id, app_key, ingredients):
    url = "https://api.edamam.com/search"

    #ingredients = [input("Enter the ingredients you have at your disposal(separated by commas):")]

    params = {
        "q": ",".join(ingredients),
        "app_id": app_id,
        "app_key": app_key,
        "to": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    index = 1

    if response.status_code == 200:
        hits = data["hits"]
        if hits:
            for hit in hits:
                recipe = hit["recipe"]
                recipe_name = recipe["label"]
                recipe_url = recipe["url"]
                print(f"{index}: Recipe: {recipe_name}")
                # print(f"URL: {recipe_url}")
                # adds to the dictionary so that all the choices have a unique number
                d[index] = [recipe_name, recipe_url, ingredients]
                index += 1
        else:
            print("No recipes found.")
    else:
        print(f"Error: Unable to fetch recipes. Status code: {response.status_code}")



def url_picker():
    x = input("Which recipe would you like? (Pick a number)")
    # checks to see if the input is a valid number
    if x.isdigit() and int(x) in d:
        # adds the choice to the database and displays the url
        table_entry = d[int(x)]
        recipe = Recipe(table_entry[0], table_entry[1], table_entry[2][0])
        try:
            session.add(recipe)
            session.commit()
        except:
            i = 0
        print(table_entry[1])
    # continues to prompt the user until a valid response is given
    else:
        print("Sorry, no matches found. Please select another number")
        while True:
            x = input("Which recipe would you like? (Pick a number)")
            if x.isdigit() and int(x) in d:
                table_entry = d[int(x)]
                print(table_entry[1])
                recipe = Recipe(table_entry[0], table_entry[1], table_entry[2][0])
                session.add(recipe)
                session.commit()
                break
            else:
                print("Sorry, no matches found. Please select another number")



if __name__ == "__main__":
    main()
