from dotenv import load_dotenv
from datetime import datetime
import os
import hashlib
import time
import requests
from ekwFetcher import EkwFetcher

load_dotenv()
fetcher = EkwFetcher()

def storeData(contents: str):
    with open('hash', 'w') as f:
        f.write(contents)
    
def checkLocalData() -> str:
    try:
        with open('hash', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

def generateHash(input: str) -> str:
    encoded = input.encode()
    hash = hashlib.md5(encoded)
    return hash.hexdigest()

def notify():
    # Notification via Pushover
    now = datetime.now()
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': os.getenv('PUSHOVER_TOKEN'),
        'user': os.getenv('PUSHOVER_USER'),
        'message': 'TEST: EKW UPDATED'
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print(f'{now} Notification sent successfully!')
    else:
        print('Failed to send notification.')

if __name__ == '__main__':
    websiteContents = fetcher.fetchContents(os.getenv('EKW_DEPARTMENT'), os.getenv('EKW_REGISTRY_NUMBER'), os.getenv('EKW_CONTROL_DIGIT'))
    hash = generateHash(websiteContents)
    storedHash = checkLocalData()
    if hash != storedHash:
        storeData(hash)
        notify()
    time.sleep(int(os.getenv('TIMEOUT')))



