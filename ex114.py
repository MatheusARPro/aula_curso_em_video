# import requests
# import logging
# import warnings

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def access_site(url):
#     """
#     Attempts to access the given URL and logs whether it is accessible or not.

#     Args:
#         url (str): The URL to access.

#     Returns:
#         bool: True if the site is accessible, False otherwise.
#     """
#     try:
#         # Disable SSL warnings for this request
#         with warnings.catch_warnings():
#             warnings.simplefilter("ignore")
#             response = requests.get(url, verify=False, timeout=10)  # Added timeout for safety
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         logging.info(f'O site {url} está acessível no momento.')
#         return True
#     except requests.exceptions.ConnectionError:
#         logging.warning(f'O site {url} não está acessível no momento.')
#         return False
#     except requests.exceptions.RequestException as e:
#         logging.error(f'Erro ao acessar o site {url}: {e}')
#         return False
    

# access_site('https://pudim.com.br')




import urllib
import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen('https://www.pudim.com.br') 
except urllib.error.URLError:
    print('O site que foi requisitado não está acessivel no momento.')
else:
    print('O site requisitado está acessivel no momento.')

