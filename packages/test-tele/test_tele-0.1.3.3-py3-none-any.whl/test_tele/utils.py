"""Utility functions to smoothen your life."""

import logging
import os
import platform
import re
import sys
from datetime import datetime
from typing import TYPE_CHECKING

from telethon.client import TelegramClient
from telethon.hints import EntityLike
from telethon.tl import types
from telethon.tl.functions.messages import TranslateTextRequest
from telethon.tl.types.messages import TranslateResultText
from telethon.tl.types import messages
from telethon.tl.custom.message import Message

# import __version__
from test_tele import storage as st
from test_tele.config import CONFIG
from test_tele.plugin_models import STYLE_CODES, SendAs

if TYPE_CHECKING:
    from test_tele.plugins import TgcfMessage

ALBUM_ID = None
CAPTION = ""
MEDIA_ALBUM = []

def platform_info():
    nl = "\n"#Running tgcf {__version__}\
    return f""" 
    Python {sys.version.replace(nl,"")}\
    \nOS {os.name}\
    \nPlatform {platform.system()} {platform.release()}\
    \n{platform.architecture()} {platform.processor()}"""


async def send_message(recipient: EntityLike, tm: "TgcfMessage") -> Message:
    """Forward or send a copy, depending on config."""
    client: TelegramClient = tm.message.client

    if CONFIG.plugins.special.translate and CONFIG.plugins.special.check:
        tm = await translate(tm)
    
    if CONFIG.show_forwarded_from:
        return await client.forward_messages(recipient, tm.message)
    
    if tm.new_file:
        message = await client.send_file(
            recipient, tm.new_file, caption=tm.text, reply_to=tm.reply_to
        )
        return message

    if CONFIG.plugins.special.check and CONFIG.plugins.special.send_as != SendAs.ONEBYONE:
        if CONFIG.plugins.special.send_as == SendAs.SOURCE:
            return await send_message_as(recipient, tm)
    else:
        tm.message.text = tm.text
        return await client.send_message(recipient, tm.message, reply_to=tm.reply_to)
    

async def send_message_as(recipient: EntityLike, tm: "TgcfMessage"):
    global CAPTION
    global ALBUM_ID
    global MEDIA_ALBUM
    client = tm.message.client


    logging.warning(f"gaje cuy -- > {tm.message.grouped_id} {tm.text}")
    
    if tm.message.grouped_id != None:
        if tm.message.grouped_id != ALBUM_ID and MEDIA_ALBUM:
            logging.warning(f"sending #1 {tm.message.grouped_id} {tm.text} {CAPTION}")
            await client.send_file(
                recipient, MEDIA_ALBUM, caption=CAPTION, reply_to=tm.reply_to
            )
            MEDIA_ALBUM = []
        
        logging.warning(f"appending #1 {tm.message.grouped_id} {tm.text} {CAPTION}")
        if tm.message.grouped_id != ALBUM_ID:
            logging.warning("kok ini true?")
            CAPTION = tm.text
        logging.warning(f"{tm.message.grouped_id != ALBUM_ID} ini caption: {CAPTION}")
        ALBUM_ID = tm.message.grouped_id
        MEDIA_ALBUM.append(tm.message.media)
    elif tm.message.grouped_id != ALBUM_ID:
        logging.warning(f"sending #2 {tm.message.grouped_id} {tm.text} {CAPTION}")
        await client.send_file(
            recipient, MEDIA_ALBUM, caption=CAPTION, reply_to=tm.reply_to
        )
        MEDIA_ALBUM = []
        ALBUM_ID = tm.message.grouped_id
        if tm.message.grouped_id != None:
            logging.warning(f"appending #2 {tm.message.grouped_id} {tm.text} {CAPTION}")
            MEDIA_ALBUM.append(tm.message.media)
            CAPTION = tm.text
        else:
            if tm.new_file:
                logging.warning(f"kirim 1 atas {tm.message.grouped_id} {tm.text} {CAPTION}")
                return await client.send_file(
                    recipient, tm.new_file, caption=tm.text, reply_to=tm.reply_to
                )
            else:
                logging.warning(f"kirim 2 atas {tm.message.grouped_id} {tm.text} {CAPTION}")
                return await client.send_message(recipient, tm.message, reply_to=tm.reply_to)
    else:
        logging.warning(f"{tm.message.grouped_id != ALBUM_ID} {tm.message.grouped_id} {ALBUM_ID}")
        if MEDIA_ALBUM:
            logging.warning(f"sending #3 {tm.message.grouped_id} {tm.text} {CAPTION}")
            await client.send_file(
                recipient, MEDIA_ALBUM, caption=CAPTION, reply_to=tm.reply_to
            )
            MEDIA_ALBUM = []
            if tm.new_file:
                logging.warning(f"kirim 1 bawah {tm.message.grouped_id} {tm.text} {CAPTION}")
                return await client.send_file(
                    recipient, tm.new_file, caption=tm.text, reply_to=tm.reply_to
                ) 
            else:
                logging.warning(f"kirim 2 bawah {tm.message.grouped_id} {tm.text} {CAPTION}")
                return await client.send_message(recipient, tm.message, reply_to=tm.reply_to)



async def translate(tm: "TgcfMessage") -> Message:
    client = tm.message.client
    if tm.text:
        try:
            translate_text_result: TranslateResultText = await client(TranslateTextRequest(
                to_lang=CONFIG.plugins.special.lang,
                peer=tm.message.chat_id,
                msg_id=tm.message.id,
                text=tm.text
            ))
            tm.text = translate_text_result.text
        except Exception as e:
            logging.error(f"{e}")
            pass
    return tm


def cleanup(*files: str) -> None:
    """Delete the file names passed as args."""
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            logging.info(f"File {file} does not exist, so cant delete it.")


def stamp(file: str, user: str) -> str:
    """Stamp the filename with the datetime, and user info."""
    now = str(datetime.now())
    outf = safe_name(f"{user} {now} {file}")
    try:
        os.rename(file, outf)
        return outf
    except Exception as err:
        logging.warning(f"Stamping file name failed for {file} to {outf}. \n {err}")


def safe_name(string: str) -> str:
    """Return safe file name.

    Certain characters in the file name can cause potential problems in rare scenarios.
    """
    return re.sub(pattern=r"[-!@#$%^&*()\s]", repl="_", string=string)


def match(pattern: str, string: str, regex: bool) -> bool:
    if regex:
        return bool(re.findall(pattern, string))
    return pattern in string


def replace(pattern: str, new: str, string: str, regex: bool) -> str:
    def fmt_repl(matched):
        style = new
        s = STYLE_CODES.get(style)
        return f"{s}{matched.group(0)}{s}"

    if regex:
        if new in STYLE_CODES:
            compliled_pattern = re.compile(pattern)
            return compliled_pattern.sub(repl=fmt_repl, string=string)
        return re.sub(pattern, new, string)
    else:
        return string.replace(pattern, new)


def clean_session_files():
    for item in os.listdir():
        if item.endswith(".session") or item.endswith(".session-journal"):
            os.remove(item)
