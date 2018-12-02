from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
import telebot
bot = telebot.TeleBot('734544473:AAE_EP-gB8xp-sEjXBuztWcvgdCJ-qL1pNc')


class UpdateBot(APIView):
    def post(self, request):
        json_string = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return Response({'code': 200})


def start_buttons():
    key = ReplyKeyboardMarkup(True, False)
    button1 = KeyboardButton('About')
    button2 = KeyboardButton('Operation mode')
    button3 = KeyboardButton('Vaccine')
    button4 = KeyboardButton('Drugs and insulin')
    button5 = KeyboardButton('Potranage')
    key.add(button1, button2)
    key.add(button3, button4)
    key.add(button5)
    return key


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hi', reply_markup=start_buttons())