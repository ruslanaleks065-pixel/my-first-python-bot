import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен вашего бота, полученный у @BotFather
TOKEN = "8872471464:AAGdKIRXl1ucifGGYUza7xr_1tQmAJyVr0Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
@dp.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новичок", callback_data="level_easy")],
        [InlineKeyboardButton(text="Профи", callback_data="level_hard")]
    ])
    await message.answer("Привет! Выбери свой уровень:", reply_markup=kb)

# Ветвление: Обработка выбора уровня
@dp.callback_query(F.data.startswith("level_"))
async def choose_level(callback: types.CallbackQuery):
    if callback.data == "level_easy":
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="print('Hello')", callback_data="ans_correct")],
            [InlineKeyboardButton(text="echo 'Hello'", callback_data="ans_wrong")]
        ])
        await callback.message.answer("Как вывести текст в консоль Python?", reply_markup=kb)
    else:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Декоратор", callback_data="ans_correct")],
            [InlineKeyboardButton(text="Класс", callback_data="ans_wrong")]
        ])
        await callback.message.answer("Что оборачивает функцию, расширяя её поведение?", reply_markup=kb)
    await callback.answer()

# Логическое завершение
@dp.callback_query(F.data.startswith("ans_"))
async def final_result(callback: types.CallbackQuery):
    if callback.data == "ans_correct":
        text = "Верно! Отличная работа."
    else:
        text = "Неверно. Попробуй еще раз, введя /start."
    await callback.message.answer(text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())