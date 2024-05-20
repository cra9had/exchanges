import os

from aiogram_dialog import DialogManager

from bot.const.buy_menu import OP_CREDENTIALS
from services.api import Exchanger


async def get_my_currency(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency'].get('text')

    return {'my_currency': f'<b>{my_currency}</b>'}


async def get_all_currs_choice(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']
    exchange_currency = dialog_manager.dialog_data['exchange_currency']

    return {'my_currency_text': f'<b>{my_currency.get('text')}</b>',
            'exchange_currency': f'<b>{exchange_currency.get('name')}</b>'}


async def get_my_curr_input_values(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']
    exchange_currency = dialog_manager.dialog_data['exchange_currency']
    value_to_transfer = my_currency.get('value') * (1 - float(os.getenv('EXCHANGE_COMMISSION')))
    exchange_curr_value = await Exchanger.get_curr_value_in_rub(value_to_transfer, exchange_currency.get('key'))
    dialog_manager.dialog_data['exchange_currency'].update(value=exchange_curr_value)
    return {'my_currency_text': f'<b>{my_currency.get('text')}</b>',
            'my_currency_value': f'<b>{my_currency.get('value')}</b>',
            'exchange_currency_text': f'<b>{exchange_currency.get('name')}</b>',
            'exchange_curr_value': exchange_curr_value}


async def get_input_credentials(dialog_manager: DialogManager, **kwargs):
    my_credentials = dialog_manager.dialog_data['my_credentials']
    return {'my_credentials': f'<code>{my_credentials}</code>'}


async def get_operator_credentials(dialog_manager: DialogManager, **kwargs):
    op_credentials_data = OP_CREDENTIALS
    output_credentials = '💳 <b>Реквизиты для оплаты</b>\n\n'
    for credentials in op_credentials_data.values():
        output_credentials += f'💸 {credentials["name"]} <code>{credentials["credential"]}</code>\n'

    return {'output_credentials': output_credentials}