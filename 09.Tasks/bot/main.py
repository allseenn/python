from telegram import Update
import random
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mod_help as help
import mod_game as game
import mod_log as log
########## TOKEN ##############
TOKEN = ""
# with open ('D:\Documents\Bots\GBpyBot.txt', 'r') as file:
#        TOKEN = file.readline()
###############################
async def new(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        global board, bot, man, count
        count = 0
        board = game.game()
        bot = "GeekBot"
        man = update.effective_user.first_name
        await update.message.reply_text(f"{man} нолик, {bot} крестик")
        lot = random.choice([man, bot])
        if lot == bot:
                board = game.bot_turn(board)
                await update.message.reply_text(game.prints(board))
                await update.message.reply_text(f'{lot} пошел первым, {man} ходи /s <n> или /h помощь')
                
        else:
                await update.message.reply_text(game.prints(board))
                await update.message.reply_text(f"{man}, ходи первым /s <n> или /h помощь")
        lot = man

async def step(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        global lot, bot, board, count
        msg = update.message.text
        choose = msg.split()[1]
        if count < 5:
                board = game.man_turn(board, choose)
                # await update.message.reply_text(game.prints(board))
                if game.winner_check(board) == "O":
                        await update.message.reply_text(game.prints(board))
                        await update.message.reply_text(f'Победил {man}!')
                        log.log(update, "win")
                        count = 10
                        exit()     
                board = game.bot_turn(board)
                await update.message.reply_text(game.prints(board))
                if game.winner_check(board) == "X":
                        await update.message.reply_text(f'Победил {bot}! ') 
                        log.log(update, "loose") 
                        count = 10
                        exit()
                else:
                        await update.message.reply_text(f'{man} ходи /s <n> или /h помощь')
                count += 1
        elif 8 < count >= 5:
                await update.message.reply_text(f'Ничья')
                log.log(update, "draw")
                count = 10
        else:
                await update.message.reply_text(f'Игра окончена, /n начать новую')

board = ""
lot = ""
man = ""
bot = ""
count = 0

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", help.start))
app.add_handler(CommandHandler("h", help.help))
app.add_handler(CommandHandler("n", new))
app.add_handler(CommandHandler("s", step))
# app.add_handler(CommandHandler("sum", mod_commands.sum))
app.run_polling()
