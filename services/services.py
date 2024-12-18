import random
from lexicon.lexicon import LEXICON_EN

RULES = {'rock': 'scissors',
         'scissors': 'paper',
         'paper': 'rock'}

RPS_VALUES = {'rock': 'Rock 🗿',
              'paper': 'Paper 📜',
              'scissors': 'Scissors ✂',}

def get_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper'])

def _get_key(user_choice: str) -> str:
    for key in RPS_VALUES:
        if RPS_VALUES[key] == user_choice:
            return key

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _get_key(user_choice)
    if user_choice == bot_choice:
        return 'nobody_won'
    elif RULES[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'