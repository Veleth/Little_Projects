import hashlib
import os
import re
import time
from datetime import datetime
from typing import NoReturn

import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

def notify(url: str) -> NoReturn:
    now = datetime.now()
    pushover_url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': os.getenv('PUSHOVER_TOKEN'),
        'user': os.getenv('PUSHOVER_USER'),
        'message': f'{url} UPDATED'
    }

    response = requests.post(pushover_url, data=data, timeout=30)
    if response.status_code == 200:
        print(f'{now} Notification sent successfully!')
    else:
        print('Failed to send notification.')

def fetch_local_data(filename: str) -> str:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ''

def store_data(filename, contents: str) -> NoReturn:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(contents)

def generate_hash(value: str) -> str:
    encoded = value.encode()
    md5 = hashlib.md5(encoded)
    return md5.hexdigest()


def check_website(url: str) -> NoReturn:
    response = requests.get(url, timeout=30)
    url_without_protocol = url.split('//')[1] if '//' in url else url
    filename = re.sub(r'\W+', '_', url_without_protocol)
    soup = BeautifulSoup(response.text, 'html.parser')
    visible_text = soup.get_text()
    current_hash = generate_hash(visible_text)
    stored_hash = fetch_local_data(filename)
    print(f'Content fetched from {url}. Hash: {current_hash}')
    if current_hash != stored_hash:
        print(f'Hash does not match the old hash, {stored_hash}. Storing new hash and sending notification.')
        store_data(filename, current_hash)
        notify(url)

if __name__ == '__main__':
    websites = os.getenv('WEBSITES')
    if not websites:
        print('No websites configured. Exiting.')
        exit()

    websites = [site for site in websites.split(',') if site]
    while True:
        for website in websites:
            check_website(website)
        time.sleep(int(os.getenv('TIMEOUT', 900)))
