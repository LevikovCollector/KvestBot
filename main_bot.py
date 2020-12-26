from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

import os
from dotenv import load_dotenv

class Bot():
    def __init__(self):

        updater = Updater(os.getenv('TELEGRAM_TOKEN'),use_context=True)
        self.quiz_stage = 1

        dispacher = updater.dispatcher
        dispacher.add_handler(CommandHandler("start", self.greet_user))
        dispacher.add_handler(MessageHandler(Filters.text, self.listen_user))

        updater.start_polling()
        updater.idle()

    def greet_user(self, update,context):
        img_greet = open('img/greet.jpg', 'rb')
        update.message.reply_text('Hello!')
        update.message.reply_photo(photo=img_greet)

    def listen_user(self, update, context):
        text_from_user = update.message.text
        update.message.reply_text(f'Вы написали: {text_from_user}')


if __name__ == '__main__':
    load_dotenv(dotenv_path='.env')
    bot = Bot()

