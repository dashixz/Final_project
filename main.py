import telebot
token=""

bot=telebot.TeleBot(token)

import random
from telebot import types
f = open('text.txt', 'r', encoding='UTF-8')
texthelp = f.read().split('\n')
f.close()
f = open('image.txt', 'r', encoding='UTF-8')
imagehelp = f.read().split('\n')
f.close()
f = open('video.txt', 'r', encoding='UTF-8')
videohelp = f.read().split('\n')
f.close()
f = open('research.txt', 'r', encoding='UTF-8')
researchhelp = f.read().split('\n')
f.close()
f = open('presentation.txt', 'r', encoding='UTF-8')
presentationhelp = f.read().split('\n')
f.close()
f = open('design.txt', 'r', encoding='UTF-8')
designhelp = f.read().split('\n')
f.close()

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Text")
        item2 = types.KeyboardButton("Image")
        item3 = types.KeyboardButton("Video")
        item4 = types.KeyboardButton("Research")
        item5 = types.KeyboardButton("Presentation")
        item6 = types.KeyboardButton("Design")

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        bot.send_message(m.chat.id, 'Hi! Im here to help u with ur study problems. Here some sites and programs that might help u: \nPress text for help with text \nPress image for help with images\nPress for help with\nPress for help with\nPress for help with\nPress for help with\nPress for help with ',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Text' :
            answer = random.choice(texthelp)
    elif message.text.strip() == 'Image':
            answer = random.choice(imagehelp)
    elif message.text.strip() == 'Video':
            answer = random.choice(videohelp)
    elif message.text.strip() == 'Research':
            answer = random.choice(researchhelp)
    elif message.text.strip() == 'Presentation':
            answer = random.choice(presentationhelp)
    elif message.text.strip() == 'Design':
            answer = random.choice(designhelp)
    bot.send_message(message.chat.id, answer)

bot.polling()