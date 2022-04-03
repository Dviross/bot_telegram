# from enum import Enum
#
# import Keyboards as KB
# from telegram.ext import *
#
# import Constants as keys
# import Responses as R
#
#
#
# print("bot started...")
#
#
# class keyboard_mode(Enum):
#     START_KEYBOARD = 1
#     POW_KEYBOARD = 2
#     ADMIN_KEYBOARD = 3
#
#
# def start_command(update, context):
#     KB.set_start_Keyboard(update, context)
#     update.message.reply_text('Type something to get started! ')
#
#
# def help_command(update, context):
#     update.message.reply_text('Type to get started! ')
#
#
# def error(update, context):
#     print(f"update {update} caused error {context.error}")
#
#
# def handle_message(update, context):
#     text = str(update.message.text).lower()
#     response = R.sample_responses(text)
#
#     update.message.reply_text(response)
#
#
# def buttens_message(update, context, flag_keyboard):
#     text = str(update.message.text).lower()
#     arr_response = R.first_appearance_buttens(text)
#
#     if (arr_response):
#         for i in arr_response:
#             update.message.reply_text(i)
#
#     if text == "back to start menu":
#         KB.set_start_Keyboard(update, context)
#         flag_keyboard = keyboard_mode.START_KEYBOARD
#     if text in ("text3", "back to pow menu"):
#         KB.set_POW_keyBoard(update, context)
#         flag_keyboard = keyboard_mode.POW_KEYBOARD
#     if (text == "pow!3"):
#         KB.set_admin_keyBoard(update, context)
#         flag_keyboard = keyboard_mode.ADMIN_KEYBOARD
#         if text == "חזור":
#             match flag_keyboard:
#                 case keyboard_mode.POW_KEYBOARD:
#                     KB.set_start_Keyboard(update, context)
#                 case keyboard_mode.ADMIN_KEYBOARD:
#                     KB.set_POW_keyBoard(update, context)
#
#
# def main(flag_keyboard):
#     updater = Updater(keys.API_KEY, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(CommandHandler("help", help_command))
#
#     dp.add_handler(MessageHandler(Filters.text, buttens_message(flag_keyboard=flag_keyboard)))
#     dp.add_handler(MessageHandler(Filters.text, handle_message))
#
#     dp.add_error_handler(error)
#
#     updater.start_polling()
#     updater.idle()
#
#
# main(flag_keyboard = flag_keyboard)


import Keyboards as KB
from telegram import *
from telegram.ext import *

import Constants as keys
import Responses as R

print("bot started...")


def start_command(update, context):
    KB.set_start_Keyboard(update, context)
    update.message.reply_text('Type something to get started! ')


def help_command(update, context):
    update.message.reply_text('Type to get started! ')


def error(update, context):
    print(f"update {update} caused error {context.error}")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def buttens_message(update, context):
    # image =
    text = str(update.message.text).lower()
    arr_response = R.first_appearance_buttens(text)

    if (arr_response):
        for i in arr_response:
            update.message.reply_text(i)

    if text == "back to start menu":
        KB.set_start_Keyboard(update, context)
    if text in ("text3", "back to pow menu"):
        KB.set_POW_keyBoard(update, context)
    if (text == "pow!3"):
        KB.set_admin_keyBoard(update, context)
    # context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, )])
    if (text == "gif"):
        flyButtons = [[InlineKeyboardButton("👍", callback_data="like")],
                      [InlineKeyboardButton("👎", callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(flyButtons),
                                 text="Do you like the gif?")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, buttens_message))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
