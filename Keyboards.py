from telegram import *

def set_start_Keyboard(update, context):
    buttons = [[KeyboardButton("text1")], [KeyboardButton("text2")], [KeyboardButton("text3")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="start kryboard",
                             reply_markup=ReplyKeyboardMarkup(buttons, True))

def set_POW_keyBoard(update, context):
    buttons = [[KeyboardButton("POW!1")], [KeyboardButton("POW!2")], [KeyboardButton("POW!3")],
               [KeyboardButton("gif")], [KeyboardButton("back to start menu")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="POW menu",
                             reply_markup=ReplyKeyboardMarkup(buttons, True))


def set_admin_keyBoard(update, context):
    buttons = [[KeyboardButton("אדמין")], [KeyboardButton("כפרע")], [KeyboardButton("back to POW menu")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="כפרע menu:",
                             reply_markup=ReplyKeyboardMarkup(buttons, True))
