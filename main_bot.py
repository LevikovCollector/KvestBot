from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import os
from dotenv import load_dotenv

class Bot():
    def __init__(self):

        updater = Updater(os.getenv('TELEGRAM_TOKEN'),use_context=True)
        self.quiz_stage = 1

        dispacher = updater.dispatcher
        dispacher.add_handler(CommandHandler("start", self.greet_user))
        dispacher.add_handler(CallbackQueryHandler(self.buttons))
        dispacher.add_handler(MessageHandler(Filters.text, self.listen_user))

        updater.start_polling()
        updater.idle()

    def greet_user(self, update,context):
        keyboard = [[InlineKeyboardButton("GO!", callback_data='1')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        with open('img/greet.jpg', 'rb') as img:
            update.message.reply_text('Hello!', reply_markup=reply_markup)
            update.message.reply_photo(photo=img)
        # self.chat_id = update['chat']['id']
        self.update = update

    def listen_user(self, update, context):
        print(update)
        text_from_user = update.message.text
        update.message.reply_text(f'Вы написали: {text_from_user}')

    def question_1(self):
        keyboard = [
            [
                InlineKeyboardButton("Option 1", callback_data='1'),
                InlineKeyboardButton("Option 2", callback_data='2'),
                InlineKeyboardButton("Option 2", callback_data='2'),
            ],
            [InlineKeyboardButton("Option 3", callback_data='3')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        self.update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def buttons(self, update, bot):
        if update.callback_query['data']:
            self.question_1()

if __name__ == '__main__':
    load_dotenv(dotenv_path='.env')
    bot = Bot()

