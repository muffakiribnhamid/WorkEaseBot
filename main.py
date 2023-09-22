import os
import telebot
import pyshorteners

BOT_TOKEN = '6464105034:AAGhDtxN24TU5HAN1REKQBt1ZwJZrhkxRio'

bot = telebot.TeleBot(BOT_TOKEN)
s = pyshorteners.Shortener()


@bot.message_handler(commands=['start', 'hello', 'hi'])
def send_welcome(message):
    bot.reply_to(message,"Asalamualikum, How are You Doing? \nHere are Commands \n1:/shortenLink \n2:/qrcodeGen")

@bot.message_handler(commands=['shortenLink'])
def sendQr(message):
    bot.reply_to(message,"Enter Your Link")

    @bot.message_handler(func=lambda msg: True)
    def shorten_link(message):
        try:
            original_url = message.text
            shortened_url = s.tinyurl.short(original_url)
            bot.reply_to(message,f"Here Is Your Link: {shortened_url}")
        except Exception as e:
            bot.reply_to('Sorry Having Some Server Issues Come Back Later ):')

@bot.message_handler(commands=['qrcodeGen'])
def sendQr(message):
   bot.reply_to(message,"Hello World")


bot.polling()
