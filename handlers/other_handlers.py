from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_EN

router = Router()

@router.message()
async def send_echo(message: Message):
        await message.reply(text=LEXICON_EN['other_answer'])