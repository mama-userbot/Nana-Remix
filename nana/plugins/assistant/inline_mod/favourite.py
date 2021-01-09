from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineQueryResultArticle
from pyrogram.types import InputTextMessageContent
from nana import Owner


async def fav_func(fav, answers):
    if fav:
        text = '**My watchlist:**\n'
        for title in fav:
            text += f' - {title.data}\n'
        keyb = [
            [
                InlineKeyboardButton(
                    text='Watched ✅', callback_data=f'remfav_{Owner}',
                ),
            ],
        ]
        answers.append(
            InlineQueryResultArticle(
                title='Favourites',
                description='Anime',
                input_message_content=InputTextMessageContent(
                    text, parse_mode='markdown',
                ),
                reply_markup=InlineKeyboardMarkup(keyb),
            ),
        )
    else:
        answers.append(
            InlineQueryResultArticle(
                title='Fabourites',
                description='Anime',
                input_message_content=InputTextMessageContent(
                    '**No favourites yet!**', parse_mode='markdown',
                ),
            ),
        )
