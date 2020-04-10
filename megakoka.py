import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('1023733994:AAFCmwj-kiOfOW57APcXvZqnyBWCZnOMiBU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI-hl6JrcYcXMNK-Hlb3ItPeqCgPFzqAALqAgACtXHaBr_PemH5zBx1GAQ')
    bot.send_message(message.chat.id, 'Йо, {0.first_name}!\nЯ живой. '.format(message.from_user, bot.get_me(), parse_mode="html"))
    
@bot.d_handler(content_types=['text'])
def send_text(message):        
    if message.text.lower() in fck_list:
        i = 1
        while (i < 5):
            bot.send_message(message.chat.id, '🖕🏾')
            i += 1
                
        else:
            bot.send_message(message.chat.id, '{0.first_name}! Иди на хуй' .format(message.from_user, bot.get_me(), parse_mode="html"))
                

@bot.message_handler(content_types=['text'])
def send_text(message):
    fck_list = ["🖕","🖕🏻","🖕🏼","🖕🏽","🖕🏾","🖕🏿"] #tralling
    fst_list = ["🤛","🤛🏻","🤛🏼","🤛🏽","🤛🏾","🤛🏿"] #tralling
    ape_list = ["🙈","🙉","🙊","🐵","🐒"] #tralling
    daddy_list =["кто тебя создал?","кто твой создатель?","кто твой отец?","кто твой папочка?"]
    hi_list = ["привет","здарова","здорова","йо","сап","здравствуй"]
    hian_list = ["Йо","Ну привет","Здарова","Привет","Сап"]
    if message.text.lower() in hi_list:
        bot.send_message(message.chat.id, str(random.choice(hian_list)))
    
    elif message.text.lower() in fst_list:
        bot.send_message(message.chat.id, '🤜🏾')
                
    elif message.text.lower() == "эски":
        bot.send_message(message.chat.id, str(random.choice(ape_list)))              
        
    elif message.text.lower() in daddy_list:
        bot.send_message(message.chat.id, '@e_rocket')
        
    elif message.text.lower() == "тиай":
        sti = open('static/sticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)        
        
    else:
        bot.send_message(message.chat.id, 'Чо каво, сучара!?')
        
bot.polling( none_stop = True) 
