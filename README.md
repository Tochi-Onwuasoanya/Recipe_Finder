# Recipe_Finder
This code provides a simple recipe finder program that allows users to save recipes and find new recipes based on the ingredients they have. The program uses the Edamam API to search for recipes.

# Installation
To run this program, you need to install the following dependencies:

requests: It can be installed using pip install requests.
sqlalchemy: It can be installed using pip install sqlalchemy.
Usage
Run the program by executing the Python script. You will be prompted with a menu to choose from two options:

Look at saved recipes: This option will display the recipes that have been saved in the database.

Find a new recipe: This option allows you to search for new recipes based on the ingredients you have. You will be prompted to enter the ingredients you have at your disposal (separated by commas). The program will then fetch recipes using the Edamam API and display the search results. You can select a recipe by entering the corresponding number. If no matches are found, you will be prompted to select another number.

# Database
The program uses an SQLite database named project1_db.db. The database contains a single table named recipe with the following columns:

recipe_name: The name of the recipe (primary key).
recipe_url: The URL of the recipe.
ingredients: The ingredients used in the recipe.

# API Keys
The program requires an Edamam API ID and API key to perform recipe searches. The API ID and key should be assigned to the app_id and app_key variables in the code, respectively. Make sure to replace the placeholder values with your own API credentials.

# License
This project is licensed under the MIT License. Feel free to modify and use the code as per your needs.
