from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mod_commands

with open ('D:\Documents\Bots\GBpyBot.txt', 'r') as file:
        TOKEN = file.readline()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("hello", mod_commands.hello))
app.add_handler(CommandHandler("time", mod_commands.time))
app.add_handler(CommandHandler("help", mod_commands.help))
app.add_handler(CommandHandler("sum", mod_commands.sum))
app.run_polling()
