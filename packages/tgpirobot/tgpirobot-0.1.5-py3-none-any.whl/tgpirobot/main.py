import os
import sys
import time
from tqdm import tqdm
import subprocess
from pyfiglet import figlet_format
from subprocess import Popen, PIPE
from tgpirobot.tgpirobot import run_bot, version
from rich import print
from rich.console import Console
from rich.progress import Progress
from inquirer import List, prompt

def print_help():
      # Print banner   
      print(figlet_format('tgpirobot', font='standard'))
    
      print(f'''
      tgpirobot - Auto-reply app for Telegram
    
      Version: {version}
      Author: HK4CRPRASAD (https://github.com/hk4crprasad)
      
      tgpirobot lets you auto-reply to messages on Telegram when you are offline!
    
      Features:
    
      - Send automatic replies
      - Blocks spammers
      - Includes jokes, quotes etc
      
      Usage:
      
      tgpirobot -r/--run   Run tgpirobot
      tgpirobot -piro/--piro   Show help message
      
      tgpirobot is licensed under the GPL-3.0.
      See https://github.com/hk4crprasad/tgpirobot for more info.
      ''')
      sys.exit()

def update_bot():
    print("Updating tgpirobot...")

    with Progress() as progress:
        task = progress.add_task("[cyan]Progress...", total=100)

        # Run pip install in the background
        pip_process = subprocess.Popen(["pip", "install", "--upgrade", "tgpirobot"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for i in range(1, 101):
            progress.update(task, completed=i)
            time.sleep(0.4)  # Adjust sleep duration to match your desired speed

        # Wait for the pip process to complete
        pip_process.communicate()

    print("Update complete.")

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['-r', '--run', 'run']:
            run_bot()
        elif arg in ['--piro', '-piro', 'piro']:
            print_help()
        elif arg in ['-u', '--update', 'update']:
            update_bot()
        else:
            print("Invalid arguments. Use --piro/-piro/piro for help, -r/--run/run to run the bot, or -u/--update/update to update the bot.")
    else:
        print("Invalid arguments. Use --piro/-piro/piro for help, -r/--run/run to run the bot, or -u/--update/update to update the bot.")


if __name__ == "__main__":
    main()
