from pyrogram import *
from pyrogram.types import *


try:
    from .main import *
except:
    pass
try:
    from .call import *
except Exception as e:
    print("An error occurred:", e)
    pass






ABOUT_TEXT = """
**My Details:**
`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)

`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)

`👨‍💻 Developer:` [Anonymous](t.me/DKBOTZHELP_2)

`📢 Support:` [Anonymous](https://t.me/DKBOTZ)

`🌐 Source Code:` **[Click Here](https://t.me/DKBOTZHELP_2)**
"""
ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('👨‍💻 Developer:', url='t.me/DKBOTZHELP_2')
    ]
])

@Client.on_message(filters.command('dev'))
async def dev_command_dkbotz(c, m: Message):
    reply_markup=ABOUT_REPLY_MARKUP

    bot = await c.get_me()

    await m.reply_text(ABOUT_TEXT.format(bot.mention(style='md')),reply_markup=reply_markup , disable_web_page_preview=True)


@Client.on_message(filters.command('about'))
async def about_command_dkbotz(c, m: Message):
    reply_markup=ABOUT_REPLY_MARKUP

    bot = await c.get_me()
    await m.reply_text(ABOUT_TEXT.format(bot.mention(style='md')),reply_markup=reply_markup , disable_web_page_preview=True)
