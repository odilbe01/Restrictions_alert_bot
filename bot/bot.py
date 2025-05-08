
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import json
import os

with open("image_keywords.json", "r") as f:
    image_db = json.load(f)

def handle_message(update: Update, context: CallbackContext):
    message = update.message.text.upper()
    for keyword in image_db:
        if keyword in message:
            image_path = image_db[keyword]
            if os.path.exists(image_path):
                with open(image_path, "rb") as photo:
                    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
            return

def main():
    updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
