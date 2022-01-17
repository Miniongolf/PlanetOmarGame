import os
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
    os.system("clear")
    pwait(f"Hello, {user}! Welcome to the {green}Planet Omar Adventure Game{fr}!", 1, True)
    pwait("Here, you will play the role of Omar's grouchy neighbour.", 1, True)
    pwait("Enjoy!", 2)
    os.system("clear")

def houseTutorial():
    os.system("clear")
    pwait("You wake up to the beeping of a truck backing up.", 0.75, True)
    pwait("Still half asleep, you sigh, rubbing your eyes.", 0.75, True)
    pwait("You decide to go outside to check out what's happening.", 1, True)
    os.system('clear')
    pwait("Use arrow keys or wasd to move around the house! Go outside and hit the checkmark.", 0.2, True)
    pwait("Your character is the \"@\" symbol in the bedroom.", 0, True)

def fightTutorial():
    os.system("clear")
    pwait(f"You see your neighbours moving in. {bold}They're Muslim.{fr} You know to treat everyone with respect. \nYou know it's wrong to discriminate based on religion. But you can't help it. \nYou try as hard as you can to fight back the negativity.")
    pwait("\nYou can defend yourself using these 3 actions.")
    pwait("(1) Counting to 5 (3 damage, 95% accuracy) \n(2) Deep breaths (7 damage, 70% accuracy) \n(3) Happy thoughts (12 damage, 50% accuracy)\n")
    pwait("Some actions do more damage than others, but are less accurate.", split=True)
    pwait("Type in 1, 2, or 3 to select your move, then press enter to confirm. Keep attacking until the enemy is defeated.\n\n")

def mazeTutorial():
    pwait("You are the \"@\" in the top-left of the maze. Use arrow keys or wasd to move through the maze\nto the \"I\"s to get information about Muslim culture. Then go to the \"Q\" to start the quiz.", 1, True)

def quizTutorial():
    os.system("clear")
    time.sleep(0.5)
    os.system("clear")
    pwait("You will be presented with a multiple choice quiz with 3 options.", 0.5, True)
    pwait("Type in a, b, or c to select your answer and press enter to confirm.", 1, True)
    os.system("clear")

def ending():
    pwait("You now understand the Muslim culture. You see why they wear different clothing like hijabs and why they don't eat non-Halal foods like pork.", split=True)
    pwait("")