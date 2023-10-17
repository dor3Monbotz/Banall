import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6295293651:AAGbGfFQqyggnVxTHUrZH9ux1jmCC8wocPo")
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "2b445de78e5baf012a0793e60bd4fbf5")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', "19099900"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
