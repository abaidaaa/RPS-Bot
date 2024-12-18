from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_EN
from keyboards.keyboards import buttons, game_kb
from services.services import get_bot_choice, get_winner

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['/start'],
                         reply_markup=buttons)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'],
                         reply_markup=buttons)
    
@router.message(F.text == LEXICON_EN['yes_button'])
async def game_start(message: Message):
    await message.answer(text=LEXICON_EN['yes'],
                         reply_markup=game_kb)
    
# This handler triggers the user's refusal to play the game
@router.message(F.text == LEXICON_EN['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_EN['no'])


# This handler triggers on any of the game buttons
@router.message(F.text.in_([LEXICON_EN['rock'],
                            LEXICON_EN['paper'],
                            LEXICON_EN['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_EN["bot_choice"]} '
                              f'- {LEXICON_EN[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_EN[winner], reply_markup=buttons)