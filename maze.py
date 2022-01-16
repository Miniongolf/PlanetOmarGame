from getkey import getkey, keys
import random
import quiz
upl = "\033[A"
mapstr = '''
...........
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

mapl = mapstr.splitlines()


def strToList(mlstring):
    array = mlstring.splitlines()
    for i in range(len(array)):
        array[i] = list(array[i])
    return array

area = strToList(mapstr)
def ShowMap(map):
    print(upl*(len(map)+2))
    # os.system("clear") is slower, creating delay between the player's movements.
    for i in range(len(map)):
        print(*map[i])





def updateMap(map, x, y, symb):
    map[y][x] = symb
    ShowMap(map)



def maze(map, template, text):
    pX, pY = 5, 6
    oldX, oldY = 5, 6
    maxX, maxY, minX, minY = 10, len(map), 0, 1
    # empty = " .#"
    solid = "_|"
    updateMap(map, pX,pY,'@')

    while template[pY][pX] != "Q":
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
            updateMap(map, pX,pY,'@')
            if template[pY][pX] == "I":
                if text != []:
                    info = random.choice(text)
                    text.remove(info)
                else:
                    print("You have all the information you need. Go to the Q to take the Quiz!")
                print(info)

            if template[oldY][oldX] == "I":
                updateMap(map, oldX, oldY, "O")
                trow = list(template[oldY])
                trow[oldX] = "O"
                trow = "".join(trow)
                template[oldY] = trow
            else:
                updateMap(map, oldX, oldY, template[oldY][oldX])