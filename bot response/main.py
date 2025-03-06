import telebot

# замени 'YOUR TOKEN' на токен твоего бота
bot = telebot.TeleBot('')

# укажи свой chat_id
your_chat_id = ''

# создадим временное хранилище для сообщений
user_messages = {}

# Словарь для хранения user_id пользователей
user_ids = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Сохраняем user_id отправителя
    user_ids[message.from_user.username] = message.from_user.id if message.from_user.username else message.from_user.id
    bot.reply_to(message, 'Привет! Пиши сюда, я пересылаю сообщения админу. Используй команду /send @username текст, чтобы отправить сообщение пользователю.')

@bot.message_handler(commands=['send'])
def send_message_to_user(message):
    try:
        # Разделяем команду на части
        parts = message.text.split(' ', 2)
        if len(parts) < 3:
            bot.reply_to(message, 'Использование: /send @username текст')
            return
        
        username = parts[1].lstrip('@')  # Удаляем символ "@" из юзернейма
        text = parts[2]

        # Проверяем, есть ли user_id в словаре
        if username in user_ids:
            user_id = user_ids[username]
            # Получаем юзернейм отправителя или используем имя/ID
            sender_username = message.from_user.username or message.from_user.first_name or str(message.from_user.id)
            # Формируем сообщение с юзернеймом отправителя
            full_message = f'Сообщение от @{sender_username}: {text}' if message.from_user.username else f'Сообщение от {sender_username}: {text}'
            bot.send_message(user_id, full_message)
            bot.reply_to(message, f'Сообщение отправлено {username}: {text}')
        else:
            bot.reply_to(message, f'Пользователь @{username} не найден. Убедитесь, что он начал диалог с ботом.')
    except Exception as e:
        bot.reply_to(message, f'Ошибка: {str(e)}')

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    # Сохраняем user_id и юзернейм отправителя, если его еще нет в словаре
    if message.from_user.username:
        user_ids[message.from_user.username] = message.from_user.id
    else:
        user_ids[str(message.from_user.id)] = message.from_user.id  # Используем ID, если юзернейм отсутствует

    # Пересылаем сообщение админу с указанием юзернейма отправителя
    sender_username = message.from_user.username or message.from_user.first_name or str(message.from_user.id)
    full_message = f'Сообщение от @{sender_username}: {message.text}' if message.from_user.username else f'Сообщение от {sender_username}: {message.text}'
    bot.send_message(your_chat_id, full_message)


bot.polling()
