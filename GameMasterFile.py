import os
import maze, moveStats, quiz, turnBattle, tutorials
from colorama import Fore, Style

global all
# Simplify the colours from Colorama
green, red, yellow, lgreen, lred, lyellow, lmagenta, cr = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET
bold, fr = Style.BRIGHT, Style.RESET_ALL

colours = {"green": green, "red": red, "yellow": yellow, "lgreen": lgreen, "lred": lred, "lyellow": lyellow, "lmagenta": lmagenta, "cr": cr}

upl = "\033[A"

user = input("What do you want me to call you?\n")
print("")
p = {
    "name": user,
    "defence": 0,
    "strength": [0,0],
    "willpower": 0,
    "hp": 50
}
e = {
    "name": None,
    "hp": 0,
    "accuracy": 0
}



clothingInfo = ["Information slide 1", "Information slide 2", "Information slide 3"]


# tutorials.introduction(user)
# tutorials.houseTutorial()
# maze.maze(maze.house, maze.housel[:], 36, 3, sep = False)
# tutorials.fightTutorial()
# turnBattle.fight(1, p, e)
os.system("clear")
tutorials.mazeTutorial()
maze.maze(maze.area, maze.mapl[:], 0, 1, text=clothingInfo)
tutorials.quizTutorial()
quiz.quiz(quiz.clothingQuiz)
