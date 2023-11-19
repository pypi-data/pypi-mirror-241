import os
import sys
from tqdm import tqdm
from pyfiglet import figlet_format
from subprocess import Popen, PIPE
from tgpirobot.tgpirobot import run_bot, version

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

    # Use Popen to capture output for tqdm
    process = Popen(["pip", "install", "--upgrade", "tgpirobot"], stdout=PIPE, stderr=PIPE, text=True)
    with tqdm(total=100, desc="Progress", unit="%", dynamic_ncols=True) as pbar:
        for line in process.stderr:
            if "ERROR" in line:
                print("Update failed. Please check the error message.")
                return
            # Parse progress from the output
            if "Downloading" in line or "Installing" in line:
                progress = int(line.split("%")[0].split()[-1])
                pbar.update(progress - pbar.n)
    
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
