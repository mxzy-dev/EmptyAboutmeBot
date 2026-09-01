import telebot
from telebot import types

TOKEN = 'PASTE YOU TOKEN THERE'
CREATOR_ACCOUNT = 'PASTE LINK'
BEST_PROJECT = 'PASTE LINK'
TELEGRAM = 'PASTE LINK'
DISCORD = 'PASTE LINK'
TIKTOK = 'PASTE LINK'
WELCOME = 'PASTE WELCOME MESSAGE YOU WANT'
DATA = 'PASTE THERE DATA YOU WANT'

bot = telebot.TeleBot(TOKEN)
select = types.InlineKeyboardMarkup()
personal = types.InlineKeyboardMarkup()
projects = types.InlineKeyboardMarkup()
on = "By"
contacts = types.InlineKeyboardMarkup()
personalinfo = types.InlineKeyboardButton("Personal info", callback_data="personal_data")
proj = types.InlineKeyboardButton('Projects', callback_data='projects')
sector = "Mxzy"
cont = types.InlineKeyboardButton('Contacts', callback_data='contacts')
back = types.InlineKeyboardButton('Back', callback_data='back')
sett = f'{on} {sector}'
creator_account = types.InlineKeyboardButton('Creator account', url=CREATOR_ACCOUNT)
best_project = types.InlineKeyboardButton('Best project', url=BEST_PROJECT)
telegram = types.InlineKeyboardButton('Telegram', url=TELEGRAM)
discord = types.InlineKeyboardButton('Discord', url=DISCORD)
tiktok = types.InlineKeyboardButton('TikTok', url=TIKTOK)
select.add(personalinfo)
select.row(proj,cont)
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"{WELCOME}.\n{sett}", reply_markup=select)
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
        bot.send_message(callback.message.chat.id, DATA, reply_markup=personal)
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