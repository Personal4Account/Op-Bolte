from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("bot_start"))
async def start_op(_, query: CallbackQuery):
        await query.edit_message_text(
              f"""**𝐇𝐞𝐲𝐲 [!!](https://telegra.ph/file/07dec9c9679660f60fbea.jpg) 𝐁𝐚𝐛𝐲 ^ ❤️ ^ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐒𝐮𝐩𝐞𝐫𝐅𝐚𝐬𝐭 ✨ 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐫𝐯𝐞𝐫 😎🤘 𝐀𝐝𝐝 𝐌𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 & 𝐅𝐞𝐞𝐥 𝐋𝐚𝐠 𝐅𝐫𝐞𝐞 __ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎸 𝐢𝐧 𝘃𝗰. 𝐑𝐮𝐧 𝐎𝐧 𝐕𝐏𝐒 🌎 𝐒𝐞𝐫𝐯𝐞𝐫 <𝟑
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


@Client.on_callback_query(filters.regex("bot_about"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""**^ 📀 𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐆𝐢𝐯𝐞𝐧 𝐁𝐞𝐥𝐨𝐰 </ 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐀𝐥𝐥 𝐓𝐡𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐁𝐨𝐭 ^

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : 
@Its_romeoo | @itz_xoxo**""",
        reply_markup=InlineKeyboardMarkup(
            [
                    InlineKeyboardButton("^ 𝐅𝐮𝐥𝐥 𝐈𝐧𝐟𝐨 🤖", callback_data="bot_info"),
                    InlineKeyboardButton("^ 𝐒𝐞𝐭𝐔𝐩❗️", callback_data="bot_setup")
                ],[
                    InlineKeyboardButton("^ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬❓", callback_data="bot_commands"),
                    InlineKeyboardButton("^ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 ⚙", callback_data="bot_code")
                ],[
                    InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bot_code"))
async def bot_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("Source Code")
    await query.edit_message_text(
        f"""**^ 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐒𝐨𝐨𝐧 🎸 𝐓𝐡𝐞 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐁𝐨𝐭 𝐢𝐬 𝐑𝐞𝐚𝐝𝐲 </ 𝐈𝐟 𝐰𝐞 𝐆𝐞𝐭 𝐆𝐨𝐨𝐝 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 𝐅𝐫𝐨𝐦 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 , 𝐓𝐡𝐞 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐝 𝐓𝐨 𝐘𝐨𝐮 𝐄𝐚𝐫𝐥𝐲 𝐀𝐬 𝐏𝐨𝐬𝐬𝐢𝐛𝐥𝐞 ✅ ^**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_about")]]
        ),
    )


@Client.on_callback_query(filters.regex("bot_setup"))
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("Full Setup")
    await query.edit_message_text(
        f"""**1 = 𝐀𝐝𝐝 𝐭𝐡𝐢𝐬 𝐏𝐨𝐰𝐞𝐫𝐅𝐮𝐥 𝐁𝐨𝐭 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ^ 𝐓𝐡𝐞𝐧 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧 𝐖𝐢𝐭𝐡 𝐍𝐞𝐞𝐝𝐞𝐝 𝐏𝐨𝐰𝐞𝐫𝐬 & 𝐂𝐚𝐥𝐥 𝐀 𝐀𝐝𝐦𝐢𝐧 𝐓𝐨 𝐒𝐞𝐧𝐝 /play 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐈𝐧𝐯𝐢𝐭𝐞 𝐓𝐡𝐞 𝐌𝐮𝐬𝐢𝐜 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐈𝐧 𝐓𝐡𝐞 𝐆𝐫𝐨𝐮𝐩 🎸 

2 = 𝐀𝐟𝐭𝐞𝐫 𝐉𝐨𝐢𝐧𝐢𝐧𝐠 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐏𝐥𝐚𝐲 𝐘𝐨𝐮𝐫 𝐅𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐒𝐨𝐧𝐠𝐬 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 𝐈𝐧 𝐭𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 !! ^ #𝐒𝐭𝐫𝐚𝐲𝐂𝐨𝐝𝐞𝐫 ❤️ 𝐒𝐞𝐫𝐯𝐞𝐫 <3 

𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : @StrayCoder 
𝐁𝐢𝐠 𝐓𝐡𝐚𝐧𝐤𝐬 𝐓𝐨 @itz_xoxo ^ 🤝**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_about")]]
        ),
    )


@Client.on_callback_query(filters.regex("bot_commands"))
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("Commands")
    await query.edit_message_text(
        f"""**⭐️ 𝗕𝗮𝘀𝗶𝗰 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 :

/play (song Name) - Start streaming Song in the voice chat of the Group / Channel

/song (Song Name) - Download the song from the Stray Server <3

/repo - Get the source code of the Bot

/help , /commands - Get all the commands of the Bot


⭐️ 𝗔𝗱𝗺𝗶𝗻𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 :

/skip - Skips the Current Track in the voice chat and starts playing next song 

/pause /resume - Pause and Resume the Song in voice chat

/end /stop - The assistant of the Player disconnects from the voice Chat


Powered By : @StrayCoder**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_about")]]
        ),
    )


@Client.on_callback_query(filters.regex("bot_info"))
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("Bot Information")
    await query.edit_message_text(
        f"""**𝐈 𝐚𝐦 𝐚𝐧 𝐒𝐮𝐩𝐞𝐫𝐅𝐚𝐬𝐭 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐏𝐥𝐚𝐲𝐞𝐫 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐋𝐚𝐠 𝐟𝐫𝐞𝐞 & 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 __ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 𝐀 𝐍𝐨𝐨𝐛 𝐓𝐞𝐚𝐦 !! (𝐲) 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐟𝐨𝐫 𝐅𝐫𝐞𝐞 </

⭐️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : @Its_romeoo
⭐️ 𝐌𝐚𝐧𝐚𝐠𝐞𝐝 𝐁𝐲 : @itz_xoxo

(𝐲) #𝐒𝐭𝐫𝐚𝐲_𝐒𝐞𝐫𝐯𝐞𝐫 😎🤘 𝐌𝐮𝐬𝐢𝐜**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_about")]]
        ),
    )
