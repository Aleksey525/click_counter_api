import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv
import os
import argparse
import sys


def shorten_link(token: str, url: str) -> str:
    headers = {'Authorization': token}
    data = {'long_url': url}
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(api_url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(bitlink: str, token: str) -> str:
    headers = {'Authorization': token}
    payload = {'units': '-1'}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    splited_url = urlsplit(bitlink)
    bitlink_atr = f'{splited_url.netloc}{splited_url.path}'
    complite_url = url_template.format(bitlink_atr)
    response = requests.get(complite_url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url: str, token: str) -> bool:
    splited_url = urlsplit(url)
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    url_atr = f'{splited_url.netloc}{splited_url.path}'
    complite_url = url_template.format(url_atr)
    headers = {'Authorization': token}
    response = requests.get(complite_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(
        description='Приложение для сокращения ссылок и получения количества кликов по ним'
    )
    parser.add_argument('link', help='user link')
    args = parser.parse_args()
    if is_bitlink(args.link, token):
        try:
            clicks = count_clicks(args.link, token)
        except requests.exceptions.HTTPError:
            print(f'Введен некорректный адрес1')
        else:
            print(f'По вашей ссылке прошли {clicks} раз(а)')
    else:
        try:
            shorten_bitlink = shorten_link(token, args.link)
        except requests.exceptions.HTTPError:
            print(f'Введен некорректный адрес')
        else:
            print(f'Битлинк: {shorten_bitlink}')


if __name__ == '__main__':
    main()
