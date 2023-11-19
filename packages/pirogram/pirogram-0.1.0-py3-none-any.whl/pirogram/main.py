import sys
from pirogram.pirogram import run_bot, version
from pyfiglet import figlet_format

def print_help():
      # Print banner   
      print(figlet_format('Pirogram', font='standard'))
    
      print(f'''
      Pirogram - Auto-reply app for Telegram
    
      Version: {version}
      Author: HK4CRPRASAD (https://github.com/hk4crprasad)
      
      Pirogram lets you auto-reply to messages on Telegram when you are offline!
    
      Features:
    
      - Send automatic replies
      - Blocks spammers
      - Includes jokes, quotes etc
      
      Usage:
      
      pirogram -r/--run   Run Pirogram
      pirogram -piro/--piro   Show help message
      
      Pirogram is licensed under the GPL-3.0.
      See https://github.com/hk4crprasad/pirogram for more info.
      ''')
      sys.exit()


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['-r', '--run', 'run']:
            run_bot()
        elif arg in ['--piro', '-piro', 'piro']:
            print_help()
        else:
            print("Invalid arguments. Use --piro/-piro/piro for help or -r/--run/run to run the bot.")
    else:
        print("Invalid arguments. Use --piro/-piro/piro for help or -r/--run/run to run the bot.")

if __name__ == "__main__":
    main()
