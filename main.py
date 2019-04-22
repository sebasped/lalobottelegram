#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:51:59 2019

@author: sebas
"""

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
import requests
#import re
from datetime import date
from dateutil.relativedelta import relativedelta

#from functools import wraps

#def send_typing_action(func):
#    """Sends typing action while processing func command."""

#    @wraps(func)
#    def command_func(update, context, *args, **kwargs):
#        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
#        return func(update, context,  *args, **kwargs)
#
#    return command_func


def laloEnemigo(bot, update):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
#    return url

def laloAmigo(bot, update):
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['file']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def lalo(bot, update):
    url = "https://cloud.disroot.org/s/2SP5JeCqNdpLbrn"
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

#@send_typing_action
def laloHabla(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=chat_id, text="Miaauuuuu")
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    bot.send_voice(chat_id=chat_id, voice=open('./catmiau.mp3', 'rb'))
#    bot.send_audio(chat_id=chat_id, audio=open('/home/sebas/hacking/gits/telegramBot/catmiau.mp3', 'rb'))
#    pass
    
def laloEdad(bot, update):
    chat_id = update.message.chat_id
    now = date.today()
    birthdate = date(2018, 1, 15)
    rdelta = relativedelta(now, birthdate)
    rdeltaGato = rdelta*7
    bla = 'Soy Lalo y tengo '+str(rdelta.years)+' año, '+str(rdelta.months)+' meses y '+str(rdelta.days)+u' días. Pero en edad de gato tengo '+str(rdeltaGato.years)+' años, '+str(rdeltaGato.months)+' meses y '+str(rdeltaGato.days)+u' días.'
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)    
    bot.send_message(chat_id=chat_id, text=bla)
    #print 'Age in days - ', rdelta.days
    
    

def main():
    updater = Updater('824466032:AAE_GTMQZrKddCNFiC8mzVGGphvyQWnYgjI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('lalo',lalo))
    dp.add_handler(CommandHandler('lalohabla',laloHabla))
    dp.add_handler(CommandHandler('laloedad',laloEdad))
    dp.add_handler(CommandHandler('laloenemigo',laloEnemigo))
    dp.add_handler(CommandHandler('laloamigo',laloAmigo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()