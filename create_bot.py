from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage


bot = Bot("token")
dp = Dispatcher(bot, storage=MemoryStorage())


