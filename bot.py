from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database

TOKEN = '5223109925:AAEmhvYf03am5ky0NOO2L0K97H8SFigDtUM'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('database.db')