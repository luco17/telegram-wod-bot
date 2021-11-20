import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.callbackcontext import CallbackContext
from wods import get_rowing_wods, wod_dict_to_text, get_ski_wods, get_bike_wods

PORT = int(os.environ.get('PORT', 5000))
BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_NAME = os.environ.get("APP_NAME")

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


def rowing(update, context: CallbackContext):
    rowing_wods = get_rowing_wods()
    wod_text = wod_dict_to_text(rowing_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text)


def ski(update, context: CallbackContext):
    ski_wods = get_ski_wods()
    wod_text = wod_dict_to_text(ski_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text
    )


def bike(update, context: CallbackContext):
    bike_wods = get_bike_wods()
    wod_text = wod_dict_to_text(bike_wods)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=wod_text
    )


row_handler = CommandHandler('row', rowing)
dispatcher.add_handler(row_handler)

ski_handler = CommandHandler('ski', ski)
dispatcher.add_handler(ski_handler)

bike_handler = CommandHandler('bike', bike)
dispatcher.add_handler(bike_handler)

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=BOT_TOKEN)
updater.bot.set_webhook(APP_NAME.join(BOT_TOKEN))
