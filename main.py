import telebot
from database import init_db, get_user, create_user, increment_free_tips

# 🔑 Токен твоего бота
BOT_TOKEN = 8367412487:AAGjIRskfVmvhPU94HE7G_fHS9UBxEux5m4
bot = telebot.TeleBot(BOT_TOKEN)

# Инициализация базы при запуске
init_db()

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not get_user(user_id):
        create_user(user_id)
    bot.reply_to(
        message,
        "Bonjour! 👋 Я — ваш универсальный помощник.\n"
        "Напишите любой запрос.\n"
        "Первые 2 совета — бесплатно! 🎁"
    )

@bot.message_handler(func=lambda m: True)
def handle_request(message):
    user_id = message.from_user.id
    user = get_user(user_id)
    
    if not user:
        create_user(user_id)
        user = (user_id, 0, 0)

    free_used = user[1]

    if free_used < 2:
        tips = [
            "💡 Совет 1: Сделайте глубокий вдох на 4 секунды, задержите дыхание на 4, выдохните на 6. Повторите 3 раза.",
            "💡 Совет 2: Напишите 3 вещи, за которые вы благодарны сегодня. Это снижает тревожность."
        ]
        bot.reply_to(message, tips[free_used])
        increment_free_tips(user_id)
        
        if free_used + 1 == 2:
            bot.send_message(
                user_id,
                "Вы использовали все бесплатные советы. 🎉\n"
                "Хотите продолжить? Напишите /subscribe для подписки!"
            )
    else:
        bot.reply_to(
            message,
            "🔒 Подписка требуется.\n"
            "Напишите /subscribe, чтобы узнать, как получить доступ к полной версии."
        )

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    bot.reply_to(
        message,
        "✨ Подписка скоро будет доступна через Telega-100!\n"
        "Вы получите:\n"
        "• Неограниченные советы\n"
        "• Генерацию изображений\n"
        "• Персональную поддержку\n\n"
        "Следите за обновлениями! 💌"
    )

if name == 'main':
    print("✅ Бот запущен и работает 24/7...")
    bot.infinity_polling()
