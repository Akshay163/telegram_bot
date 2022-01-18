# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:29:05 2022

@author: pandi
"""
from datetime import datetime

def bot_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("time", "time?"):
        
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        
        return str(date_time)
    
    return("I don't understand. Please check your input.")