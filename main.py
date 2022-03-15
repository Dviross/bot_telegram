import Constants as keys
from telegram import *
from telegram.ext import *
import Responses as R


print("bot started...")
def start_command(update, context):
    buttons=[[KeyboardButton("text1")], [KeyboardButton("text2")], [KeyboardButton("text3")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, im a police bot!", reply_markup=ReplyKeyboardMarkup(buttons))
    # update.message.reply_text('Type something to get started! ')


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
    text = str(update.message.text)
    response = R.first_appearance_buttens(text)

    update.message.reply_text(response)
    # context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, )])




def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, buttens_message))
    #dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()