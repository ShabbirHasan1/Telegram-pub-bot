import time
from telethon import TelegramClient, events, sync
from pystyle import *
import sys
from datetime import datetime


banner = '''
            ████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
            ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
               ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
               ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
               ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
               ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                     --> By @loTus405 <--                    v1.1              
                                                                     '''

COLA = Col.light_blue
N4ME = "Telegram AutoPUB"

print(Colorate.Vertical(Colors.cyan_to_blue, banner))

def makeInput(que=''):
    print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
    a = input(f"{COLA}╚{Col.reset} root@root {COLA}>>{Col.reset} ")
    return a

def animated_print(arg1):
    sys.stdout.flush()
    sys.stdout.write(f"\r{arg1}")

def GetConfig():
    try:
        f = open("config/account.txt", "r")
        lines = f.readlines()
        for li in lines:
            li = li.replace("\n", "")
            if "api_id" in li:
                a = li.replace("api_id", "").replace(" ", "").replace("=", "").replace("\n", "")
                # print(li.split())
                # li.replace("=", "")
                api_id = a
            elif "api_hash" in li:
                a = li.replace("api_hash", "").replace(" ", "").replace("=", "").replace("\n", "")
                # print(li.split())
                if li == "X":
                    return False, False
                api_hash = a
        return api_id, api_hash
    except:
        return None, None

def GetChannels(client):
    try:
        f = open("config/channels.txt", "a", encoding="utf8")
    except:
        return False

    print()
    for dialog in client.iter_dialogs():
        if "-" in str({dialog.id}) and len(str(dialog.id)) > 12:
            # print(f'{dialog.id} - {dialog.title}')

            print(f"{COLA}[{Col.reset}+{COLA}]{Col.reset} Channel ID: {Col.cyan}{dialog.id}{Col.reset} Channel Name: {Col.light_blue}{dialog.title}{Col.reset}")
            f.write(f'{dialog.id} - {dialog.title}\n')
    print()
    return True

def LoadChannels():
    listchan = []
    try:
        f = open("config/channels.txt", "r", encoding='utf8')
        lines = f.readlines()

        for li in lines:
            li = li.replace("\n", "")

            idd = li.split(" - ")[0]
            listchan.append(idd)
        return listchan
    except:
        return False

def help():
    print(f'''
    HELP COMMANDS
    -------------

    .message    {COLA}|{Col.reset} see saved message
    .account    {COLA}|{Col.reset} see saved account
    .channels   {COLA}|{Col.reset} load channels and save them
    .pub <time> {COLA}|{Col.reset} start the bot with a delay, example: {Col.cyan}.pub 2h{Col.reset}

    ''')

def GetMessage():
    try:
        f = open("config/pub.txt", "r", encoding="utf8")
        text = f.read()
        return text
    except:
        return False

def pub(tis, message, client, channels):
    while True:
        good, bad = 0,0
        for channel in channels:
            now = datetime.now()
            ti = now.strftime("%H:%M:%S")
            try:
                entity = client.get_entity(int(channel))
                client.send_message(entity=entity, message=message)
                good += 1
            except:
                bad += 1
            animated_print(f"[{Col.cyan}{ti}{Col.reset}] {COLA}[{Col.reset}*{COLA}]{Col.reset} Sending to {channel} Sent: {Col.cyan}{good}{Col.reset}/{len(channels)}{COLA}.{Col.reset}")
        print()
        time.sleep(tis)

def convertTime(time):
    # litle algo i did a few years ago
    time2 = time.replace(" ", "")
    time2 = time2.replace("s", "s ").replace("mi", "mi ").replace("h", "h ").replace("d", "d ").replace("M", "M ").replace("y", "y ")
    time2 = time2.split(" ")
    arguments = len(time2)
    arg = 0
    sec = 0
    while arg < arguments:
        if "s" in time2[arg]:
            amount = int(time2[arg].replace("s", ''))
            sec += amount
        elif "m" in time2[arg]:
            amount = time2[arg].replace("m", '')
            amount = int(amount)*60
            sec += amount
        elif "h" in time2[arg]:
            amount = int(time2[arg].replace("h", ''))*60*60
            sec += amount
        else:
            try:
                amount = int(time2[arg].replace("s", ''))
                sec += amount
            except:
                pass
        arg += 1
    sec = round(sec, 2)
    return sec


api_id, api_hash = GetConfig()
if not api_id:
    print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
    print(f"{COLA}║{Col.reset} Edit /config/account.txt with your API information{COLA}.{Col.reset} ")
    input(f"{COLA}╚{Col.reset} Your API Information can be find here: https://my.telegram.org{COLA}.{Col.reset} \n")
    sys.exit()
elif api_id == None:
    print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
    input(f"{COLA}╚{Col.reset} Could not open /config/account.txt to get API information{COLA}.{Col.reset} ")
    sys.exit()

client = TelegramClient('session_name', api_id, api_hash)
client.start()

while True:
    cmd = makeInput()

    if cmd == ".message":
        textt = GetMessage()
        if not textt:
            print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
            print(f"{COLA}╚{Col.reset} Could not open /config/pub.txt to get Message{COLA}.{Col.reset} ")
        else:
            print(f"\n{COLA}[{Col.reset}*{COLA}]{Col.reset} Saved Message {COLA}${Col.reset}")
            print()
            print(textt)
            print()

    elif cmd == ".account":
        print(f"\n{COLA}[{Col.reset}*{COLA}]{Col.reset} Saved Account {COLA}${Col.reset}")
        print(f'''   {COLA}[{Col.reset}+{COLA}]{Col.reset} API ID -> {api_id}
   {COLA}[{Col.reset}+{COLA}]{Col.reset} API HASH -> {api_hash}''')


    elif cmd == ".channels":
        cn = GetChannels(client)
        if not cn:
            print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
            print(f"{COLA}╚{Col.reset} Could not open /config/channels.txt to get USER Channels{COLA}.{Col.reset} ")
        else:
            print(f"{COLA}[{Col.reset}*{COLA}]{Col.reset} Channel saved to /config/channels.txt {COLA}${Col.reset}")
            print(f"{COLA}[{Col.reset}*{COLA}]{Col.reset} Open this file to edit channels to send the publicity {COLA}${Col.reset}")            

    elif cmd == ".exit": sys.exit()

    elif ".pub " in cmd:
        argt = cmd.replace(".pub ", "")
        ts = convertTime(argt)
        if ts < 60*5: ts = 60*5

        listchan = LoadChannels()
        if not listchan:
            print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
            print(f"{COLA}╚{Col.reset} Could not open /config/channels.txt to get Channels ID{COLA}.{Col.reset} ")
        else:
            textt = GetMessage()
            if not textt:
                print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
                print(f"{COLA}╚{Col.reset} Could not open /config/pub.txt to get Message{COLA}.{Col.reset} ")
            else:
                print(f"\n{COLA}╔{Col.reset} {Col.cyan}{N4ME} ~ By loTus04{Col.reset} {COLA}${Col.reset}")
                print(f"{COLA}║{Col.reset} Bot is ready{COLA}.{Col.reset} ")
                input(f"{COLA}╚{Col.reset} Channels: {len(listchan)} | Message: {textt.splitlines()[0]}... | Delay: {ts}s || READY ?{COLA}.{Col.reset} \n")
                pub(ts, textt, client, listchan)
    
    elif cmd == ".help":
        help()

