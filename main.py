import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='6337181033:AAFzwsVZCrXbM5VMVwwwGJMMGDRYHYa1bQo')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привіт!')
    await message.reply('Як справи?')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('The bot is disabled.')
    except:
        print('We have a problem')