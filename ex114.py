import requests
import logging


logging.basicConfig(level=logging.INFO)


def acessa_site(url):
    try:
        requests.get(url=url, verify=False)
    except requests.exceptions.ConnectionError:
        logging.debug(f'O site {url} não está acessível no momento.')
    else:
        logging.debug(f'O site {url} está acessível no momento.')


acessa_site('https://pudim.com.br')
