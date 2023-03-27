class Input:
    def __init__(self):
        pass

    def create_user_input_for_dish() -> str:
        incoming_input = input("Hello! It's great to have you here. Please enter the ingredients you have, separated by commas: ")
        return incoming_input.strip()
    
    
