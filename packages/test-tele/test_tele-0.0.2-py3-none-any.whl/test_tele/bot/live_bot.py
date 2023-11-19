"""A bot to controll settings for tgcf live mode."""

import logging
import re
import time

import yaml
from telethon import events

from test_tele import config
from test_tele.utils import start_download
from test_tele.bot.utils import (
    admin_protect,
    display_forwards,
    get_args,
    get_command_prefix,
    remove_source
)
from test_tele.config import CONFIG, write_config
from test_tele.plugin_models import Style
from test_tele.plugins import TgcfMessage


@admin_protect
async def forward_command_handler(event):
    """Handle the `/forward` command."""
    notes = """The `/forward` command allows you to add a new forward.
    Example: suppose you want to forward from a to (b and c)

    ```
    /forward source: a
    dest: [b,c]
    ```

    a,b,c are chat ids

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        forward = config.Forward(**parsed_args)
        try:
            remove_source(forward.source, config.CONFIG.forwards)
        except:
            pass
        CONFIG.forwards.append(forward)
        config.from_to, config.reply_to = await config.load_from_to(event.client, config.CONFIG.forwards)

        await event.respond("Success")
        write_config(config.CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


@admin_protect
async def remove_command_handler(event):
    """Handle the /remove command."""
    notes = """The `/remove` command allows you to remove a source from forwarding.
    Example: Suppose you want to remove the channel with id -100, then run

    `/remove source: -100`

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        source_to_remove = parsed_args.get("source")
        CONFIG.forwards = remove_source(source_to_remove, config.CONFIG.forwards)
        config.from_to, config.reply_to = await config.load_from_to(event.client, config.CONFIG.forwards)

        await event.respond("Success")
        write_config(config.CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


@admin_protect
async def style_command_handler(event):
    """Handle the /style command"""
    notes = """This command is used to set the style of the messages to be forwarded.

    Example: `/style bold`

    Options are preserve,normal,bold,italics,code, strike

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n")
        _valid = [item.value for item in Style]
        if args not in _valid:
            raise ValueError(f"Invalid style. Choose from {_valid}")
        CONFIG.plugins.fmt.style = args
        await event.respond("Success")
        write_config(CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation
    

async def auto_download_command_handler(event):
    """Handle any incoming message"""

    try:
        link_regex = re.compile(r"\bhttps?://\S+")
        link = re.findall(link_regex, event.message.text)[0]

        if link:
            tm = TgcfMessage(event.message)
            tm.text = link
            tm.reply_to = tm.message.id
            
            await start_download(event.message.chat_id, tm)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


async def download_deez_command_handler(event):
    """Handle the /dd command"""
    notes = """
    **Usage**

    Command: `/dd`
    Usage: URL.. [OPTION].. 

    **Option**
    `-r` : Range, number of images, use either a number or literal 'all'
    `-u` : Username, to login with
    `-p` : Password, belonging to the given username

    **Example**
    `/dd https://example.com -r 3`
    `/dd https://example.com -u admin -p admin`

    **Note**
    Enclose URLs containing special characters (&, etc.) in double quotes: "URL".
    User/Pass required to download private content like Instagram's private user account post.

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n")

        pattern = r'^/dd\s+([^-\s]+)\s+(-r\s+(\d+))?(?:\s+-u\s+(\S+)\s+-p\s+(\S+))?$'
        match = re.match(pattern, event.message.text)

        link = match.group(1)
        r = match.group(3)
        u = match.group(4)
        p = match.group(5)

        if link:
            tm = TgcfMessage(event.message)
            r = int(r) if r else None
            tm.text = f'"{link}"' + f" -u {u} -p {p}" if u and p else ""
            tm.reply_to = tm.message.id
            await start_download(event.message.chat_id, tm, r)


    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation
    

async def test_command_handler(event):
    """Test doang"""

    logging.warning("test bisa?")
    tm = TgcfMessage(event.message)
    client = tm.message.client
    tm.reply_to = tm.message.id

    try:
        tm.new_file = [
            "https://video.twimg.com/ext_tw_video/1725102154854068225/pu/vid/avc1/966x720/ml4FJnhdJds3gtg9.mp4?tag=12"
        ]
        try:
            await client.send_file(event.message.chat_id, tm.new_file, reply_to=tm.reply_to)
        except:
            arr = []
            for item in tm.new_file:
                message = await client.send_file(event.message.chat_id, item, reply_to=tm.reply_to)
                arr.append(message)
                await client.delete_messages(event.message.chat_id, message)
            await client.send_file(event.message.chat_id, arr, reply_to=tm.reply_to)

    except Exception as e:
        await client.send_message(event.message.chat_id, str(e), reply_to=tm.reply_to)
        logging.error(f"Test : {e}")
    finally:
        raise events.StopPropagation


async def start_command_handler(event):
    """Handle the /start command"""
    await event.respond(CONFIG.bot_messages.start)


async def help_command_handler(event):
    """Handle the /help command."""
    await event.respond(CONFIG.bot_messages.bot_help)


def get_events():
    _ = get_command_prefix()
    logging.info(f"Command prefix is . for userbot and / for bot")
    command_events = {
        "start": (start_command_handler, events.NewMessage(pattern=f"{_}start")),
        "forward": (forward_command_handler, events.NewMessage(pattern=f"{_}forward")),
        "remove": (remove_command_handler, events.NewMessage(pattern=f"{_}remove")),
        "style": (style_command_handler, events.NewMessage(pattern=f"{_}style")),
        "help": (help_command_handler, events.NewMessage(pattern=f"{_}help")),
        "test_doang": (test_command_handler, events.NewMessage(pattern=f"{_}test")),
        "download_deez": (download_deez_command_handler, events.NewMessage(pattern=f"{_}dd")),
        "auto_download": (auto_download_command_handler, events.NewMessage()),

    }

    return command_events
