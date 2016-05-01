Reddit Comment Xpander Bot
======

Simple Telegram bot that sends the contents of a reddit message (that was linked to the active chat), allowing users to read it without leaving the app.


To install it (from the project folder) simply run the command (requires Python 3):
```
pip install -r requirements.txt
```

### Limitations
* If the comment link has a `context` query param then, the comment that the bot sends, is the first from that given context.
