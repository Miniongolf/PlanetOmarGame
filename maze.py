from getkey import getkey, keys
from colorama import Fore, Style

green, red, yellow, lgreen, lred, lyellow, lmagenta, cr = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET
bold, fr = Style.BRIGHT, Style.RESET_ALL

upl = "\033[A"

housestr = '''
         ______________________________        
        |            |                 |       
        |            |                 |       
        |            '     Bedroom     |       
        |  Bathroom  |                 |       
        |            |                 |       
        |            |____. .__________|_______
Outside |____________|          |             |
        |   |                   |             |
        |   |                   '   Kitchen   |
√       ' E '      Hallway      |             |
        |   |                   |             |
        |___|___________________|_____________|
'''

locationstr = '''
S.......|..
........|.I
.______....
.....I|....
|...__|.|..
|.......|..
|_____|.|..
........|..
..._____|..
....I...|..
..........Q'''

foodstr = '''
S..........
.I......|.I
.______....
........|..
........|..
........|..
...........
........|..
........|..
....I...|__
..........Q'''

clothingstr = '''
S..........
.I......|.I
.______....
........|..
........|..
........|..
........|..
........|..
........|..
....I...|..
..........Q'''

housel = housestr.splitlines()
locationl = locationstr.splitlines()
foodl = foodstr.splitlines()
clothingl = clothingstr.splitlines()

def strToList(mlstring):
    array = mlstring.splitlines()
    for i in range(len(array)):
        array[i] = list(array[i])
    return array

house = strToList(housestr)
location = strToList(locationstr)
food = strToList(foodstr)
clothing = strToList(clothingstr)

def ShowMap(map, sep):
    print(upl*(len(map)+2))
    # os.system("clear") is slower, creating delay between the player's movements.
    for i in range(len(map)):
        if sep == True:
            print(*map[i])
        else:
            print(*map[i], sep="")





def updateMap(map, x, y, symb, sep):
    map[y][x] = symb
    ShowMap(map, sep)



def maze(map, template, pX, pY, sep = True, text = None):
    oldX, oldY = pX+0, pY+0
    maxX, maxY, minX, minY = len(template[1])-1, len(map), 0, 1
    # empty = " .#"
    solid = "_|"
    updateMap(map, pX,pY,'@', sep)

    while template[pY][pX] not in "Q√":
        PosUpdate = False
        tempoldX = pX
        tempoldY = pY
        # Get the player input
        key = getkey()
        if (key == "w" or key == keys.UP) and pY > minY:
            if map[pY-1][pX] not in solid:
                pY -= 1
                PosUpdate = True
        if (key == "a" or key == keys.LEFT) and pX > minX:
            if map[pY][pX-1] not in solid:
                pX -= 1
                PosUpdate = True
        if (key == "s" or key == keys.DOWN) and pY < maxY - 1:
            if map[pY+1][pX] not in solid:
                pY += 1
                PosUpdate = True
        if (key == "d" or key == keys.RIGHT) and pX < maxX:
            if map[pY][pX+1] not in solid:
                pX += 1
                PosUpdate = True
        
        if PosUpdate == True:
            oldX, oldY = tempoldX + 0, tempoldY + 0
            updateMap(map, pX,pY,'@', sep)
            if template[pY][pX] == "I":
                if text != []:
                    info = text[0]
                    text.remove(info)
                else:
                    print("You have all the information you need. Go to the Q to take the Quiz!")
                print(lgreen, info, fr)

            if template[oldY][oldX] == "I":
                updateMap(map, oldX, oldY, ".", sep)
                trow = list(template[oldY])
                trow[oldX] = "O"
                trow = "".join(trow)
                template[oldY] = trow
            else:
                updateMap(map, oldX, oldY, template[oldY][oldX], sep)