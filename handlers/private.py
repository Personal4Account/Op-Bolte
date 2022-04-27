import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    UPDATES_CHANNEL,
)



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/07dec9c9679660f60fbea.jpg",
        caption=f"""**𝐇𝐞𝐲𝐲 !! 𝐁𝐚𝐛𝐲 ^ ❤️ ^ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐒𝐮𝐩𝐞𝐫𝐅𝐚𝐬𝐭 ✨ 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐫𝐯𝐞𝐫 😎🤘 𝐀𝐝𝐝 𝐌𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 & 𝐅𝐞𝐞𝐥 𝐋𝐚𝐠 𝐅𝐫𝐞𝐞 __ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎸 𝐢𝐧 𝘃𝗰. 𝐑𝐮𝐧 𝐎𝐧 𝐕𝐏𝐒 🌎 𝐒𝐞𝐫𝐯𝐞𝐫 <𝟑
⚙ 𝐅𝐨𝐫 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 : /help

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : [𝐒𝐭𝐫𝐚𝐲 __ 𝐎𝐰𝐧𝐞𝐫 ^](https://t.me/Its_romeoo)
𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : [𝐌𝐫. 𝐗𝐨𝐗𝐨 -](https://t.me/itz_xoxo)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐓𝐨 𝐀𝐝𝐝 𝐌𝐞",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "• 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• 𝐒𝐞𝐭𝐮𝐩 & 𝐈𝐧𝐟𝐨𝐦𝐚𝐭𝐢𝐨𝐧", callback_data="bot_about"
                    )
                ],
            ]
        ),
    ) 


@Client.on_message(command("help") & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""⭐️ 𝗕𝗮𝘀𝗶𝗰 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 :

/play (song Name) - Start streaming Song in the voice chat of the Group / Channel

/song (Song Name) - Download the song from the Stray Server <3

/repo - Get the source code of the Bot

/help , /commands - Get all the commands of the Bot



⭐️ 𝗔𝗱𝗺𝗶𝗻𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 :

/skip - Skips the Current Track in the voice chat and starts playing next song 

/pause /resume - Pause and Resume the Song in voice chat

/end /stop - The assistant of the Player disconnects from the voice Chat


Powered By : @StrayCoder
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "❰𝗖𝗵𝗮𝗻𝗻𝗲𝗹❱", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
            ]
        )
    )
