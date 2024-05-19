from aiogram.fsm.state import StatesGroup, State


class BuyMenuSG(StatesGroup):
    choose_my_currency = State()
    choose_to_change_currency = State()
    input_my_currency_value = State()
    confirm_inputs = State()

    input_credentials = State()
    confirm_credentials = State()

    choose_delivery = State()

    confirm_payment = State()
    load_cheque = State()
    wait_confirmation = State()