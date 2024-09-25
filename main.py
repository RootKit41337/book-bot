import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import load_config, Config
from keyboards.main_menu import set_main_menu
from handlers import other_handlers, user_handlers


logger = logging.getLogger(__name__)

async def main():
    #logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    #подрубил конфиг
    config: Config = load_config()

    #подрубил бота
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    #меню бота 
    await set_main_menu(bot)


    #подключаем роутеры
    dp.include_routers(
        user_handlers.router,
        other_handlers.router
    )

    #запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
