"""
Операция "Купить":

    - По нажатию кнопки "Купить" открывается меню выбора валюты для оплаты (в текущей версии - рубль).

    - После выбора валюты пользователем, отображается меню с валютами для
    обмена (криптовалюты, евро, доллар).

    - Пользователь вводит сумму для обмена в рублях.

    - Бот использует интеграцию с сервисами для получения актуального курса и расчета комиссии, формируя сумму для обмена.

    - После нажатия кнопки "Продолжить", пользователь должен ввести реквизиты для получения валюты (адрес кошелька или номер иностранной карты).

    - Пользователю предлагается выбрать способ доставки (быстрая или стандартная).
"""
from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Button, Url, SwitchTo, Column, Next
from aiogram_dialog.widgets.text import Const, Format, Multi

from bot.const.buy_menu import CHOOSE_MY_CURR_TEXT, CHOOSE_EXCHANGE_CURR_TEXT, EXCHANGE_CURRS_BTN_TEXTS
from bot.const.cabinet import SUPPORT_BTN_TEXT, BUY_BTN_TEXT, SUPPORT_BTN_URL, CABINET_MSG_TEXT
from bot.getters.buy_menu import get_my_currency, get_all_currs_choice, get_my_curr_input_values, get_input_credentials, \
    get_operator_credentials
from bot.handlers.buy_menu import input_my_curr_handler, input_credentials_handler, after_payment_to_menu_handler, \
    input_payment_detals
from bot.on_click.buy_menu import go_exchange_currency, go_input_curr_value, input_delivery_type, \
    start_to_menu_after_payment
from bot.on_click.cabinet import start_buy_menu
from bot.states.buy_menu import BuyMenuSG

buy_menu = Dialog(
    Window(
        Const(CHOOSE_MY_CURR_TEXT),
        Column(
            Next(text=Const("Рубль ₽"), id='ruble_to_exchange_click', on_click=go_exchange_currency),
        ),
        state=BuyMenuSG.choose_my_currency,
    ),
    Window(
        Format("Вы выбрали {my_currency}"),
        Const(CHOOSE_EXCHANGE_CURR_TEXT),
        Column(
            *(Next(text=Const(exch_curr_value), id=f'{exch_curr_key}_click', on_click=go_input_curr_value) for
              exch_curr_key, exch_curr_value in EXCHANGE_CURRS_BTN_TEXTS.items())
        ),
        state=BuyMenuSG.choose_to_change_currency,
        getter=get_my_currency,
    ),

    Window(
        Multi(
            Format("💸 Ваша валюта - {my_currency_text}"),
            Format("💱 Валюта для обмена - {exchange_currency}"),
            Format("🏷️ Введите сумму для обмена ({my_currency_text}):"),
            sep='\n\n',
        ),
        MessageInput(
            func=input_my_curr_handler,
            content_types=ContentType.TEXT,
        ),
        getter=get_all_currs_choice,
        state=BuyMenuSG.input_my_currency_value,
    ),

    Window(
        Multi(
            Format("💸 Ваша валюта - {my_currency_text}"),
            Format("💱 Валюта для обмена - {exchange_currency_text}"),
            Format("🏷️ Сумма для обмена - {my_currency_value} ({my_currency_text}):"),
            Format("📝 Вы получите {exchange_curr_value} ({exchange_currency_text})"),
            sep='\n\n',
        ),
        SwitchTo(text=Const('➡️ Продолжить'), id='confirm_inputs_click', state=BuyMenuSG.input_credentials),
        SwitchTo(text=Const('🔁 Ввести заново'), id='restart_input_click', state=BuyMenuSG.choose_my_currency),
        getter=get_my_curr_input_values,
        state=BuyMenuSG.confirm_inputs,
    ),

    Window(
        Const("🔢 Введите реквизиты для получения валюты (адрес кошелька или номер иностранной карты)"),
        MessageInput(
            func=input_credentials_handler,
            content_types=ContentType.TEXT,
        ),
        state=BuyMenuSG.input_credentials,
    ),

    Window(
        Format("💳 Ваши реквизиты: {my_credentials}"),
        SwitchTo(text=Const('➡️ Продолжить'), id='confirm_inputs_click', state=BuyMenuSG.choose_delivery),
        SwitchTo(text=Const('🔁 Ввести заново'), id='restart_input_click', state=BuyMenuSG.input_credentials),
        state=BuyMenuSG.confirm_credentials,
        getter=get_input_credentials,
    ),

    Window(
        Const("🚚 Выберите способ доставки"),
        Next(text=Const("📦 Обычная"), id='standart_delivery_click', on_click=input_delivery_type),
        Next(text=Const("⚡ Быстрая"), id='fast_delivery_click', on_click=input_delivery_type),
        state=BuyMenuSG.choose_delivery,
    ),

    Window(
        Format("{output_credentials}"),
        Next(Const("✅ Я оплатил"), id='user_confirm_payment_click'),
        state=BuyMenuSG.confirm_payment,
        getter=get_operator_credentials,
    ),

    Window(
        Const("📝 Загрузите скриншот оплаты или чек"),
        MessageInput(
            func=input_payment_detals,
            content_types=ContentType.PHOTO,
        ),
        MessageInput(
            func=input_payment_detals,
            content_types=ContentType.DOCUMENT,
        ),
        state=BuyMenuSG.load_cheque,
    ),
    Window(
        Const("⌛ Проводится проверка вашей оплаты. Ожидайте"),
        Button(Const("Личный кабинет"), id='after_payment_to_cabinet_click', on_click=start_to_menu_after_payment),
        MessageInput(
            func=after_payment_to_menu_handler,
            content_types=ContentType.ANY,
        ),
        state=BuyMenuSG.wait_confirmation,
    )
)
