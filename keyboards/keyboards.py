from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_EN


# Creating keyboard from ReplyKeyboardBuilder

btn_yes = KeyboardButton(text=LEXICON_EN['yes_button'])
btn_no = KeyboardButton(text=LEXICON_EN['no_button'])

# Init builder class
builder = ReplyKeyboardBuilder()
# Make width 2 buttons in line
builder.row(btn_yes, btn_no, width=2)
# Markup buttons
buttons: ReplyKeyboardMarkup = builder.as_markup(
    one_time_keyboard=True, # Minimize the keyboard
    resize_keyboard=True # Adjust the keyboard to the size of the device
)

# Create buttons
btn_1 = KeyboardButton(text=LEXICON_EN['rock'])
btn_2 = KeyboardButton(text=LEXICON_EN['scissors'])
btn_3 = KeyboardButton(text=LEXICON_EN['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1],
              [btn_2],
              [btn_3]],
    resize_keyboard=True,
    input_field_placeholder='Choice "Rock", "Scissors" or "Paper"!'
)