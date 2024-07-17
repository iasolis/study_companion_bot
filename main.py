import logging
from src.bot import dp
from aiogram import executor
import sys

sys.path.insert(0, 'src/handlers/handler_reg.py')
sys.path.insert(0, 'src/handlers/handler_menu_profile.py')
sys.path.insert(0, 'src/handlers/handler_menu_main.py')
sys.path.insert(0, 'src/handlers/handler_match.py')
from src.handlers import handler_menu_profile, handler_match, handler_menu_main, handler_reg


async def start_up():
    print("BOT Online!")
    logging.basicConfig(level=logging.INFO)


handler_reg.handler_register(dp)
handler_menu_profile.handler_menu_profile(dp)
handler_menu_main.handler_menu_main(dp)
handler_match.handler_menu_match(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_up)
