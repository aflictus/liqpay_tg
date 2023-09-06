from aiogram.utils import executor
from create_bot import dp
from handlers import payment_handler


async def on_startup(_):
    print("The bot has been enabled")

payment_handler.handlers_bot(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)







