import warnings
from urllib.parse import parse_qs
from urllib.parse import urlparse

import praw
import validators
from twx.botapi import TelegramBot

bot = TelegramBot('BOT_API_KEY')
bot.update_bot_info().wait()
print(bot.username)


def run():
    last_update = 0
    r = praw.Reddit("Telegram Comment Xpander")
    while True:
        updates = bot.get_updates(last_update + 1).wait()
        for update in updates:
            last_update = max(update.update_id, last_update)
            if update.message.text and validators.url(update.message.text):
                parse = urlparse(update.message.text)
                parts = parse.path[1:].split('/')
                params = parse_qs(parse.query)
                context = 0
                if 'context' in params:
                    try:
                        context = int(params['context'][0])
                    except ValueError:
                        print("Context is not an int")
                if len(parts) == 6 and 'r' == parts[0] and 'comments' == parts[2]:
                    try:
                        comment = r.get_submission(update.message.text).comments[0]
                        reply = "%s\nSubmitted by - %s\n%s" % (comment.body, comment.author.name, update.message.text)
                        bot.send_message(update.message.chat, reply)
                    except Exception as e:
                        print("Unexpected error:", str(e))
                    

if __name__ == '__main__':
    warnings.simplefilter('ignore')
    run()
