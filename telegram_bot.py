# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:14:34 2022

@author: pandi
"""
#import logging library to debug the program better

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#Import necessary libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


updater = Updater(token='5018778507:AAHBd74vwtAYTCx3z-vNmc81ed7bRR08hUE', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, 
    text="I'm a bot, please talk to me!")
    
dispatcher.add_handler(CommandHandler('start', start))

