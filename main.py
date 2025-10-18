import telebot
import os

# Импорты для базы данных (с обработкой ошибок)
try:
    from database import init_db, get_user, create_user
except ImportError:
    # Временная реализация, если database.py отсутствует
    users = {}
    def init_db():
        pass
    def get_user(user_id):
        return users.get(user_id)
    def create_user(user_id):
        users[user_id] = {"tips": 0}

# Токен бота (лучше из переменной окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8367412487:AAGZT0XsLcWWk8TuvhiNFhs8Gcw3xRQ69j8")
bot = telebot.TeleBot(BOT_TOKEN)

# Инициализация
init_db()

# Обработчик /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not get_user(user_id):
        create_user(user_id)
    bot.reply_to(message, "Привет! 😄 — ваш универсальный помощник.\nНапишите любой запрос...")

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    if user:
        bot.reply_to(message, f"Вы написали: {message.text}")
    else:
        bot.reply_to(message, "Сначала используйте /start!")

# Запуск бота
if name == "main":
    print("Бот запускается...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка бота: {e}")
