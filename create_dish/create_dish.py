class Dish:
    def __init__(self, ingredients: str) -> None:
        self.ingredients = ingredients


    def create_recipe(self):
        return f"""
        You are a reputed chef, you come home and you have just a few ingredients to cook. You have this basics ingredients such as: salt, pepper, water, oil, butter, onions and garlic, you have to combine this with the list informed as  'Ingredients'. You don't have to use everything, but you do the best combination possible for this meal.

        Ingredients: {self.ingredients}

        Title of the recipe:
        Used ingredients:
        Instructions: 
        """
    

    