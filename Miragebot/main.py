# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:34:35 2022

@author: pandi
"""
import constants as keys
from telegram.ext import *

import responses_mirage as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Hello Wanderer! Type ""help"" to get more Mirage related detailes")
    
def help_command(update, context):
    help_description = f"""Welcome to Mirage market. Please the following command to get the desired info: {os.linesep}contract: Use this command to get the contract address {os.linesep}doc: Use this command to get the notion documnetation of Mirage project {os.linesep}website: Use this command to get the website link {os.linesep}chart: Use this command to get the link of Mirage chart on dexscreener {os.linesep}buy: Use this command to get the buy link on duneswap {os.linesep}lp: Use this command to get the link for the LP contract {os.linesep}
    """
    update.message.reply_text(help_description)

def contract(update, context):
    update.message.reply_text("Mirage contract address: 0xFb83B2c9f65f92937fd8798Acf8A79571b864273")

def doc(update, context):
    update.message.reply_text("Here is the documentation link: {os.linesep}https://zenith-aries-078.notion.site/Mirage-Labs-0178eb74ff3145d09e53eaad2a5fa2c6")

def website(update, context):
    update.message.reply_text("Check out Mirage's website: https://www.mirage.market/")

def chart(update, context):
    update.message.reply_text("Realtime price chart for Miragon dexscreener")

def buy(update, context):
    update.message.reply_text("Hello Wanderer! Type ""help"" to get more Mirage related detailes")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.bot_responses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")
   
def main():
    
    updater = Updater(keys.API_KEY, use_context = True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("bot", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    dispatcher.add_error_handler(error)
    
    updater.start_polling()
    
    updater.idle()
    
if __name__ == '__main__':
       main()