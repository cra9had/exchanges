from aiogram.fsm.state import StatesGroup, State


class BuyMenuSG(StatesGroup):
    choose_my_currency = State()
    choose_to_change_currency = State()
    input_my_currency_value = State()
