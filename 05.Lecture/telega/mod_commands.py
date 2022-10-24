from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime as dt
import mod_log as log

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    await update.message.reply_text(f'{dt.datetime.now().strftime("%Y%m%d-%H:%M:%S")}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    string = update.message.text.split()
    elements = str(string[1]).split("+")
    sum = 0
    for item in elements:
        sum += int(item)
    await update.message.reply_text(f'sum of elements is {sum}')