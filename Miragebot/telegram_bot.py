# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:14:34 2022

@author: pandi
"""
#import logging library to debug the program better

import logging

#Import necessary libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#importing relevant libraries from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import os
import time
os.chdir(r"D:\telegram_bot")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# Start and read commands are created
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, 
    text="I'm a bot, please talk to me!")
    
def read(update, context):

    browser = webdriver.Chrome(os.getcwd() + '\chromedriver.exe')
    browser.get('https://www.outline.com')

    linkbar = browser.find_element_by_id('source')
    linkbar.send_keys(context.args) 
    linkbar.send_keys(Keys.ENTER)

    time.sleep(10)
    context.bot.send_message(chat_id=update.message.chat_id, text=browser.current_url)
    
def main():
   #updater and dispatcher objects created
   updater = Updater(token='5018778507:AAHBd74vwtAYTCx3z-vNmc81ed7bRR08hUE', use_context=True)
   dispatcher = updater.dispatcher
   
   dispatcher.add_handler(CommandHandler('start', start))
   dispatcher.add_handler(CommandHandler('read', read))
   #start the bot
   updater.start_polling()
   #stop
   updater.idle()
   
if __name__ == '__main__':
       main()