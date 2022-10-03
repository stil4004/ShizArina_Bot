# -*- coding: utf8 -*-
import Texts
import random
import time
import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('')

Hello = ["Привет", "привет", "Хай", "хай"]

HelloFromArina = ["Саламчик малейкумчик", "СалАм АлейКУм", "СаламАлейкуМ"]

Intro = ["Как дела?", "Как дела", "как дела", "как дела?", "сап", "Сап", "Че по планам?", "че по планам?",
         "че по планам", "Че по планам"]

Citats = ["Погуляй)", "ПоДаРОк", "Я в поле, ничего не слышу"]

First = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

Second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

Second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

Third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

GoodNight = ["Спокойной ночи", "спокойной ночи", "Спокойной ночки", "спокойной ночки"]


@bot.message_handler(commands=['start'])
def start(message):
    # Genius menu
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Че')
    item2 = types.KeyboardButton('Бля')
    item3 = types.KeyboardButton('Похуй')
    item4 = types.KeyboardButton('Гадание')
    item5 = types.KeyboardButton('Может по пиву?')
    item6 = types.KeyboardButton('На кого ты похож(по мнению Арины)')
    markup.add(item1, item2, item3, item4, item5)
    markup.add(item6)

    # start
    bot.send_message(message.chat.id, "СалАМ алейкУм")
    bot.send_message(message.chat.id, "Создатели шизы: \n@Trapmaloj feat @qqhich")
    time.sleep(0.8)
    bot.send_message(message.chat.id, "И нахуя ты сюда пришел", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':

        if ("рдр" in message.text) or ("Рдр" in message.text) or ("РДР" in message.text):
            bot.send_message(message.chat.id, "Рдр это как рука.. дьявола…… рука?!")

        elif message.text in Intro:
            bot.send_message(message.chat.id, "Так, что у меня завтра?.. нарушения психического…. да ладно, похуй")

        elif ("завтра" in message.text) or ("Завтра" in message.text):
            bot.send_message(message.chat.id, "Так, что у меня завтра?.. нарушения психического….А, да похуй")

        elif message.text in Hello:
            bot.send_message(message.chat.id, HelloFromArina[randint(0, 2)])

        elif message.text in GoodNight:
            bot.send_message(message.chat.id, "СПАТЬ НХЙ")
            time.sleep(0.8)
            img = open('Arina(GN).jpg', 'rb')
            bot.send_photo(message.chat.id, img)

        elif message.text == 'Че':
            bot.send_message(message.chat.id, "Хуй в очё)))")

        elif message.text == 'Бля':
            bot.send_message(message.chat.id, Citats[randint(0, 2)])

        elif message.text == 'Похуй':
            bot.send_message(message.chat.id, "Спать нахй")
            time.sleep(0.8)
            img = open('Arina(Helmet).jpg', 'rb')
            bot.send_photo(message.chat.id, img)

        elif message.text == 'Гадание':
            bot.send_message(message.chat.id, "В очко себе погадай\n*Карты разряжены*")
            time.sleep(1.2)
            bot.send_message(message.chat.id, "Ладно, так и быть...")
            time.sleep(1.1)
            goroscope = First[randint(0, 4)] + Second[randint(0, 3)] + Second_add[randint(0, 4)] + Third[randint(0, 4)]
            bot.send_message(message.chat.id, goroscope)

        elif message.text == 'Может по пиву?':
            bot.send_message(message.chat.id, "Да не... не....")
            time.sleep(1.3)
            bot.send_message(message.chat.id, "Мы все...")
            time.sleep(1.4)
            bot.send_message(message.chat.id, "Иди чаи погоняй...")

        elif message.text == 'На кого ты похож(по мнению Арины)':
            img = open(f'RandomPhotos/{randint(1, 18)}.jpg', 'rb')
            bot.send_photo(message.chat.id, img)

        else:
            get_user_text(message)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Че')
        item2 = types.KeyboardButton('Бля')
        item3 = types.KeyboardButton('Похуй')
        item4 = types.KeyboardButton('Гадание')
        item5 = types.KeyboardButton('Может по пиву?')
        item6 = types.KeyboardButton('На кого ты похож(по мнению Арины)')
        markup.add(item1, item2, item3, item4, item5)
        markup.add(item6)


@bot.message_handler(content_types=['photo'])
def bot_photo_reaction(message):
    bot.send_message(message.chat.id, "Господи, что эТо")
    time.sleep(1)
    bot.send_message(message.chat.id, "Ночь на дворе все таки...")


def get_user_text(message):
    bot.send_message(message.chat.id, "А… у… э… ой бля… пошел нахуй")


bot.polling(none_stop=True)
