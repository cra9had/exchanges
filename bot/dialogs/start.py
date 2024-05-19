from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from bot.states.start import StartSG

start_dialog = Dialog(
    Window(
        Const("Добро пожаловать в магазин обмена!"),
        state=StartSG.start,
    ),
)
