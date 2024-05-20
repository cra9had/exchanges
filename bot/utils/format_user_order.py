from typing import Dict


def format_order(dialog_data: Dict, user_id: int, username: str | None) -> str:

    order = f'<b> Заказ пользователя {user_id}</b>' if not username else f'<b>Заказ пользователя @{username}</b>\n\n'
    my_currency, exchange_currency = dialog_data["my_currency"], dialog_data["exchange_currency"]
    order += f'Валюта для оплаты: <b>{my_currency["value"]}</b> {my_currency["text"]}\n'
    order += f'Валюта для обмена: <b>{exchange_currency["value"]}</b> {exchange_currency["name"]}\n'
    order += f'Реквизиты для получения валюты: <code>{dialog_data["my_credentials"]}</code>\n'
    order += f'Доставка: {dialog_data["delivery_type"]}\n'

    return order
