from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контаки'),
                                     KeyboardButton(text='Про нас')]],
                                     resize_keyboard=True,
                                      input_field_placeholder='Виберіть пункт меню...' )

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболкі', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кросівки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')]])