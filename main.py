import os
import telebot

TOKEN = "656488884:AAFpyXXOeIBnGaMPfWfvcO0bUUYKv4CPW8s"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
##########################################
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "You write to me: "+message.text)
    print ("Message text: "+ message.text)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
###############################################
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://telegram-bot-r.herokuapp.com/" + TOKEN)
updater.idle()