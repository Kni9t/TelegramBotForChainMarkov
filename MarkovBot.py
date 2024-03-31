import telebot
import random
from telebot import types
import json
import markovify

bot = telebot.TeleBot('<Bot-key>')

megaString = ""

with open('MarkovModelDict.txt', 'r', encoding='utf-8') as file:
    megaString += file.read()

text_model = markovify.NewlineText(megaString, state_size=3)

def CreateMessage():
    buf = text_model.make_sentence()
    while (buf is None):
        buf = text_model.make_sentence()
    return buf.capitalize()


print("Модель готова!")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Сгенерировать")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Привет! Этот бод позволяет получить небольшое предложение состоящее из случайных слов, собранных из фанфиков! \nP.s. текст совершенно не формотирован и порой будет выходить совсем белиберда хД', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == 'Сгенерировать' :
         bot.send_message(message.chat.id, CreateMessage())
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/start")
        item2=types.KeyboardButton("Сгенерировать")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, "Я не знаю такой команды! Вы можете перезапустить меня, если что-то пошло не так!", reply_markup=markup)

# Запускаем бота
bot.polling(none_stop=True, interval=0)

#https://xakep.ru/2021/11/28/python-telegram-bots/