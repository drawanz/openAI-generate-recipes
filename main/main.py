import os
import openai
from dotenv import load_dotenv
load_dotenv()
from create_dish.create_dish import Dish
from user_input.user_input import Input

openai.api_key = os.getenv('OPENAI_API_KEY')

class Main:
    def __init__(self, dish: Dish, user_input: Input):
        self.dish = dish
        self.user_input = user_input

    
    def main():
        pass