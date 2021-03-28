# Used for identify features etc., DO NOT MODIFY
VERSION = "0.3b"
# DO NOT MODIFY END

TIME_BETWEEN_CHECK = 10
TIME_BETWEEN_CLEAR = 3600 # An hour
EXPIRY_TIME = 3600 * 6
HTTP_RETRY = 3

BASE_JSON_DIR = "jsons"
LOGS_DIR = "logs"

CHANNELS_JSON = "channels.json"
FETCHED_JSON = "fetched.json"

# Use multi-IPs for checking.
IP_POOL = None

# Send to discord on video privated
ENABLE_PRIVATE_CHECK = False

# Callbacks
ENABLED_MODULES = {
    "discord": False,
    "telegram": False
}

DISCORD_WEBHOOK_URL = None
DISCORD_SEND_FILES = False

TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None
TELEGRAM_SEND_FILES = False

# On live
ENABLED_MODULES_ONLIVE = {
    "discord": False,
    "telegram": False
}

DISCORD_WEBHOOK_URL_ONLIVE = None

TELEGRAM_BOT_TOKEN_ONLIVE = TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID_ONLIVE = None

# ====== Chat Downloader ====== #
# `pip install chat_downloader`
CHAT_DIR = None

CHAT_INACTIVITY_DURATION = 30
CHAT_BUFFER_TIME = 1
CHAT_TASK_CLEAR_INTERVAL = 300

# `pip install brotlipy`
BROTLI_COMPRESS = False
# ====== Chat Downloader END ====== #