from pirobot.pirobot import run_bot
import sys

def print_help():
    print("pirobot - Telegram Auto Reply, When offline")
    print("Author: HK4CRPRASAD (GitHub: https://github.com/hk4crprasad/pirobot)")
    print("Usage:")
    print("  pirobot --piro/-piro   : Show this help message")
    print("  pirobot -r/-run  : Run the Telegram bot")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['--piro', '-piro']:
            print_help()
        elif arg in ['-r', '--run']:
            run_bot()
        else:
            print("Invalid argument. Use --piro/-piro for help or -r/--run to run the bot.")
    else:
        print("Invalid arguments. Use --piro/-piro for help or -r/--run to run the bot.")
