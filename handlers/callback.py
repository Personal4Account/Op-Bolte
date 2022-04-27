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
                [
                    InlineKeyboardButton("^ 𝐅𝐮𝐥𝐥 𝐈𝐧𝐟𝐨 ⚙", callback_data="bot_info"),
                ],[
                    InlineKeyboardButton("^ 𝐒𝐞𝐭𝐔𝐩❗️", callback_data="bot_setup"),
                ],[
                    InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bot_start")
                ],
            ]
        ),
    )
