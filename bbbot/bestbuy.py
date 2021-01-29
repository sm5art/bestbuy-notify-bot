import requests
from bs4 import BeautifulSoup
from bbbot.logging import logger_factory

logger = logger_factory(__name__)

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

availability_str = '"availability":"http://schema.org/InStock"' 
nonavailability_str = '"availability":"http://schema.org/SoldOut"'

def get_request(endpoint):
    req = requests.get(endpoint, headers=headers)
    logger.info("Sending request to %s" % endpoint)
    return req

def availability(endpoint):
    ret = availability_str in get_request(endpoint).text
    if ret:
        logger.info("Stock is available sending message to discord")
    else:
        logger.info("Stock is not available")
    return ret

