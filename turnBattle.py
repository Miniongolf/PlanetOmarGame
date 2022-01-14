from random import randint, random, uniform
from colorama import Fore, Style
import moveStats

upl = "\033[A"
green, red, yellow, lgreen, lred, lyellow, lmagenta, cr = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET
bold, fr = Style.BRIGHT, Style.RESET_ALL
moves = [None, "Counting down", "stab", "slash", "overkill", "block", "heal"]

def showPlayerStats(p):
    print("Your Stats:")
    print("Strength: %s | Willpower: %s | HP: %s\n" % (p["strength"], p["willpower"], p["hp"]))

# Make the enemy template
e = {
    "name": None,
    "hp": 0,
    "accuracy": 0
}

def showEnemyStats(e):
    print("\nEnemy Stats:\rName: %s | HP: %s | Accuracy: %s\n" % (e["name"], e["hp"], "{:.2f}".format(e["accuracy"])))


# The enemy's actions
def cpu(p, e):
    cacc = random()
    if e["melee"] > e["ranged"]:
        atkdmg = e["melee"]
    else:
        atkdmg = e["ranged"]
    if cacc <= e["accuracy"]:
        p["hp"] -= (atkdmg - p["defence"])
        print(f"{red}%s{cr} hit you for {lred}%s{cr} damage! You have {lgreen}%s{cr} health left." % (e["name"], atkdmg, p["hp"]))
    else:
        print(f"{red}%s{cr} missed you for 0 damage! You have {lgreen}%s{cr} health left." % (e["name"], p["hp"]))
    return p

# Randomly pick what enemy the player fights
def pickEnemy(p, e):
    enum = randint(1,2)
    eacc = uniform(0.1, 0.25)
    ehp = randint(40,60)
    if enum == 1:
        e = {"name": "Zombie",
        "melee": randint(5,9), 
        "ranged": 0,
        "hp":ehp+10,
        "accuracy":eacc}
        
    elif enum == 2:
        e = {"name": "Skeleton",
        "melee": 0, 
        "ranged": randint(3,7),
        "hp":ehp,
        "accuracy": 2*eacc}
    print(f"{lred}%s {lmagenta}attacked you!\n{cr}" % e["name"])
    showPlayerStats(p)
    return e


# The actual battle
def fight(count, p, e):
    if e["hp"] <= 0:
        e = {
    "name": None,
    "hp": 0,
    "accuracy": 0
    }
    while p["hp"] > 0:
        # Reset player damage
        pdmg = 0
        pdef = 0
        hit = False
        crit = False
        # If the enemy is dead, generate a new one
        if e["hp"] <= 0:
            if e["name"] != None:
                print(f"\n{lgreen}{bold}You defeated the %s!\n{fr}" % e["name"])
            count -= 1
            if count < 0:
                break
            e = pickEnemy(p,e)
        validInput = False
        # While it's still the player's turn (they haven't entered a valid input)
        while validInput == False:
            acc = random()
            move = input()
            print(upl*2)
            # If the move is a melee move
            if move.isnumeric():
                if int(move) < len(moves):
                    move = moves[int(move)]

            if move in moveStats.attacks:
                # If the move hits
                if acc <= (moveStats.attacks[move][1] + p["strength"][1])/2:
                    pdmg = (moveStats.attacks[move][0] + p["strength"][0])*2
                    hit = True
                    crit = True
                elif acc <= moveStats.attacks[move][1] + p["strength"][1]:
                    pdmg = moveStats.attacks[move][0] + p["strength"][0]
                    hit = True
                validInput = True
            
            elif move in moveStats.misc:
                pdef = p["willpower"] + moveStats.misc[move][0]
                p["hp"] += moveStats.misc[move][1]
                validInput = True
                if move == "heal":
                    print(f"You healed yourself for {lgreen}%s{cr} hp! You {red}%s{cr} have {lyellow}%s{cr} health left." % (moveStats.misc["heal"][1], p["name"], p["hp"]))
                if move == "block":
                    print(f"You steel your mind, reducing the damage next turn by {lgreen}%s{cr} damage!" % (moveStats.misc["block"][0]))
            # If the move is to scout
            elif move == "scout" or move == "/scout":
                showEnemyStats(e)
                validInput = True
                hit = None
            # Otherwise tell the player "Invalid input!"
            else:
                print("Invalid input!")
            e["hp"] -= pdmg
        # Show how much health the enemy still has
        if crit == True:
            print(f"{yellow}CRITICAL HIT!!!{cr}", end=" ")
        if hit == True:
            print(f"You hit the {red}%s{cr} for {lgreen}%s{cr} damage! The {red}%s{cr} has {lyellow}%s{cr} health left." % (e["name"], pdmg, e["name"], e["hp"]))
        elif hit == False:
            print(f"You missed the {red}%s{cr} for {lgreen}0{cr} damage! The {red}%s{cr} has {lyellow}%s{cr} health left." % (e["name"], e["name"], e["hp"]))
        
        if e["hp"] > 0:
            p = cpu(p, e)

    if p["hp"] <= 0:
        print(f"{red}You died…{cr}")