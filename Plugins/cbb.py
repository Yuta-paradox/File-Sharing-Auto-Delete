# (©) Itz_Zeno
# Movie Channel @Netflix_Dual
# Anime Channel @Anime_Wide

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╔═════════════════\n├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={6383801114}'>ᴢᴇɴᴏ ㊍</a>\n├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n├⋗ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Movie_Decade>ᴍᴏᴠɪᴇ ᴅᴇᴄᴀᴅᴇ</a>\n├⋗ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Wide>ᴀɴɪᴍᴇ ᴡɪᴅᴇ</a>\n├⋗ Request Group : <a href=https://t.me/Requests_Groupp>Req Grp</a>\n╚═════════════════</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
