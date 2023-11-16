#!/data/data/com.termux/files/usr/bin/python3
from telethon import TelegramClient, events, Button
from time import sleep
import requests
import telethon
import json
import itertools
import asyncio
import argparse

def get_config():
    api_id = input("Enter your api_id: ")
    api_hash = input("Enter your api_hash: ")
    max_flood_attempts = int(input("Enter max_flood_attempts: "))
    image_url = input("Enter image URL: ")
    message_intro = input("Enter message intro: ")

    config_data = {
        "api_id": api_id,
        "api_hash": api_hash,
        "max_flood_attempts": max_flood_attempts,
        "image_url": image_url,
        "message_intro": message_intro
    }
    with open('configs.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    print("Configurations saved in configs.json")

def load_configs():
    try:
        with open('configs.json', 'r') as config_file:
            config_data = json.load(config_file)
            api_id = config_data.get("api_id", '')
            api_hash = config_data.get("api_hash", '')
            max_flood_attempts = config_data.get("max_flood_attempts", 5)
            image_url = config_data.get("image_url", '')
            message_intro = config_data.get("message_intro", '')
        return api_id, api_hash, max_flood_attempts, image_url, message_intro
    except FileNotFoundError:
        get_config()
        print("Error: Configs file not found. Run 'pirobot -h' for help.")
        return None, None, None, None, None

api_id, api_hash, max_flood_attempts, image_url, message_intro = load_configs()

def print_help():
    print("pirobot - Telegram Flood control Script")
    print("Author: HK4CRPRASAD (GitHub: https://github.com/hk4crprasad/pirobot)")
    print("Usage:")
    print("  pirobot -h   : Show this help message")
    print("  pirobot -r   : Run the Telegram bot")
    print("\nFlood Control Functionality:")
    print("  The bot includes flood control functionality to prevent spam.")
    print("  If a user exceeds the maximum allowed flood attempts, the bot will block them temporarily.")
    print("  Configuration for flood control can be set in the `get_config` function.")
    print("\nConfiguring the User:")
    print("  To configure the User, run the script and follow the prompts.")
    print("  You will be asked to enter your api_id, api_hash, max_flood_attempts, image URL, and message intro.")
    print("  The configurations will be saved in the 'configs.json' file.")


client = TelegramClient('user', api_id, api_hash).start()
response = requests.get(image_url)

with open('fetched_image.png', 'wb') as file:
    file.write(response.content)

online = True
offline_user_ids = set()

try:
    with open('/sdcard/nonblock.json', 'r') as nonblock_file:
        nonblock_user_ids = set(json.load(nonblock_file))
except FileNotFoundError:
    nonblock_user_ids = set()


async def confirm_block(user_id):
    return True  # Always block

@client.on(events.UserUpdate)
async def handle_update(event):
    global online
    try:
        user = await event.client.get_me()
        online = getattr(user.status, 'online', False)
    except telethon.errors.rpcbaseerrors.TimedOutError:
        print("Timed out while getting user information. Retrying...")

@client.on(events.NewMessage())
async def handler(event):
    global online
    global flood_counter
    global offline_user_ids
    global nonblock_user_ids
    sender_id = event.message.from_id

    try:
        if sender_id is None:
            print("Error: Sender ID is None.")
            return

        sender_id_str = str(sender_id)

        if sender_id_str in excluded_channel_ids or sender_id_str in nonblock_user_ids:
            return

        if not online:
            offline_user_ids.add(sender_id_str)
        if sender_id_str in flood_counter:
            flood_counter[sender_id_str] += 1
        else:
            flood_counter[sender_id_str] = 1

        if flood_counter[sender_id_str] > max_flood_attempts:
            print(f"Warning: User {sender_id_str} exceeded maximum allowed flood attempts. Blocking...")

            if await confirm_block(sender_id_str):
                if sender_id_str not in nonblock_user_ids:
                    try:
                        await client(telethon.tl.functions.contacts.BlockRequest(sender_id))
                    except Exception as e:
                        print(f"Unexpected error: {e}")
                else:
                    print(f"User {sender_id_str} is in the nonblock list. Not blocking.")

                await asyncio.sleep(60)  # Unblock after 1 minute
                flood_counter[sender_id_str] = 0

                try:
                    await client(telethon.tl.functions.contacts.UnblockRequest(sender_id))
                except Exception as e:
                    print(f"Unexpected error during unblocking: {e}")

                return

        else:
            try:
                await asyncio.sleep(2)
                ram = await client.send_message(
                    event.chat_id,
                    message_intro + "⠋",
                    file="fetched_image.png",
                    buttons=[
                        [Button.url("Share now", url=f"https://t.me/share/url?url={event.message.id}")]
                    ]
                )

                previous_message_content = None
                user_entity = await client.get_entity(sender_id)
                for progress in itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]):
                    if online:
                        print("You are online! Script paused.")
                        break
                    sleep(0.5)
                    update_message = (
                        message_intro +
                        f"Progress: {progress}\nFlood Attempts Left: {max_flood_attempts - flood_counter[sender_id_str]}"
                    )
                    if update_message != previous_message_content:
                        try:
                            await ram.edit(update_message)
                        except telethon.errors.rpcerrorlist.MessageIdInvalidError:
                            print("Error: Invalid message ID while editing. Skipping.")
                        previous_message_content = update_message
            except telethon.errors.rpcbaseerrors.ForbiddenError as e:
                print("ForbiddenError: Writing messages is not allowed in this chat.")
            except telethon.errors.rpcerrorlist.UserPrivacyRestrictedError:
                print("Error: User privacy settings restrict blocking.")
            except telethon.errors.rpcerrorlist.ChatAdminRequiredError:
                print("Error: Admin privileges required to block user in the chat.")
            except telethon.errors.rpcerrorlist.FloodWaitError as e:
                print(f"FloodWaitError: You are blocked from performing this action. Retry in {e.seconds} seconds.")
            except ValueError as e:
                print(f"Error: {e}")

    except telethon.errors.rpcbaseerrors.ForbiddenError as e:
        if "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e):
            print("ForbiddenError: Sending photos is not allowed in this chat.")
        else:
            print(f"ForbiddenError: {e}")

def main():
    parser = argparse.ArgumentParser(description='Telegram Flood Control Script')
    parser.add_argument('-r', '--run', action='store_true', help='Run the Telegram Account')
    parser.add_argument('-h', '--help', action='store_true', help='Show help message')

    args = parser.parse_args()

    if args.help:
        print_help()
    elif args.run:
        print("Press Ctrl+C to exit")
        client.run_until_disconnected()
    else:
        print("Invalid command. Use 'pirobot -h' for help.")
