from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/finance?q=HKD"
r = requests.get(url)
soup = BeautifulSoup(r.content)
g_data = soup.find_all('span', {'class': 'bld'})
c = g_data[0].text
"""Set up the Fucking bot"""

bot = TelegramBot('331382532:AAF_VdgQmBf7rxPskV2x3BeswEjbpR7f9b4')
bot.update_bot_info().wait()
print(bot.username)

#result = bot.send_message(user_id,'test message body').wait()
#print(result)
def Rate(bot, update):
    text = '1 HKD = '
    update.message.reply_text(text, c)
updater = Updater('331382532:AAF_VdgQmBf7rxPskV2x3BeswEjbpR7f9b4')

updater.dispatcher.add_handler(CommandHandler('Rate', Rate))
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
updater.start_polling()
