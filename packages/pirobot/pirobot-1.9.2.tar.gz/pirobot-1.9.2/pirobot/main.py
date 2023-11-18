import sys
from pirobot.pirobot import run_bot, print_help

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['-r', '--run']:
            run_bot()
        elif arg in ['--piro', '-piro']:
            print_help()
        else:
            print("Invalid argument. Use --piro/-piro for help or -r/--run to run the bot.")
    else:
        print("Invalid arguments. Use --piro/-piro for help or -r/--run to run the bot.")

if __name__ == "__main__":
    main()
