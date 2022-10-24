from telegram import Update
import datetime as dt

def log(update: Update, context):
    file = open('bot.log', 'a')
    file.write(f'{dt.datetime.now().strftime("%Y%m%d-%H:%M:%S")}\t{update.effective_user.id}\t{update.effective_user.name}\t{update.effective_user.full_name}\t{context}\n')
    file.close()