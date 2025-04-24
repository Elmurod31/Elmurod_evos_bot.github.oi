import asyncio
from os import getenv
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from handlers import handlers_router as handlers

load_dotenv()
dp = Dispatcher()
TOKEN = getenv("TOKEN")

dp.include_router(handlers)



async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting...........")
    asyncio.run(main())