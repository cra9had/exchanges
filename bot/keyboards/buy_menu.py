from aiogram.utils.keyboard import InlineKeyboardBuilder


def confirm_payment_kb(user_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Подтвердить", callback_data=f'confirm_payment_{user_id}')
    builder.button(text="Отклонить", callback_data=f'decline_payment_{user_id}')

    return builder.as_markup()