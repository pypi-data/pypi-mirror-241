import logging
import subprocess
from typing import Any, Dict

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from test_tele.plugins import TgcfMessage, TgcfPlugin

def download(text):

    process = subprocess.Popen(
        ["gallery-dl", text]
    )

class TgcfSpecial(TgcfPlugin):
    id_ = "special"

    def __init__(self, data):
        self.special = data
        logging.info(self.special)

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if tm.text and self.special.download:
            download(tm.text)
        
        return tm

    