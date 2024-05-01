from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keybords as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привіт!', reply_markup=kb.main)
    # await message.reply('Як справи?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Ви натиснули на кнопку допомоги')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Виберіть категорію товару', reply_markup=kb.catalog)