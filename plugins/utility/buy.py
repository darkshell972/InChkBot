from pyrogram import Client, filters
from plugins.utility.db import *

@Client.on_message(filters.command("buy", prefixes=["/", "."]))
async def buy_command(bot, message):
    user_id = message.from_user.id
    if not await is_user_registered(user_id):
        await message.reply_text("You are not registered. Use /register to register.")
        return
    text = f'''<b>
Prices :-
━━━━━━━━━━━━━
1 days - 65₹  ||  1$
7 days - 250₹  ||  3$
15 days - 500₹  ||  6$
30 days - 750₹  ||  8.9$
━━━━━━━━━━━━━
Low anti-spam , cheap , fast,  added HQ gates  ⚡️

Payment Methods - Binance / Crypto
━━━━━━━━━━━━━
For more details contact @c34der
Price list - <a href="https://t.me/c34der">Click here</a>
━━━━━━━━━━━━━
If you interested to buy contact @XAY4N. ⭐
</b>'''

    await message.reply_text(text, quote=True, disable_web_page_preview=True)
