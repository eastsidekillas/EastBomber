import telebot

bot = telebot.TeleBot('5020437807:AAEDNUixZ44Hoza1vqADTRqNoMFVQdGyvGY')


@bot.message_handler(commands=['help'])
def start(message):
    help = 'Для старта бота напишите /bomber'
    bot.send_message(message.chat.id, help)


number = ''
time = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/bomber':
        bot.send_message(message.from_user.id, 'Введите номер цели:')
        bot.register_next_step_handler(message, get_number)
    else:
        bot.send_message(message.from_user.id, 'Введите /bomber или /help')


def get_number(message):
    global number
    number = message.text
    bot.send_message(message.from_user.id, 'Введите время атаки:')
    bot.register_next_step_handler(message, get_time)


def get_time(message):
    global time
    time = message.text
    time_integer = int(time)
    time = time_integer
    main()


def main():
    threads = 4
    from SMS.main import SMS_ATTACK
    SMS_ATTACK(threads, time, number)


bot.polling()