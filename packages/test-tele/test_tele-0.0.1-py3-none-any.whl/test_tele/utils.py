"""Utility functions to smoothen your life."""

import logging
import os
import json
import platform
import re
import sys
import shutil
import asyncio
import subprocess
from datetime import datetime
from typing import TYPE_CHECKING, Union

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
CAPTION = []
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

    if CONFIG.show_forwarded_from:
        as_album = None
        if CONFIG.plugins.special.check and CONFIG.plugins.special.send_as == SendAs.ALBUM:
            as_album = True
        return await client.forward_messages(
            recipient, tm.message, silent=True, as_album=as_album, background=True
        )

    if CONFIG.plugins.special.check and CONFIG.plugins.special.send_as != SendAs.ONEBYONE and CONFIG.mode == 1:
        if CONFIG.plugins.special.send_as == SendAs.SOURCE:
            return await get_album(recipient, tm)
    else:
        return await start_sending(recipient, tm)


async def start_sending(recipient: EntityLike, tm: "TgcfMessage") -> Message:
    client = tm.message.client
    if tm.new_file:
        message = await client.send_file(
            recipient, tm.new_file, caption=tm.text, reply_to=tm.reply_to, silent=True, background=True
        )
        return message
    else:
        tm.message.text = tm.text
        return await client.send_message(
            recipient, tm.message, reply_to=tm.reply_to, silent=True, background=True
        )


# Work well in past mode
async def send_message_source(recipient: EntityLike, tm: "TgcfMessage") -> Message:
    client = tm.message.client
    global MEDIA_ALBUM
    caption = None
    
    if MEDIA_ALBUM:
        if CAPTION and (CAPTION[-1] != '' or CAPTION[0] != '') and CONFIG.mode == 1 and CONFIG.past.reverse:
            caption = CAPTION[0]
        else:
            caption = CAPTION[-1]
        return await client.send_file(
            recipient, MEDIA_ALBUM, caption=caption, reply_to=tm.reply_to
        )
    else:
        return await start_sending(recipient, tm)


async def get_album(recipient: EntityLike, tm: "TgcfMessage") -> Message:
    global MEDIA_ALBUM, ALBUM_ID, CAPTION

    if tm.message.grouped_id != None:
        if tm.message.grouped_id != ALBUM_ID and MEDIA_ALBUM:
            await send_message_source(recipient, tm)
            MEDIA_ALBUM = []
            CAPTION = []
            ALBUM_ID = tm.message.grouped_id
            MEDIA_ALBUM.append(tm.message.media)
            CAPTION.append(tm.text)
            return
        else:
            ALBUM_ID = tm.message.grouped_id
            MEDIA_ALBUM.append(tm.message.media)
            CAPTION.append(tm.text)
    elif tm.message.grouped_id != ALBUM_ID:
        message = await send_message_source(recipient, tm)
        MEDIA_ALBUM = []
        CAPTION = []
        ALBUM_ID = tm.message.grouped_id
        if tm.message.grouped_id != None:
            MEDIA_ALBUM.append(tm.message.media)
            CAPTION.append(tm.text)
        else:
            message = await send_message_source(recipient, tm)
            return message
    else:
        if MEDIA_ALBUM:
            message = await send_message_source(recipient, tm)
            MEDIA_ALBUM = []
            CAPTION = []
        message = await send_message_source(recipient, tm)
        return message


# Download image from supported url
async def download_from_link(recipient: EntityLike, tm: "TgcfMessage", link: str, count: Union[int, str]=10):
    # Perintah untuk menjalankan gallery-dl dan mendownload konten dari Telegraph
    command0 = f'gallery-dl --range 0 -j {link} --config-ignore -c config/config.json'

    # Get how many file are they inside the link
    tot_image = count
    try:
        output = subprocess.Popen(command0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = output.communicate()
        data = json.loads(out)
        tot_image = data[0][1]["count"]
    except:
        pass

    if str(count).lower() == 'all':
        count = tot_image

    command1 = f'gallery-dl --no-part --range 1-{count} {link} --config-ignore -c config/config.json'

    try:
        process = subprocess.Popen(
            command1, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        media_list = []
        n = 0
        while True:
            n += 1
            line = process.stdout.readline().decode('utf-8')

            if not line:
                break
            
            if not line.startswith("./"):
                continue

            output = line.strip()
            output = output[2:].replace('\\', '/')

            # Membagi nama folder dan nama file
            folder_name, file_name = os.path.split(output)

            media_list = await upload_files(tm, media_list, folder_name, file_name)
            
            if len(media_list) % 10 == 0:
                # masih error jika didalam link terdapat media dengan jenis berbeda
                tm.text = f'#media_downloader' if n == count else None
                tm.new_file = media_list
                await start_sending(recipient, tm)
                media_list = []

            await asyncio.sleep(0.5)

        if media_list:
            tm.text = f'#media_downloader'
            tm.new_file = media_list
            await start_sending(recipient, tm)
            media_list = []

        shutil.rmtree(folder_name)

    except Exception as e:
        logging.error(f"{e}")
        tm.text = "Unsupported URL"
        await start_sending(recipient, tm)


async def upload_files(tm: "TgcfMessage", media_list, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    client = tm.message.client

    with open(file_path, 'rb') as file:
        media_photo = await client.upload_file(file=file, part_size_kb=512, file_name=file_name)
        media_list.append(media_photo)
    cleanup(file_path)
    
    return media_list


async def translate(tm: "TgcfMessage") -> Message:
    """Live translate the message text."""
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
