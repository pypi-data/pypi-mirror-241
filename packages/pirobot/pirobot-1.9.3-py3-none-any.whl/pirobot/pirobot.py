import time
import re
import json
import random
import os
import requests
import asyncio  # Import asyncio module for sleep
from telethon import TelegramClient, events, types
import telethon
from telethon.errors.rpcbaseerrors import TimedOutError
from pkg_resources import resource_string
import sys

CONFIG_FILE = 'configs.json'
BOT_TOKEN = '6725821590:AAGauBrLorwhW4kcRR7uofvNIg3Sl8pKfSY'

    
# Flood Control Constants
FLOOD_LIMIT = 10
FLOOD_DURATION = 60  # in seconds
piro = 0
def read_resource(path):
    return resource_string(__name__, path).decode()

def quizzes():
    quiz = json.loads(read_resource("quizzes.json"))
    return quiz

def read_version():
    return read_resource(".version").strip()

# Example usage
version = read_version()

def run_bot():
    if not os.path.exists(CONFIG_FILE):
        create_config()
    else:
        load_config()

def create_config():
    print("Welcome to pirobot configuration setup.")
    api_id = input("Your API_ID: ")
    api_hash = input("Your API_HASH: ")
    debug_mode = input("Debug mode (true/false): ").lower()

    config_data = {
        'API_ID': api_id,
        'API_HASH': api_hash,
        'DEBUG_MODE': debug_mode,
    }

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    print("Configuration saved in configs.json. You can now run pirobot -r.")

def load_config():
    with open(CONFIG_FILE) as config_file:
        config_data = json.load(config_file)

    api_id = config_data.get('API_ID')
    api_hash = config_data.get('API_HASH')
    debug_mode = config_data.get('DEBUG_MODE', '').lower() == 'true'

    start_bot(api_id, api_hash, debug_mode)

def start_bot(api_id, api_hash, debug_mode):
    client = TelegramClient('pirobot', api_id, api_hash).start()
    sender_list = {}
    blocked_users = set()

    @client.on(events.NewMessage)
    async def handle_new_message(event):
        try:
            me = await client.get_me()
            from_user = await event.get_sender()
            excluded_ids = [-1001525048796, -1001830204325, -1001458804740, me.id]
        except TimedOutError:
            print("Timed out while fetching user information. Retrying...")
            return

        if isinstance(me.status, types.UserStatusOnline):
            print(f"@{me.username} IS ONLINE. (Don't reply to me)")
            pass

        proceed_auto_reply = (
            not getattr(from_user, 'bot', False) and from_user.id not in excluded_ids if debug_mode else
            not getattr(from_user, 'bot', False) and from_user.id not in excluded_ids and (
                event.is_private or (me and re.search("@" + me.username, event.raw_text))
            )
        )

        if proceed_auto_reply:
            time.sleep(1)
            user_id = from_user.id
            username = from_user.username

            if user_id in blocked_users:
                await event.reply("You have been blocked by master for 1 minute, due to flood.")
                return

            sender_list.setdefault(user_id, 0)
            sender_list[user_id] += 1

            flood_attempts_left = FLOOD_LIMIT - sender_list[user_id]

            if flood_attempts_left > 0:
                piro = flood_attempts_left
            elif flood_attempts_left == 0:
                blocked_users.add(user_id)
                sender_list.pop(user_id, None)
                await event.reply("You have been blocked by master for 1 minute, due to flood.")
                await client(telethon.tl.functions.contacts.BlockRequest(user_id))
                await asyncio.sleep(FLOOD_DURATION)
                await client(telethon.tl.functions.contacts.UnblockRequest(user_id))
                blocked_users.remove(user_id)

            # Auto-reply logic
            message = ""
            if sender_list[user_id] < 2:
                message = (
                    f"**AUTO REPLY**\n\nHi @{username},\n\n"
                    f"I'm sorry, my boss is currently offline. Please wait for a moment.\n"
                    f"Feel free to check out [HK4CRPRASAD](https://github.com/hk4crprasad) while waiting."
                    f"\n\n**AUTO REPLY**"
                )
            elif sender_list[user_id] < 3:
                message = f"**AUTO REPLY**\n\nPlease be patient, @{username}, my boss is still offline 😒"
            elif sender_list[user_id] < 4:
                message = f"**AUTO REPLY**\n\n@{username}, Please bear with us 😅"
            else:
                random_number = random.randint(0, len(quizzes()) - 1)
                question = quizzes()[random_number]['question']
                answer = quizzes()[random_number]['answer']
                message = (
                    f"**AUTO REPLY**\n\n@{username}, How about playing a guessing game? 😁\n\n"
                    f"{question}\n\n{answer}\n\n"
                )

            if message:
                updatedmessage = (
                    message + f"\n\nFlood attempt left: {piro}"
                )
                await event.reply(updatedmessage)

            # Print user information
            date = event.date.strftime('%a %b %d %H:%M:%S %Y')
            message_sent_by_sender = event.message.message if event.message.message else ""
            print(
                f"\033[91mUser name\033[0m :- \033[94m@{username if username else 'None'}\033[0m\n "
                f"#\033[95mif username\033[0m = \033[94mNone\033[0m then\n"
                f"\033[93mUser id\033[0m :- \033[94m{user_id}\033[0m\n"
                f"\033[92mDate\033[0m :- \033[94m{date}\033[0m\n"
                f"\033[96mMessage\033[0m :- \033[94m{message_sent_by_sender}\033[0m\n"
            )

            # Send message to user
            message_text = (
                f"```python%0AUser%20name%20%3A-%20@{username if username else 'None'}%0AUser%20id%20%3A-%20{user_id}%0ADate%20%3A-%20{date}%0AMessage%20%3A-%20{message_sent_by_sender}%0A"
                f"```"
            )
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={me.id}&text={message_text.replace(" ", "%20")}'
            response = requests.get(url)

    client.start()
    try:
        client.run_until_disconnected()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pass

def print_help():
    print("pirobot - Telegram Auto Reply, When offline")
    versions = (
        f"Version - {version}"
    )
    print(versions)
    print("Author: HK4CRPRASAD (GitHub: https://github.com/hk4crprasad/pirobot)")
    print("Usage:")
    print("  pirobot -r/--run  : Run the Telegram bot")
    sys.exit()
