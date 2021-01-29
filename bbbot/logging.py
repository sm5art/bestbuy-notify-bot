import logging

logging.basicConfig(level=logging.INFO)

def logger_factory(name):
    return logging.getLogger(name)