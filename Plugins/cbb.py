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
            text = f"<b>╔═════════════════\n├⋗ My God : <a href='tg://user?id={6193451722}'>Yuta ㊍</a>\n├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n├⋗ Anime Channel : <a href=https://t.me/Animes_Paradox>Anime Paradox</a>\n├⋗ Ongoing Channel : <a href=https://t.me/ongoing_Paradox>Ongoing channel</a>\n├⋗ Anime Chat Group : <a href=https://t.me/Paradox_anime_gang>Anime chat Grp</a>\n╚══════════════════</b>",
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
