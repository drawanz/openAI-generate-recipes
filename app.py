from main.main import Main
from create_dish.create_dish import Dish
from user_input.user_input import Input


user_input = Input.create_user_input_for_dish()
dish = Dish(user_input)
new_dish = Main(dish.create_recipe())
print(new_dish.create_dish())
recipe_title = new_dish.create_dish().split("\n")[1].split(':')[1].strip()
print(new_dish.create_image_from_title(recipe_title))




