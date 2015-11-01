__author__ = 'Marcin'
from socket import gethostbyname


def get_ip_address(url):
    return gethostbyname(url)

