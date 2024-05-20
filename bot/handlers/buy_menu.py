import re

from aiogram import Bot
from aiogram.enums import ContentType, ParseMode
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from bot.keyboards.buy_menu import confirm_payment_kb
from bot.states.cabinet import CabinetSG
from bot.utils.format_user_order import format_order


async def input_my_curr_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    try:
        my_currency_value = int(message.text)
    except ValueError:
        return

    dialog_manager.dialog_data['my_currency'].update(value=my_currency_value)
    await dialog_manager.next()


async def input_credentials_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    card_pattern = r'^\d{16}$'
    cryptowallet_pattern = r'^[a-zA-Z0-9]{33,}$'
    if re.match(card_pattern, message.text) or re.match(cryptowallet_pattern, message.text):
        dialog_manager.show_mode = ShowMode.AUTO
        dialog_manager.dialog_data['my_credentials'] = message.text
        await dialog_manager.next()
    else:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer("⚠️ Неправильный формат: введённые данные не являются ни картой, ни кошельком.")


async def input_payment_detals(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    bot: Bot = dialog_manager.middleware_data['bot']
    for operator in dialog_manager.middleware_data['operators']:
        caption = format_order(dialog_manager.dialog_data, message.chat.id, message.from_user.username)
        if message.document:
            await bot.send_document(chat_id=operator, document=message.document.file_id, caption=caption,
                                    reply_markup=confirm_payment_kb(message.chat.id))
        if message.photo:
            await bot.send_photo(chat_id=operator, photo=message.photo[-1].file_id, caption=caption,
                                 reply_markup=confirm_payment_kb(message.chat.id))

    await dialog_manager.next()


async def after_payment_to_menu_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager, **kwargs) -> None:
    await dialog_manager.start(state=CabinetSG.cabinet_menu, mode=StartMode.RESET_STACK)
