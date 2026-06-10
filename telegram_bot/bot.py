from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8863109789:AAGoXUD5iMXjWeGueRjYEW-EB2Irl2NLTX0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello it`s working Mr. Zigman 🚀")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT started....")

app.run_polling()
