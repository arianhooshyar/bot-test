import logging

from telegram.ext import Updater, CommandHandler, MessageHandler

# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and

# context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""

    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""

    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""

    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    updater = Updater("6129607481:AAHt1PdMv-L8EdYtbSLIafJ8DWhV21s3STQ", update_queue=True)

    # Get the dispatcher to register handlers

    dp = updater.dispatcher

    # on different commands - answer in Telegram

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("help", help))

    #  dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
