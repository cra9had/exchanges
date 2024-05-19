from aiogram_dialog import DialogManager


async def get_my_currency(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency'].get('text')

    return {'my_currency': f'<b>{my_currency}</b>'}


async def get_all_currs_choice(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']
    exchange_currency = dialog_manager.dialog_data['exchange_currency']

    return {'my_currency_text': f'<b>{my_currency.get('text')}</b>',
            'exchange_currency': f'<b>{exchange_currency.get('value')}</b>'}


async def get_my_curr_input_values(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']
    exchange_currency = dialog_manager.dialog_data['exchange_currency']

    return {'my_currency_text': f'<b>{my_currency.get('text')}</b>',
            'my_currency_value': f'<b>{my_currency.get('value')}</b>',
            'exchange_currency': f'<b>{exchange_currency.get('value')}</b>'}


async def get_input_credentials(dialog_manager: DialogManager, **kwargs):
    my_credentials = dialog_manager.dialog_data['my_credentials']
    return {'my_credentials': f'<code>{my_credentials}</code>'}
