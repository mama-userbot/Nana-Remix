from asyncio import sleep
from pyrogram import filters
from nana import app, COMMAND_PREFIXES, AdminSettings, edit_or_reply
from nana.utils.sticker import create_sticker

__MODULE__ = "Quotly"
__HELP__ = """
This module can make message text to sticker. (Experimental)

──「 **Make Quote From Message** 」──
-> `q`
__Reply To Message Text To Create Quote Sticker.__

"""


@app.on_message(
    filters.user(AdminSettings) &
    filters.command("q", COMMAND_PREFIXES)
)
async def q_maker(_, message):
    if not message.reply_to_message:
        await edit_or_reply(
            message,
            text="**Reply to any users text message**"
        )
        return
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    while not is_sticker:
        try:
            ms_g = await app.get_history("@QuotLyBot", 1)
            check = ms_g[0]["sticker"]["file_id"]
            print(check)
            is_sticker = True
        except Exception as e:
            print(e)
            await sleep(0.5)
            try:
                print("Making a Quote")
            except Exception as e:
                print(e)
    msg_id = ms_g[0]["message_id"]
    await message.delete()
    await app.copy_message(
        message.chat.id,
        "@QuotLyBot",
        msg_id
    )


@app.on_message(
    filters.user(AdminSettings) &
    filters.command("quote", COMMAND_PREFIXES)
)
async def qoute_maker(client, message):
    if message.reply_to_message:
        await create_sticker(client, message.reply_to_message)
    else:
        await create_sticker(client, message)

    await message.delete()
