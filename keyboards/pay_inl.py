from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inl_kb(order_id, payment, text):
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text="Оплатить", callback_data=f"payment+{order_id}+{payment}+{text}"))
