import telebot
from telebot import types

token = "5089459285:AAHW2ZPiWpa3bMbiIbEAkJgpqpXbRqfy90U"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Как поступить в Мтуси?', 'Есть какая-нибудь группа студентов Мтуси?', 'Стоит ли поступать в Мтуси?')
    bot.send_message(message.chat.id, 'Привет! Ты можешь посмотреть мои возможности используя комманду /help',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Что я могу: \n'
                     ' /info - Информация о МТУСИ \n'
                     ' /music - Показывает хороших исполнителей \n'
                     ' /support - Куда обратиться в случае возникновения каких-либо проблем с ботом')


@bot.message_handler(commands=['info'])
def help_message(message):
    bot.send_message(message.chat.id, 'Всю актуальную информацию ты можешь найти на сайте https://mtuci.ru/')


@bot.message_handler(commands=['music'])
def help_message(message):
    bot.send_message(message.chat.id,
                     "Советую послушать таких исполнителей:\nATL, Imagine Dragons, Maroon 5, Eminem, DVRST, Kizaru")


@bot.message_handler(commands=['support'])
def help_message(message):
    bot.send_message(message.chat.id, 'Напишите на почту volkovilya064@gmail.com и опишите вашу проблему')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Как поступить в Мтуси?':
        bot.send_message(message.chat.id,
                         'Вы можете найти всю необходимую информацию для поступления на сайте. \n https://mtuci.ru/')
    if message.text == 'Есть какая-нибудь группа студентов Мтуси?':
        bot.send_message(message.chat.id, 'Конечно есть, например в ВК: \n https://vk.com/aktivist_mtuci')
    if message.text == 'Стоит ли поступать в Мтуси?':
        bot.send_message(message.chat.id, 'Конечно стоит, это один из лучших технических вузов Москвы!')


bot.polling()
