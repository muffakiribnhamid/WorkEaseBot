import telebot
import pyshorteners
import qrcode
from io import BytesIO


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
   bot.reply_to(message,"Enter Qr Details")

   @bot.message_handler(func=lambda msg: True)
   def make_qr(message):
       try:
           text = message.text
           qr = qrcode.QRCode(
               version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_L,
               box_size=10,
               border=4,
           )
           qr.add_data(text)
           qr.make(fit=True)
           qr_img = qr.make_image(fill_color = 'black', back_color = 'white')

           img_buffer = BytesIO()
           qr_img.save(img_buffer,format="PNG")
           img_buffer.seek(0)

           bot.send_photo(message.chat.id,img_buffer)

       except Exception as e:
           bot.reply_to(message, "Sorry, I couldn't generate the QR code. Please try again.")


bot.polling()
