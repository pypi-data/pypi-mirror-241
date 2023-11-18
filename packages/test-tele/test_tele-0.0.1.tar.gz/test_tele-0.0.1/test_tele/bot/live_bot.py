"""A bot to controll settings for tgcf live mode."""

import logging

import yaml
from telethon import events

from test_tele import config
from test_tele.utils import download_from_link
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
        logging.warning(parsed_args)
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


async def download_command_handler(event):
    """Handle the /dd command"""
    notes = """This command is used to download images from given link.

    arguments are: [link: string] [n-image: optional(number | "all")]

    Example: `/dd https://telegra.ph/Jizoku-A-Night-With-Loona-11-16`

    The default value of `n-image` is 10 (This means that 10 images will be sent to you as an album)

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n")
        
        if " " in args:
            link, n = args.split(" ")
        else:
            link = args
            n = 10
        tm = TgcfMessage(event.message)
        tm.reply_to = tm.message.id
        
        await download_from_link(event.message.chat_id, tm, link, n)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

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
        "download": (download_command_handler, events.NewMessage(pattern=f"{_}dd")),
    }

    return command_events
