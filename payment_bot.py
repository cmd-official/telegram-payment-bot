from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from aiogram.utils import executor
import logging

TOKEN = "8117246169:AAESfMHEFdkF-EAkKVZVIqpMjpK56vPbBBA"  # Токен бота из BotFather STRIPE_PROVIDER_TOKEN = "sk_test_51R8OCxPOgO9x9v463D9ZwrzHAVlc0Jj3yLQIx4KOW6qHJ4pwaEj0ZvT8hWaBPy9AMt5W3DvgfqvkG4Z77BOBnLMa00yH5kwfSF"  # Сюда вставь Secret Key из Stripe FILE_PATH = "pay_bot.txt"  # Файл, который бот отправит после оплаты

logging.basicConfig(level=logging.INFO)
bot = Bot(token="ТОКЕН", parse_mode="HTML") # Замените "ТОКЕН" на ваш токен
dp = Dispatcher(bot)

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton("Оплатить", callback_data="buy"))
await message.answer("Нажми на кнопку ниже, чтобы оплатить и получить файл.", reply_markup=markup)

await bot.send_invoice(
    chat_id=call.message.chat.id,
    title="Покупка файла",
    description="После оплаты вы получите файл.",
    payload="file_purchase",
    provider_token=STRIPE_PROVIDER_TOKEN,
    currency="rub",
    prices=[LabeledPrice(label="@айл", amount=500_100)],  # Цена в копейках (500 руб.)
    start_parameter="purchase_file",
    need_name=False, # Исправлено: было Need
    need_phone_number=False, # Исправлено: было Need
    need_email=True, # Исправлено: было Need
    is_flexible=False #Не указан, поэтому добавляю
)

@dp.pre_checkout_query_handler(lambda query: True) async def checkout(pre_checkout_query: PreCheckoutQuery): await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT) async def successful_payment(message: types.Message): await message.answer("✅ Оплата прошла успешно!") with open(FILE_PATH, "rb") as file: await bot.send_document(message.chat.id, file)

if name == "main": executor.start_polling(dp, skip_updates=True)

