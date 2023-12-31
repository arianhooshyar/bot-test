import logging
# from telegram.ext import Dispatcher
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("6129607481:AAHt1PdMv-L8EdYtbSLIafJ8DWhV21s3STQ", update_queue=True)

    # Get the dispatcher to register handlers

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("help", help))

    #   dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors

    dp.add_error_handler(error)

    # Start the Bot

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,

    # SIGTERM or SIGABRT. This should be used most of the time, since

    # start_polling() is non-blocking and will stop the bot gracefully.

    updater.idle()


if __name__ == '__main__':
    main()
