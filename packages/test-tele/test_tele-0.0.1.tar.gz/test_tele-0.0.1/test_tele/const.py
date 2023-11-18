"""Declare all global constants."""

COMMANDS = {
    "start": "Check whether I am alive",
    "dd": "Download media from given link",
    "help": "Learn usage",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.json"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"

MONGO_DB_NAME = "tgcf-config"
MONGO_COL_NAME = "tgcf-instance-0"
