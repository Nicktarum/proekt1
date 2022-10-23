import telebot
import urllib
import urllib.request
from telebot import types
import requests
import math
import random
from collections import Counter
k = 0

# Создаем экземпляр бота
bot = telebot.TeleBot('5504385632:AAG-yqQZFXIwxhBV3WdjXcxAApIjqAEtI30');
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем пять кнопок
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Сыграть в города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Выберите действия',  reply_markup=markup)

def k1(a,b,c,l):
    ur= b ** 2 - 4 * a * c
    if ur>0:
        x1= (-b + math.sqrt(ur)) / (2 * a)
        x2= (-b - math.sqrt(ur)) / (2 * a)
        x3="Первый корень "+ str(x1)+" Второй корень "+ str(x2)
        bot.send_message(l, x3)
    elif ur==0:
        x= -b / (2 * a)
        x3="Корень "+ str(x)
        bot.send_message(l, x3)
    else:
        bot.send_message(l, "Корней нет")

def k2(a,b,c,l):
    f = ""
    if (a == 1) and (b == 2) and (c == 3):
        f = f + "не существует треугольника"
    elif (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
        f = f + "Прямоугольный треугольник"
    elif (c**2 < a**2 + b**2) or (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2):
        f = f + "остроугольный треугольник"
    elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
        f = f + "тупоугольный треугольник"
    else:
        f = f + "не существует треугольника"
    bot.send_message(l, f)

def k3(a,l):
    b = bin(a)
    c = oct(a)
    d = hex(a)
    b = b[2:len(b)]
    c = c[2:len(c)]
    d = d[2:len(d)]
    f = "Двоичная система "+ b +", восьмиричная система " + c + ", шестнадцатиричная система " + d
    bot.send_message(l, f)

def k4(a,l):
    b = a[2:len(a)-2]
    b = dict(Counter(b))
    bot.send_message(l, b)

def k5(l):
    
    cityes =[]
   
    for i in range(len(cityes)):
        if cityes[i][-1] == "\n":
            cityes[i] = cityes[i][:-1]
    cityesall = cityes.copy()
    game_over = False
    city = city[2:len(city)-2]
    cend = city[-1]

    bot.send_message(l, e)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global k
    if k == 1:
        a=message.text.split()
        k1(float(a[0]),float(a[1]),float(a[2]),message.chat.id)
        k = 0
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Название случайного города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите действия',  reply_markup=markup)
    if message.text == "Решить квадратные уравнение":
        bot.send_message(message.chat.id, "Введите параметры a,b,c в уравнении ax^2 + bx + c = 0")
        k = 1
    if k == 2:  
        a=message.text.split()
        k2(float(a[0]),float(a[1]),float(a[2]),message.chat.id)
        k = 0
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Название случайного города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите действия',  reply_markup=markup)
    if message.text == "Найти какой треугольник":
        bot.send_message(message.chat.id, "Введите стороны треугольника a,b,c")
        k = 2
    if k == 3:
        a=message.text
        k3(int(a),message.chat.id)
        k = 0
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Название случайного города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите действия',  reply_markup=markup)
    if message.text == "Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления":
        bot.send_message(message.chat.id, "Введите десятичное число a")
        k = 3
    if k == 4:
        a=message.text.split()
        k4(str(a),message.chat.id)
        k = 0
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Название случайного города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите действия',  reply_markup=markup)
    if message.text == "Найти первый дублированный символ в строке":
        bot.send_message(message.chat.id, "Введите список")
        k = 4
    if k == 5:
        k5(message.chat.id)
        k = 0
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Решить квадратные уравнение")
        item2=types.KeyboardButton("Найти какой треугольник")
        item3=types.KeyboardButton("Перевод из десятичной в двоичную, восмиричную и шестнатцатиричную систему счисления")
        item4=types.KeyboardButton("Найти первый дублированный символ в строке")
        item5=types.KeyboardButton("Название случайного города")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите действия',  reply_markup=markup)
    if message.text == "Название случайного города":
        file1 = open("input.txt")
        cityes=[]
        for i in file1:
                cityes.append(i)
        mm=random.randint(0,len(cityes)-1)
        t="Город " + cityes[mm]
        bot.send_message(message.chat.id, t)
        k = 5
        
# Запускаем бота

bot.polling(none_stop=True, interval=0)
