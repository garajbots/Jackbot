import jconfig
import telebot
import random
import re

def listener(messages):
    for m in messages:
        if m.text == 'Джек' or m.text == 'джек':
            bot.send_message(m.chat.id, random.choice([line for line in open('slovar.txt', 'r')]).encode('cp1251')[:-1])
        elif re.search(r"[Сс]колько [Дд]жека", m.text):
            bot.send_message(m.chat.id, 'Цитат Джека в словаре - ' + str(len(open('slovar.txt', 'r').readlines())))

if __name__ == '__main__':
     bot = telebot.TeleBot(jconfig.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)