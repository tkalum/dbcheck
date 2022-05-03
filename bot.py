import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyromod import listen
from pyrogram import Client
from config import *
from plugins import *

def main():
    plugins = dict(root="plugins")
    app = Client("FileStore",
                 bot_token='5100731335:AAHt0PAmeE0mv9905DqpMt039vg-ibHZ18k',
                 api_id=19611094,
                 api_hash='c5198b0dab5cdd8e0eaaf3e0c742fbd3',
                 plugins=plugins,
                 workers=100)

    app.run()


if __name__ == "__main__":
    main()
