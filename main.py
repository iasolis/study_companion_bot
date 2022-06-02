import logging
from bot import dp
from aiogram import executor
import sys

sys.path.insert(0, '/handlers/handler_reg.py')
sys.path.insert(0, '/handlers/handler_menu_profile.py')
sys.path.insert(0, '/handlers/handler_menu_main.py')
sys.path.insert(0, '/handlers/handler_match.py')
from handlers import handler_reg, handler_menu_profile, handler_menu_main, handler_match


async def start_up(_):
    print("BOT Online!")
    logging.basicConfig(level=logging.INFO)


handler_reg.handler_register(dp)
handler_menu_profile.handler_menu_profile(dp)
handler_menu_main.handler_menu_main(dp)
handler_match.handler_menu_match(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_up)
