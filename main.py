import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router


async def main():
    bot = Bot(token='6337181033:AAFzwsVZCrXbM5VMVwwwGJMMGDRYHYa1bQo')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('The bot is disabled.')
    except:
        print('We have a problem')