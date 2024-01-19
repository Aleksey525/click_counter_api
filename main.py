import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv
import os
import json

load_dotenv()

token = os.getenv('TOKEN')


def shorten_link(token: str, url: str) -> str:
    headers = {'Authorization': token}
    data = {'long_url': url}
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(api_url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def valid_url(link: str) -> None:
    response = requests.get(link)
    response.raise_for_status()
    return None


def count_clicks(token: str, bitlink: str) -> str:
    headers = {'Authorization': token}
    payload = {'units': '-1'}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    splited_url = urlsplit(bitlink)
    complite_url = url_template.format(splited_url[1] + splited_url[2])
    response = requests.get(complite_url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url: str) -> bool:
    is_bitlink = False
    test = urlsplit(url)
    if test[1] == 'bit.ly':
        is_bitlink = True
    return is_bitlink
if __name__ == '__main__':
    user_url = input('Введите ссылку: ')
    if is_bitlink(user_url):
        try:
            valid = valid_url(user_url)
            count_clicks = count_clicks(token, user_url)
        except requests.exceptions.ConnectionError:
            print(f'Введен некорректный адрес')
        except requests.exceptions.HTTPError:
            print(f'Запрос завершился неудачно')
        else:
            print(f'По вашей ссылке прошли {count_clicks} раз(а)')
    else:
        try:
            valid = valid_url(user_url)
            shorten_bitlink = shorten_link(token, user_url)
        except requests.exceptions.ConnectionError:
            print(f'Введен некорректный адрес')
        except requests.exceptions.HTTPError:
            print(f'Запрос завершился неудачно')
        else:
            print(f'Битлинк: {shorten_bitlink}')




