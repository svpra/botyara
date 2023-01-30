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
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)kup)
    
@bot.message_handler(commands=["bye_kitten"])  
def bye(message):
    
bot.polling(none_stop=True)
