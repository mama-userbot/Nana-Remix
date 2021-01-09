import random

from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineQueryResultArticle
from pyrogram.types import InputTextMessageContent

from nana.plugins.pm import welc_txt


async def pmpermit_func(answers):
    button = [
        [
            InlineKeyboardButton(
                'Ask for Money',
                callback_data='engine_pm_block',
            ),
            InlineKeyboardButton(
                'Contact me',
                callback_data='engine_pm_nope',
            ),
        ],
        [
            InlineKeyboardButton(
                'Report',
                callback_data='engine_pm_report',
            ),
            InlineKeyboardButton(
                'Passing by',
                callback_data='engine_pm_none',
            ),
        ],
    ]
    random.shuffle(button)
    answers.append(
        InlineQueryResultArticle(
            title='Engine pm',
            description='Filter pm',
            input_message_content=InputTextMessageContent(
                welc_txt, parse_mode='markdown',
            ),
            reply_markup=InlineKeyboardMarkup(button),
        ),
    )
