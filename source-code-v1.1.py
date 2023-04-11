# Source Generated with Decompyle++
# File: SUIT.pyc (Python 3.10)

import os
import json
import requests
print('SUIT Client v1.0 (CC0 software): A way to use SUI without the trouble!\xe2\x84\xa2')
if not os.path.exists('suit-cache.json'):
    print("It appears that the cache file (suit-cache.json) doesn't exist. To prevent crashing, a new one will be generated. \n")
    with open('suit-cache.json', 'w') as cachefile:
        cachefile.write(json.dumps({
            'pppdud': 'is the best' }))
    print('Cache file regenerated. \n')
print('Loading cache..')
cachefile = open('suit-cache.json', 'r')
print('Extracting JSON data..')
cachefile = json.loads(cachefile.read())
username = input('Please type in a username or ID here: ')
with open('suit-cache.json', 'w') as cache_file_data:
    try:
        if username in cachefile:
            print('Username found in cache. Loading data..')
            print(cachefile[username])
        elif json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_id/{username}''').text)['Error'] == False:
            print('Info available online. Downloading data..')
            cachefile[json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_id/{username}''').text)['Username']] = json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_id/{username}''').text)['ID']
            print(cachefile[username])
        elif json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_user/{username}''').text)['Error'] == False and username not in list(cachefile.values()):
            print('ID available online but not downloaded. Downloading ID..')
            print(json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_user/{username}''').text)['Username'])
            cachefile[json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_user/{username}''').text)['Username']] = json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_user/{username}''').text)['ID']
        elif json.loads(requests.get(f'''https://sui.sid72020123.repl.co/get_user/{username}''').text)['Error'] == False and username in list(cachefile.values()):
            print('ID stored in cache. Loading data..')
            print(list(cachefile.keys())[list(cachefile.values()).index(username)])
        else:
            print('Username or ID not found.')
    finally:
        pass
    cache_file_data.write(json.dumps(cachefile))

