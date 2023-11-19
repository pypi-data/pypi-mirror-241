import time
import re 
import json
import random
import os
import requests
import sys
import asyncio
from pkg_resources import resource_string
from pyrogram import Client, filters
from pyfiglet import figlet_format

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
    print("Welcome to tgpirobot configuration setup.")  
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

    print("Configuration saved in configs.json. You can now run tgpirobot -r.")

def load_config():
    with open(CONFIG_FILE) as config_file:
        config_data = json.load(config_file)

    api_id = config_data.get('API_ID')
    api_hash = config_data.get('API_HASH')
    debug_mode = config_data.get('DEBUG_MODE', '').lower() == 'true'

    start_bot(api_id, api_hash, debug_mode)

def start_bot(api_id, api_hash, debug_mode):
    app = Client("tgpirobot", api_id=api_id, api_hash=api_hash)

    sender_list = {}
    blocked_users = set()

    @app.on_message(filters.private & ~filters.bot)
    async def handle_new_message(client, message):
        try:
            me = await client.get_me()
        except Exception:
            print("Error getting user information. Retrying...")
            return

        proceed_auto_reply = (
            debug_mode or 
            (not me.status == "online" and not message.from_user.is_bot)
        )

        if proceed_auto_reply:
            time.sleep(1)
            user_id = message.from_user.id
            username = message.from_user.username

            if user_id in blocked_users:
                await message.reply("You have been blocked by master for 1 minute, due to flood.")
                return

            sender_list.setdefault(user_id, 0)
            sender_list[user_id] += 1

            flood_attempts_left = FLOOD_LIMIT - sender_list[user_id]

            if flood_attempts_left > 0:
                piro = flood_attempts_left
            elif flood_attempts_left == 0:
                blocked_users.add(user_id)
                sender_list.pop(user_id, None)
                await message.reply("You have been blocked by master for 1 minute, due to flood.")
                await app.block_user(user_id)
                await asyncio.sleep(FLOOD_DURATION) 
                await app.unblock_user(user_id)
                blocked_users.remove(user_id)

            # Auto-reply logic
            reply_msg = ""
            if sender_list[user_id] < 2:
                reply_msg = (
                    f"**AUTO REPLY**\n\nHi @{username},\n\nI'm sorry, my boss is currently offline. Please wait for a moment."
                    f"\n\nFeel free to check out [HK4CRPRASAD](https://github.com/hk4crprasad) while waiting."
                    f"\n\n**AUTO REPLY**"
                )
            elif sender_list[user_id] < 3:
                reply_msg = f"**AUTO REPLY**\n\nPlease be patient, @{username}, my boss is still offline 😒"
            elif sender_list[user_id] < 4:
                reply_msg = f"**AUTO REPLY**\n\n@{username}, Please bear with us 😅" 
            else:
                random_number = random.randint(0, len(quizzes()) - 1)
                question = quizzes()[random_number]['question']
                answer = quizzes()[random_number]['answer']
                reply_msg = (
                    f"**AUTO REPLY**\n\n@{username}, How about playing a guessing game? 😁\n\n"
                    f"{question}\n\n{answer}\n\n"
                )

            if reply_msg:
                reply_msg += f"\n\nFlood attempt left: {piro}"
                await message.reply(reply_msg)

            # Print user information
            date = message.date.strftime('%a %b %d %H:%M:%S %Y')            
            print(
                f"\033[91mUser name\033[0m :- \033[94m@{username if username else 'None'}\033[0m\n" 
                f"\033[93mUser id\033[0m :- \033[94m{user_id}\033[0m\n"
                f"\033[92mDate\033[0m :- \033[94m{date}\033[0m\n"
                f"\033[96mMessage\033[0m :- \033[94m{message.text if message.text else ''}\033[0m\n"
            )

            # Send message to user
            message_text = (
                f"User%20name%20%3A-%20@{username if username else 'None'}%0AUser%20id%20%3A-%20{user_id}%0ADate%20%3A-%20{date}%0AMessage%20%3A-%20{message.text.replace(' ', '%20') if message.text else ''}"
            )
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={me.id}&text={message_text}' 
            response = requests.get(url)

    app.run()

