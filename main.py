import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8539582792:AAHq_r4XUZAC5CUR0QOh9KP87rzOY3Eg7mo"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Assalomu alaykum ?? Bot ishladi!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())