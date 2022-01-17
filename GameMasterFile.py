import os, time, maze, moveStats, quiz, turnBattle, tutorials
from colorama import Fore, Style

global all
# Simplify the colours from Colorama
green, red, yellow, lgreen, lred, lyellow, lmagenta, cr = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET
bold, fr = Style.BRIGHT, Style.RESET_ALL

colours = {"green": green, "red": red, "yellow": yellow, "lgreen": lgreen, "lred": lred, "lyellow": lyellow, "lmagenta": lmagenta, "cr": cr}

upl = "\033[A"

points = 0

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

locationInfo = [" - Muslims live all over the world.", " - Muslims worship one and only one god called Allah.", " - The majority of Muslims live in the Middle East, Asia, and Africa. But Muslims live around the world like in Canada and USA."]

foodInfo = [" - Muslims can only eat Halal food (e.g. lamb, beef, chicken).", " - Muslims cannot eat pork or blood, or animals that harm other animals", " - Muslims eat Halal foods to follow their God's rules (as set in the Qur'an)."]

clothingInfo = [" - Muslim men wear ghutras on their heads.", " - Muslim women wear hijabs (headscarves) to maintain modesty.", " - Muslims dress modestly to respect and be connected to their religion."]


tutorials.introduction(user)
tutorials.houseTutorial()
maze.maze(maze.house, maze.housel[:], 36, 3, sep = False)
tutorials.fightTutorial()
turnBattle.fight(1, p, e)
os.system("clear")
tutorials.mazeTutorial()
maze.maze(maze.location, maze.locationl[:], 0, 1, text=locationInfo)
tutorials.quizTutorial()
points = quiz.quiz(quiz.locationQuiz, points)
os.system("clear")
tutorials.mazeTutorial()
maze.maze(maze.food, maze.foodl[:], 0, 1, text=foodInfo)
os.system("clear")
points = quiz.quiz(quiz.foodQuiz, points)
os.system("clear")
maze.maze(maze.clothing, maze.clothingl[:], 0, 1, text=clothingInfo)
os.system("clear")
points = quiz.quiz(quiz.clothingQuiz, points, last=True)
os.system("clear")
points = tutorials.ending(user, points)
time.sleep(2)
os.system("clear")
print(f"{lgreen}Congratulations{fr}! You finished the game with {points} points! Well done!")


