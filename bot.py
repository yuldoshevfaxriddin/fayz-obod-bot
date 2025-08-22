from telegram import Update
from telegram.ext import Application, CommandHandler
from fayzobodnatija import get_result, URL_VOTE_RESULTS_XORAZM, URL_VOTE_RESULTS_XORAZM_BOGOT
from db import insert_user, has_user
from config import TOKEN

# /natija buyrug'iga javob qaytaradigan funksiya
async def natija_bogot(update: Update, context) -> None:
    message = "Bog'ot tuman natijalari:\n\n"
    await update.message.reply_text(message + get_result(URL_VOTE_RESULTS_XORAZM_BOGOT), parse_mode='HTML')

async def natija_xorazm(update: Update, context) -> None:
    message = "Xorazm viloyati natijalari:\n\n"
    await update.message.reply_text(message + get_result(URL_VOTE_RESULTS_XORAZM), parse_mode='HTML')

async def start(update: Update, context) -> None:
    await update.message.reply_text('/natija - natija ko\'rish')
help_message = """
/natija_bogot - Bog'ot tuman natijalarini ko'rish
/natija_xorazm - Xorazm viloyati natijalarini ko'rish
"""
async def start(update: Update, context) -> None:
    tg_id = update.message.from_user.id
    tg_username = update.message.from_user.username
    tg_first_name = update.message.from_user.first_name
    tg_last_name = update.message.from_user.last_name if update.message.from_user.last_name else ""
    if not has_user(tg_id):
        insert_user(tg_first_name, tg_last_name, tg_username, tg_id)
    await update.message.reply_text(help_message)
async def help(update: Update, context) -> None:
    await update.message.reply_text(help_message)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    # Dispatcher orqali buyrug'ga handler qo'shish
    application.add_handler(CommandHandler('natija_bogot', natija_bogot))
    application.add_handler(CommandHandler('natija_xorazm', natija_xorazm))
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))

    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    application.run_polling()


if __name__ == '__main__':
    main()
