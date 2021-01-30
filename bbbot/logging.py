import logging

logging.basicConfig(
         format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
         level=logging.INFO,
         datefmt='%Y-%m-%d %H:%M:%S')
def logger_factory(name):
    return logging.getLogger(name)