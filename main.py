import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers



# Init Logger
logger = logging.getLogger(__name__)

# Func config and run bot
async def main() -> None:
    # Logging configuration 
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    logging.info('Starting BOT...')
    
    # Load config to variable
    config: Config = load_config()

    # Init BOT and Dispatcher
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Router register
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
