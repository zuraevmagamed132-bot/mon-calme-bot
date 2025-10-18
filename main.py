import telebot
from database import init_db, get_user, create_user  # Импортируем только необходимые функции

# Токен вашего бота (замените на реальный или используйте переменную окружения)
BOT_TOKEN =  "8367412487:AAGjIRskfVmvhPU94HE7G_fHS9UBxEux5m4" # Для примера, лучше хранить в env
bot = telebot.TeleBot(BOT_TOKEN)

# Инициализация базы данных (если модуль database.py отсутствует, используем временное решение)
try:
    init_db()
except NameError:
    # Простая замена, если database.py не настроен
    users = {}  # Временная "база" пользователей
    def init_db():
        pass  # Пустая инициализация для теста
    def get_user(user_id):
        return users.get(user_id)
    def create_user(user_id):
        users[user_id] = {"tips": 0}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not get_user(user_id):  # Проверяем, есть ли пользователь
        create_user(user_id)  # Создаём нового, если нет
    bot.reply_to(message, "Привет! 😄 — ваш универсальный помощник.\nНапишите любой запрос...")

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    if user:
        bot.reply_to(message, f"Вы написали: {message.text}")
    else:
        bot.reply_to(message, "Сначала используйте /start, чтобы начать!")

# Запуск бота
if name == "main":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
