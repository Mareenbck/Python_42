cookbook = {
	"sandwich": {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	},
	"cake": {
		"ingredients": ["flour", "sugar", "eggs"],
		"meal": "dessert",
		"prep_time": 60
	},
	"salad": {
		"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "lunch",
		"prep_time": 15
	}
}

def print_recipes():
	for recipe in cookbook:
		print("{}".format(recipe))
	print("\n")

def print_one_recipe(recipe):
	if recipe in cookbook.keys():
		print("Recipe for {}:".format(recipe))
		print("Ingredients list: {}.".format(cookbook[recipe]['ingredients']))
		print("To be eaten for {}.".format(cookbook[recipe]['meal']))
		print("Takes {} minutes of cooking.\n".format(cookbook[recipe]['prep_time']))
	else:
		print("There is no recipe for this")

def add_recipe():
	print(">>> Enter a name:")
	name = input()
	print(">>> Enter ingredients:")
	ingredients = input()
	ingredients = ingredients.split(',')
	print(">>> Enter a meal type:")
	meal = input()
	print(">>> Enter a preparation time:")
	prep_time = input()
	new_recipe = {
		"ingredients": ingredients,
		"meal": meal,
		"prep_time": int(prep_time)
	}
	cookbook[name] = new_recipe

def delete_recipe(recipe):
	if recipe in cookbook.keys():
		del cookbook[recipe]
	else:
		print("There is no recipe for this")

def main():
	print("Welcome to the Python Cookbook ! \n\nList of available option:")
	action = ''
	while action != '5':
		print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
		print("\nPlease select an option:\n>>")
		action = input()
		if action == '1':
			add_recipe()
		elif action == '2':
			print("Please enter a recipe name you want to delete:\n>>")
			recipe = input()
			delete_recipe(recipe)
		elif action == '3':
			print("Please enter a recipe name to get its details:\n>>")
			recipe = input()
			print_one_recipe(recipe)
		elif action == '4':
			print_recipes()
		elif action == '5':
			print("Cookbook closed. Goodbye !\n")
		else:
			print("Sorry, this option does not exist.\n")

if __name__ == "__main__":
	main()
