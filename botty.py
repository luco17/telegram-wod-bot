"""
Runs the bot
"""
import os
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.callbackcontext import CallbackContext
from wods import get_rowing_wods, wod_dict_to_text, get_ski_wods, get_bike_wods

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_NAME = os.environ.get("APP_NAME")
PORT = int(os.environ.get('PORT', 5000))


def start(update: Update, context: CallbackContext):
    """Sends a message when /start is issued"""
    user = update.effective_user
    welcome_text = (f"Hi {user.first_name}, welcome to the WOD bot.\n\n"
                    "You can use three commands to get the daily C2 WOD:\n\n"
                    "/ski\n/row\n/bike\n\nHappy training!")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome_text)


def rowing(update, context: CallbackContext):
    """Rowing wod getter"""
    rowing_wods = get_rowing_wods()
    wod_text = wod_dict_to_text(rowing_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text)


def ski(update, context: CallbackContext):
    """Ski wod getter"""
    ski_wods = get_ski_wods()
    wod_text = wod_dict_to_text(ski_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text
    )


def bike(update, context: CallbackContext):
    """Bike wod getter"""
    bike_wods = get_bike_wods()
    wod_text = wod_dict_to_text(bike_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text
    )


def main():
    """start the bot"""
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler('row', rowing))
    dispatcher.add_handler(CommandHandler('ski', ski))
    dispatcher.add_handler(CommandHandler('bike', bike))

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=BOT_TOKEN)

    updater.bot.setWebhook(APP_NAME+BOT_TOKEN)

    updater.idle()


if __name__ == "__main__":
    main()
