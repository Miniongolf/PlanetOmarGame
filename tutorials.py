from os import system
import sys, time

from colorama import Fore, Style
green, red, yellow, lgreen, lred, lyellow, lmagenta, cr = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET
bold, fr = Style.BRIGHT, Style.RESET_ALL

def pwait(string, delay = 0, split = False):
    if bool(split) == True:
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)
        print("")
    else:
        print(string)
    time.sleep(delay)

def introduction(user):
    system("clear")
    pwait(f"Hello, {user}! Welcome to the {green}Planet Omar Adventure Game!{fr}", 1, True)
    pwait("Here, you will play the role of Omar's grouchy neighbour.", 1, True)
    pwait("Enjoy!", 2)
    system("clear")

def houseTutorial():
    system("clear")
    pwait("You wake up to the beeping of a truck backing up.", 0.75, True)
    pwait("Still half asleep, you sigh, rubbing your eyes.", 0.75, True)
    pwait("You decide to go outside to check out what's happening.", 1, True)
    system('clear')
    pwait("Use arrow keys or \"wasd\" to move around the house! Try going to the bathroom first.", 0, True)

def fightTutorial():
    system("clear")
    pwait(f"You see your neighbours moving in. {bold}They're muslim.{fr} You know to treat everyone equally. \nYou know it's wrong to discriminate based on religion. But you can't help it. \nYou try as hard as you can to fight back the negativity assaulting your mind.")
    pwait("You can defend yourself psychologically using these 4 attacks:")
    pwait("(1) Counting down (3 damage, 95% accuracy) \n(2) stab (7 damage, 70% accuracy) \n(3) slash (12 damage, 50% accuracy) \n(4) block (Take 20 damage less on the next turn) \n(5) heal (+20 hp)\n")

def mazeTutorial():
    pwait("Use arrow keys or wasd to move your character", 1, True)
