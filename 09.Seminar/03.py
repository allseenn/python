from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)

app = ApplicationBuilder().token("”казать свой токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.run_polling()
