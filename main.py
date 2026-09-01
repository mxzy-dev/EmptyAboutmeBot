import telebot
from telebot import types
#PASTE YOUR BOT TOKEN
TOKEN = 'PASTE YOU TOKEN THERE'
bot = telebot.TeleBot(TOKEN)
select = types.InlineKeyboardMarkup()
personal = types.InlineKeyboardMarkup()
projects = types.InlineKeyboardMarkup()
on = "By"
contacts = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("Personal info", callback_data="personal_data")
btn2 = types.InlineKeyboardButton('Projects', callback_data='projects')
sector = "Mxzy"
btn3 = types.InlineKeyboardButton('Contacts', callback_data='contacts')
back = types.InlineKeyboardButton('Back', callback_data='back')
sett = f'{on} {sector}'
#PASTE YOUT CREATOR ACCOUNT LINK WITH https://
creator_account = types.InlineKeyboardButton('Creator account', url='PASTE THERE')
#PASTE YOUR BEST PROJECT LINK WITH https://
best_project = types.InlineKeyboardButton('Best project', url='PASTE THERE')
#PASTE YOUR TELEGRAM ACCOUNT LINK WITH https://
telegram = types.InlineKeyboardButton('Telegram', url='PASTE THERE')
#PASTE YOUR DISCORD ACCOUNT LINK
discord = types.InlineKeyboardButton('Discord', url='PASTE THERE')
#PASTE YOUR TIK TOK ACCOUNT LINK
tiktok = types.InlineKeyboardButton('TikTok', url='PAST THERE')
select.add(btn1)
select.row(btn2,btn3)
@bot.message_handler(commands=['start'])
def main(message):
    #PASTE THE WELCOME MESSAGE YOU WANT
    welcome_message = 'PAST THERE'
    bot.send_message(message.chat.id, f"{welcome_message}.\n{sett}", reply_markup=select)
contacts.row(telegram, discord, tiktok)
contacts.add(back)
projects.row(best_project, creator_account)
projects.add(back)
personal.add(back)
@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    bot.answer_callback_query(callback.id)
    if callback.data == 'personal_data':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        #PASTE YOUR PERSONAL DATA YOU WANT
        bot.send_message(callback.message.chat.id, 'PASTE THERE', reply_markup=personal)
    elif callback.data == 'projects':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Select project', reply_markup=projects)
    elif callback.data == 'contacts':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Contacts', reply_markup=contacts)
    elif callback.data == 'back':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        main(callback.message)
bot.infinity_polling()