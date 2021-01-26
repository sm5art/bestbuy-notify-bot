import configparser
import os
from bbbot.utils import current_directory

CONFIG = current_directory(__file__) + "/bot.cfg"

def get_cfg(section):
    config = configparser.ConfigParser()
    config.read(CONFIG)
    api = config.items(section)
    return dict(api)