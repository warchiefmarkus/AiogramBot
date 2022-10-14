from aiogram import Bot, Dispatcher

from bot import main_dispatcher, ai_bot
from models.base import start_db, shutdown_db


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    await bot.delete_webhook()
    await start_db()


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    await shutdown_db()


if __name__ == "__main__":
    main_dispatcher.startup.register(on_startup)
    main_dispatcher.shutdown.register(on_shutdown)
    main_dispatcher.run_polling(ai_bot)
