import config
import telebot

token = '6198023279:AAHDStO17E6KuSJl5EL51udBgZDvCS0nweY'

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.reply_to(message, "Привет дружок пирожок, я ботик Пети Первого. Меня создал Uwubewt, svpra и dd")
@bot.message_handler(commands=["bye_kitten"])  
def bye(message):
    photo = open('путь_к_фото', 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=["start_test"])
def send_fucking_nigga_to_sibir(message):
	bot.reply_to(message, "Привет дружок пирожок, я ботик Пети Первого. Меня создал Uwubewt")
	
@bot.message_handler(content_types=["text"])
def rab_niger(message):
    bot.send_message(message.chat.id, message.text)
  
@bot.message_handler(content_types=["text"])  
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)kup)
    
@bot.message_handler(commands=["bye_kitten"])  
def bye(message):
    
bot.polling(none_stop=True)
