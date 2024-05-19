from aiogram import Router, F, Dispatcher, Bot
from aiogram.types import CallbackQuery, Message

router = Router()


@router.callback_query(F.data.startswith('confirm_payment_'))
async def confirm_payment(callback: CallbackQuery, bot: Bot):
    user_id = callback.data.split('_')[2]
    await callback.message.delete()
    await callback.answer('Платёж подтверждён')
    await bot.send_message(chat_id=user_id, text='✅ Ваш платёж подтверждён.')


@router.callback_query(F.data.startswith('decline_payment_'))
async def decline_payment(callback: CallbackQuery, bot: Bot):
    user_id = callback.data.split('_')[2]
    await callback.message.delete()
    await callback.answer('Платёж отклонён')
    await bot.send_message(chat_id=user_id, text='❌ Ваш платёж отклонён.')
