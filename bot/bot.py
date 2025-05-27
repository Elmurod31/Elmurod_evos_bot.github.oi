import asyncio
import json
from os import getenv
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice
from dotenv import load_dotenv

from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")
from handlers import handlers_router

load_dotenv()
dp = Dispatcher()
TOKEN = getenv("TOKEN")
CLICK = getenv("CLICK")
bot = Bot (token=TOKEN)
dp.include_router(handlers_router)


@dp.message(F.func(lambda msg: msg.web_app_data if msg.web_app_data else None))
async def get_web_app_data(message: Message):

    products = json.loads(message.web_app_data.data)
    print(f"DATA: {products}")
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="To'lov",
        description="Mahsulotlar uchun to'lov",
        payload="Maxfiy malumot",
        currency="UZS",
        prices=[LabeledPrice(label=p['name'], amount=(int(p['price']) * p['count'] * 100))
                for p in products],
        provider_token=CLICK,
        max_tip_amount=50000000,
        suggested_tip_amounts=[500000, 1000000, 2000000],
    )


@dp.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(query.id, ok=True)


@dp.message(F.func(lambda msg: msg.successful_payment if msg.successful_payment else None))
async def successful_payment(msg: Message):
    print(msg.successful_payment)
    await msg.answer("To'lov uchun raxmat!")




async def main() -> None:
    # bot = Bot(token=TOKEN)
    bot = Bot(token=TOKEN, session=session)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting.........")
    asyncio.run(main())