from main.main import Main
from create_dish.create_dish import Dish
from user_input.user_input import Input


user_input = Input.create_user_input_for_dish()
dish = Dish(user_input)
new_dish = Main(dish.create_recipe())
print(new_dish.main())
recipe_title = new_dish.main().split("\n")[1].split(':')[1].strip()




