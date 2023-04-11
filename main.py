import os
import json
import requests


print('Tuxedo (CC0 software): A way to use SUI without the trouble!')


if not os.path.exists('suit-cache.json'):
    try:
        with open('suit-cache.json', 'w') as cachefile:
            cachefile.write(json.dumps({
                'TuxedoVersion': 'v0.0.1'
            }))
            print('Cache file regenerated. \n')
    except Exception as e:
        print("An error occurred while attempting to generate the cache file: {}".format(e))


if os.path.exists('suit-cache.json'):
    cachefile = open('suit-cache.json', 'r')
    print('Extracting JSON data..')
    try:
        cachefile = json.loads(cachefile.read())
    except ValueError as e:
        print('Error parsing JSON data: {}'.format(e))
    finally:
        cachefile.close()

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
