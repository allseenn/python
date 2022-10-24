from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackContext
import datetime as dt

def log(update: Update, context: CallbackContext):
    file = open('bot.log', 'a')
    file.write(f'{dt.datetime.now().strftime("%Y%m%d-%H:%M:%S")} {update.effective_user.first_name} {update._effective_user.id} {update.message.text}\n')
    file.close()