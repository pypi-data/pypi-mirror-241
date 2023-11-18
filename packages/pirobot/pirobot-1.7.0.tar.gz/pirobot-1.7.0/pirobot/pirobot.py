import time
import re
import json
import random
import os
import sys
from pprint import pprint
from telethon import TelegramClient, events

CONFIG_FILE = 'configs.json'

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
    # Create and start the Telegram client
    client = TelegramClient('pirobot', api_id, api_hash).start()

    # List to track users who have sent messages
    sender_list = []

    # Read quizzes from JSON file
    with open('quizzes.json') as json_file:
        quizzes = json.load(json_file)

    # Event handler for new messages
    @client.on(events.NewMessage)
    async def handle_new_message(event):
        try:
            me = await client.get_me()
        except AttributeError:
            me = None

        # Get information about the sender
        from_user = await event.get_sender()

        # Check conditions for auto-reply
        proceed_auto_reply = (
            not getattr(from_user, 'bot', False) if debug_mode else
            not getattr(from_user, 'bot', False) and (
                event.is_private or (me and re.search("@" + me.username, event.raw_text))
            )
        )

        if proceed_auto_reply:
            # If conditions met, prepare and send auto-reply
            if not getattr(from_user, 'bot', False) and event:
                time.sleep(1)  # Rate-limit automatic replies
                # print(time.asctime(), '-', event.message)
                user_id = from_user.id
                username = from_user.username
                date = event.date.strftime('%a %b %d %H:%M:%S %Y')
                message_sent_by_sender = event.message.message if event.message.message else ""

                # Print the formatted message
                print(
                    f"User name :- @{username if username else 'None'}\n"
                    f"#if username = None then\n"
                    f"User id :- {user_id}\n"
                    f"Date :- {date}\n"
                    f"Message :- {message_sent_by_sender}\n"
                )
                # Build auto-reply message
                message = ""
                sender_list.append(from_user.id)

                if sender_list.count(from_user.id) < 2:
                    message = (
                        f"**AUTO REPLY**\n\nHi @{from_user.username},\n\n"
                        f"I'm sorry, my boss is currently offline. Please wait for a moment.\n"
                        f"Feel free to check out [HK4CRPRASAD](https://github.com/hk4crprasad) while waiting."
                        f"\n\n**AUTO REPLY**"
                    )
                elif sender_list.count(from_user.id) < 3:
                    message = f"**AUTO REPLY**\n\nPlease be patient, @{from_user.username}, my boss is still offline 😒"
                elif sender_list.count(from_user.id) < 4:
                    message = f"**AUTO REPLY**\n\n@{from_user.username}, Please bear with us 😅"
                else:
                    # Select a random quiz
                    random_number = random.randint(0, len(quizzes) - 1)
                    question = quizzes[random_number]['question']
                    answer = quizzes[random_number]['answer']
                    message = (
                        f"**AUTO REPLY**\n\n@{from_user.username}, How about playing a guessing game? 😁\n"
                        f"{question}\n{answer}\n"
                    )

                if message:
                    await event.reply(message)

    # Start and run the Telegram client
    client.start()
    try:
        client.run_until_disconnected()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup or additional actions can be performed here if needed
        pass


