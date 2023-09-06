from aiogram import types, Dispatcher
from keyboards.pay_inl import inl_kb
from create_bot import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from payments import Payment


async def start(message: types.Message):
    kb = inl_kb(1, 5, "text") #генерация инлайн колбэка

    await message.answer("Payment:", reply_markup=kb)


async def payment(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, f"Оплата:")

    pay = call.data.split("+")
    pt = Payment
    """Отправление ссылки на платёж"""
    await bot.send_message(f'{Payment.generate_new_url_for_pay(self=pt, order_id=pay[1], amount=pay[2], text=pay[3])}')
    """Получение статуса платежа"""
    # Payment.get_order_status_from_liqpay(self=pt, order_id=1)



def handlers_bot(dp: Dispatcher):
    dp.register_message_handler(start, commands=["buy"])
    dp.register_callback_query_handler(payment, lambda x: x.data and x.data.startswith("payment+"))
