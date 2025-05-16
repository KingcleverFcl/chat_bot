from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from database import async_session
from models import metadata

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать"),
    ])

if __name__ == "__main__":
    import asyncio
    async def main():
        await set_commands()
        from aiogram import Router
        router = Router()
        dp.include_router(router)
        await dp.start_polling(bot)

    asyncio.run(main())
