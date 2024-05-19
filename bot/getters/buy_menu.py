from aiogram_dialog import DialogManager


async def get_my_currency(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']

    return {'my_currency': f'<b>{my_currency}</b>'}


async def get_all_currs_choice(dialog_manager: DialogManager, **kwargs):
    my_currency = dialog_manager.dialog_data['my_currency']
    exchange_currency = dialog_manager.dialog_data['exchange_currency']

    return {'my_currency': f'<b>{my_currency}</b>',
            'exchange_currency': f'<b>{exchange_currency.get('value')}</b>'}