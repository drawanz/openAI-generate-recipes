import os
import openai
from dotenv import load_dotenv
load_dotenv()
from create_dish.create_dish import Dish
from user_input.user_input import Input

openai.api_key = os.getenv('OPENAI_API_KEY')

class Main:
    def __init__(self, dish: Dish):
        self.dish = dish

    
    def main(self):
        reponse = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = self.dish,
            temperature = 0.9,
            max_tokens = 512,
        )
        return reponse['choices'][0]['text']