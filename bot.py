from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database

TOKEN = '5300368249:AAFoBVdycTzs1cYZKqfdWXabj692nsOxX7o'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('database.db')