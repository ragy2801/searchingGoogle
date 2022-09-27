"""
This script is to show the main factor of represent and how to use it with on HTML Parser
HTML Parser to use is BeautifulSoup: one of the best xml and html parsers
"""
import requests
from requests.exceptions import HTTPError
import sys      # allows me to grab arguments


if __name__ == '__main__':
    for url in sys.argv[1:]:
        if not url.lower().startswith('http'):
            url = f'https://{url}'
        try:
            response = requests.get(url)

            print(f"Yeah! worked!\n\n{response.raise_for_status()}")
        except HTTPError as httperr:
            print(f"HTTP error: {httperr}")
        except Exception as err:
            print(f"Something went really wrong: {err}")

    # google = (requests.get('https://www.google.com'))
    # if google:
    #     print(f"Yeah! worked! \n \n{google.content}")
    # else:
    #     print(f"Some error Occurred\nError: {google.status_code}")




