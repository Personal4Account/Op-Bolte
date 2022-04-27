from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
        await query.edit_message_text(
              f"""


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» Check out the menu below to read the module information & see the list of available Commands !
All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👮🏻‍♀️ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("👩🏻‍💼 Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="home_start")
                ],
            ]
        ),
    )
