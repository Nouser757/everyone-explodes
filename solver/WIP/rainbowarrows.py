from ktools import Edge, rangify

northtable = [["SE", "NE", "W", "NW", "N", "S", "S", "SW", "S", "SE"], 
              ["S", "NW", "SE", "NE", "N", "NE", "N", "NW", "NE", "N"],
              ["SE", "SW", "NE", "N", "NW", "NW", "N", "W", "N", "N"],
              ["S", "E", "NW", "NW", "NW", "SW", "N", "NE", "SW", "N"],
              ["E", "NW", "S", "SW", "NW", "E", "W", "W", "E", "W"],
              ["NE", "SE", "N", "W", "SW", "NE", "W", "S", "W", "W"],
              ["NW", "N", "W", "W", "NW", "S", "SW", "W", "SE", "S"],
              ["S", "S", "NE", "SW", "S", "NW", "E", "SE", "NW", "NE"],
              ["S", "W", "SE", "NE", "N", "NE", "N", "NW", "SE", "N"],
              ["SW", "W", "S", "S", "SW", "E", "E", "S", "NE", "SW"]]

degrees = { #thanks chatgpt
    range(6): 0,
    range(6, 17): 1,
    range(17, 29): 2,
    range(29, 40): 3,
    range(40, 51): 4,
    range(51, 62): 5,
    range(62, 74): 6,
    range(74, 85): 7,
    range(85, 96): 0,
    range(96, 100): 1
}

directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
pressed = []

def correctdirection(button):
    global directions
    global pressed

def rainbowArrows(edge: Edge):
    global directions
    global pressed
    whiteArrowPos = input("Enter compass position of white arrow > ")
    display = input("Enter display # > ")
    clockwise = input("Does rainbow pattern go CW or CCW? > ") == "CW"

    i = 0 + directions.index(whiteArrowPos)

    while len(pressed) != 8:
        if directions[i] == "N": pressed.append(correctdirection(northtable[int(display[1]), int(edge.serialDigits[-1])]))
        elif directions[i] == "NE": pressed.append(correctdirection(directions[(directions.index(whiteArrowPos) + degrees[int(display)] + (4 if len(pressed) == 3 else 0))%8]))
        elif directions[i] == "E": 
            binary = int(edge.batteryHolders >= edge.portPlates)*8 + int(display/(edge.totalBatteries+1) == 0)*4 + int("parallel" in edge.portsPresent or "serial" in edge.portsPresent)*2 + int(any(x in directions for x in pressed))
            shifted = (binary >> rangify(edge.indicatorCount, 4, 1, 4)) | (binary << (4 - rangify(edge.indicatorCount, 4, 1, 4))) & 0xF
            pressed.append(correctdirection(directions[shifted%8]))
        elif directions[i] == "SE":
            if len(pressed) == 0: pressed.append("SE")
            else:
                j = directions.index(pressed[-1]) - 1
                while directions[j] in pressed: j -= 1
                pressed.append(correctdirection(directions[j+len(pressed)]))
        