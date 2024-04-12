from ktools import Edge
from textwrap import wrap

mazeFound = False

def button(edge: Edge):
    colour = input("Enter button colour > ")
    label = input("Enter button label > ")

    if colour == "blue" and label == "abort": act = "hold"
    elif edge.totalBatteries > 1 and label == "detonate": act = "press"
    elif colour == "white" and "lCAR" in edge.indicators: act = "hold"
    elif edge.totalBatteries > 2 and "lFRK" in edge.indicators: act = "press"
    elif colour == "yellow": act = "hold"
    elif colour == "red" and label == "hold": act = "press"
    else: act = "hold"

    if act == "hold":
        print("Hold the button, strip means release on [Blue: 4 / Yellow: 5 / Else: 1]")
    elif act == "press":
        print("Press the button.")

def wires(edge: Edge):
    wires = input("Enter wires [ex: 'blue red black'] > ").split(" ")

    if len(wires) == 3:
        if wires == ["blue", "blue", "red"] or "red" not in wires: print("Cut 2nd")
        else: print("Cut 3rd")

    elif len(wires) == 4:
        if wires.count("red") > 1 and int(edge.serialDigits[-1])%2==1: print("Cut last red")
        elif wires[-1] == "yellow" and "red" not in wires: print("Cut 1st")
        elif wires.count("blue") == 1: print("Cut 1st")
        elif wires.count("yellow") > 1: print("Cut 4th")
        else: print("Cut 2nd")

    elif len(wires) == 5:
        if wires[-1] == "black" and int(edge.serialDigits[-1])%2==1: print("Cut 4th")
        elif wires.count("red") == 1 and wires.count("yellow") > 1: print("Cut 1st")
        elif "black" not in wires: print("Cut 2nd")
        else: print("Cut 1st")

    elif len(wires) == 6:
        if "yellow" not in wires and int(edge.serialDigits[-1])%2==1: print("Cut 3rd")
        elif wires.count("yellow") == 1 and wires.count("white") > 1: print("Cut 4th")
        elif "red" not in wires: print("Cut 6th")
        else: print("Cut 4th")

def keypad(edge: Edge):
    columns = [["Ϙ", "Ѧ", "ƛ", "ϟ", "Ѭ", "ⳤ", "Ͽ"], ["Ӭ", "Ϙ", "Ͽ", 'Ҩ', "☆", "ⳤ", "¿"], ["©", "Ѽ", "Ҩ", "Җ", "Ԇ", "ƛ", "☆"], ["б", "¶", "Ѣ", "Ѭ", "Җ", "¿", "ټ"], ["Ψ", "ټ", "Ѣ", "Ͼ", "¶", "Ѯ", "★"], ["б", "Ӭ", "҂", "æ", "Ψ", "Ҋ", "Ω"]]
    symbols = input("Enter symbols [ex: 'Ѭ ⳤ Ϙ Җ']> ").split(" ")
    for x in columns:
        if all (item in x for item in symbols): break
    
    print(" ".join([y for y in x if y in symbols]))

def simon(edge: Edge):
    if edge.serialVowel:
        l = ['swap b-r y-g', 'swap b-g r-y', 'rotate ccw']
    else:
        l = ['rotate all but green cw', 'swap g-y', 'swap b-g r-y']
    print(l[min(int(input("Enter strike count > ")), 2)])

def memory(edge: Edge):
    mem = []

    display = input("Enter display # > ")
    if display == "1" or display == "2":
        print("pos 2")
        work = "2"
    elif display == "3":
        print("pos 3")
        work = "3"
    elif display == "4":
        print("pos 4")
        work = "4"
    mem.append(work + input("Enter label > "))

    display = input("Enter display # > ")
    if display == "1":
        print("label 4")
        work = "4"
        mem.append(input("Enter pos > ") + work)
    elif display == "2" or display == "4":
        print(f"pos {mem[0][0]}")
        work = mem[0][0]
        mem.append(work + input("Enter label > "))
    elif display == "3":
        print("pos 1")
        work = "1"
        mem.append(work + input("Enter label > "))
    
    display = input("Enter display # > ")
    if display == "1":
        print(f"label {mem[1][1]}")
        work = mem[1][1]
        mem.append(input("Enter pos > ") + work)
    elif display == "2":
        print(f"label {mem[0][1]}")
        work = mem[0][1]
        mem.append(input("Enter pos > ") + work)
    elif display == "3":
        print("pos 3")
        work = "3"
        mem.append(work + input("Enter label > "))
    elif display == "4":
        print("label 4")
        work = "4"
        mem.append(input("Enter pos > ") + work)

    display = input("Enter display # > ")
    if display == "1":
        print(f"pos {mem[0][0]}")
        work = mem[0][0]
        mem.append(work + input("Enter label > "))
    elif display == "2":
        print("pos 1")
        work = "1"
        mem.append(work + input("Enter label > "))
    elif display == "3" or display == "4":
        print(f"pos {mem[1][0]}")
        work = mem[1][0]
        mem.append(work + input("Enter label > "))
    
    display = input("Enter display # > ")
    if display == "1":   print(f"label {mem[0][1]}")
    elif display == "2": print(f"label {mem[1][1]}")
    elif display == "3": print(f"label {mem[3][1]}")
    elif display == "4": print(f"label {mem[2][1]}")

def whosOnFirst(edge: Edge):
    read = dict.fromkeys(['ur'], 0)
    read.update(dict.fromkeys(['first', 'okay', 'c'], 1))
    read.update(dict.fromkeys(['yes', 'nothing', 'led', 'theyare'], 2))
    read.update(dict.fromkeys(
        ['blank', 'read', 'red', 'you', 'your', "you're", 'their'], 3))
    read.update(dict.fromkeys(['lblank', 'reed', 'leed', 'theyre'], 4))
    read.update(dict.fromkeys(
        ['display', 'says', 'no', 'lead', 'holdon', 'youare', 'there', 'see', 'cee'], 5))

    l = {
        'blank': 'wait right okay middle blank',
        'done': "sure uhhuh next what? your ur you're hold",
        'first': 'left okay yes middle no right nothing uhhh wait',
        'hold': "youare u done uhuh you ur sure what? you're",
        'left': 'right left',
        'like': "you're next u ur hold done uhuh what? uhhuh",
        'middle': 'blank ready okay what nothing press no wait left',
        'next': 'what? uhhuh uhuh your hold sure next',
        'no': 'blank uhhh wait first what ready right yes nothing',
        'nothing': 'uhhh right okay middle yes blank no press left',
        'okay': 'middle no first yes uhhh nothing wait okay',
        'press': 'right middle yes ready press',
        'ready': 'yes okay what middle left press right blank ready',
        'right': 'yes nothing ready press no wait what right',
        'sure': "youare done like you're you hold uhhuh ur sure",
        'u': "uhhuh sure next what? you're ur uhuh done u",
        'uhhh': 'ready nothing left what okay yes right no press',
        'uhhuh': 'uhhuh',
        'uhuh': "ur u you are you're next uh uh",
        'ur': 'done u ur',
        'wait': 'uhhh no blank okay yes left first press what',
        'what': 'uhhh what',
        'what?': "you hold you're your u done uh uh like youare",
        'yes': 'okay right uhhh middle first what press ready nothing',
        'you': "sure youare your you're next uhhuh ur hold what?",
        "you're": "you you're",
        'youare': 'your next like uhhuh what? done uhuh hold you',
        'your': 'uhuh youare uhhuh your'
    }

    for _ in range(3):
        buttons = input("Enter buttons > ").split(" ")
        i = buttons[read[input('Enter display word > ')]]
        for x in l[i].split():
            if x in buttons:
                print(x)
                break

def maze(edge: Edge):
    global mazeFound
    
    mazes = [
        [
            ['RD', 'RL', 'DL', 'RD', 'RL', 'L'],
            ['UD', 'RD', 'UL', 'UR', 'RL', 'DL'],
            ['UD', 'UR', 'DL', 'RD', 'RL', 'UDL'],
            ['UD', 'R', 'URL', 'UL', 'R', 'UDL'],
            ['URD', 'RL', 'DL', 'RD', 'L', 'UD'],
            ['UR', 'L', 'UR', 'UL', 'R', 'UL']
        ],
        [
            ['R', 'RDL', 'L', 'RD', 'RDL', 'L'],
            ['RD', 'UL', 'RD', 'UL', 'UR', 'DL'],
            ['UD', 'RD', 'UL', 'RD', 'RL', 'UDL'],
            ['URD', 'UL', 'RD', 'UL', 'D', 'UD'],
            ['UD', 'D', 'UD', 'RD', 'UL', 'UD'],
            ['U', 'UR', 'UL', 'UR', 'RL', 'UL']
        ],
        [
            ['RD', 'RL', 'DL', 'D', 'RD', 'LD'],
            ['U', 'D', 'UD', 'UR', 'UL', 'UD'],
            ['RD', 'UDL', 'UD', 'RD', 'DL', 'UD'],
            ['UD', 'UD', 'UD', 'UD', 'UD', 'UD'],
            ['UD', 'UR', 'UL', 'UD', 'UD', 'UD'],
            ['UR', 'RL', 'RL', 'UL', 'UR', "UL"]
        ],
        [
            ['RD', 'DL', 'R', 'RL', 'RL', 'DL'],
            ['UD', 'UD', 'RD', 'RL', 'RL', 'UDL'],
            ['UD', 'UR', 'UL', 'RD', 'L', 'UD'],
            ['UD', 'R', 'RL', 'URL', 'RL', 'UDL'],
            ['URD', 'RL', 'RL', 'RL', 'DL', 'UD'],
            ['UR', 'RL', 'L', 'R', 'UL', 'U']
        ],
        [
            ['R', 'RL', 'RL', 'RL', 'RDL', 'DL'],
            ['RD', 'RL', 'RL', 'RDL', 'UL', 'U'],
            ['URD', 'DL', 'R', 'UL', 'RD', 'DL'],
            ['UD', 'UR', 'RL', 'DL', 'U', 'UD'],
            ['UD', 'RD', 'RL', 'URL', 'L', 'UD'],
            ['U', 'UR', 'RL', 'RL', 'RL', 'UL']
        ],
        [
            ['D', 'RD', 'DL', 'R', 'RDL', 'DL'],
            ['UD', 'UD', 'UD', 'RD', 'UL', 'UD'],
            ['URD', 'UL', 'U', 'UD', 'RD', 'UL'],
            ['UR', 'DL', 'RD', 'UDL', 'UD', 'D'],
            ['RD', 'UL', 'U', 'UD', 'UR', 'UDL'],
            ['UR', 'RL', 'RL', 'UL', 'R', 'UL']
        ],
        [
            ['RD', 'RL', 'RL', 'DL', 'RD', 'DL'],
            ['UD', 'RD', 'L', 'UR', 'UL', 'UD'],
            ['UR', 'UL', 'RD', 'L', 'RD', 'UL'],
            ['RD', 'DL', 'URD', 'RL', 'UL', 'D'],
            ['UD', 'U', 'UR', 'RL', 'DL', 'UD'],
            ['UR', 'RL', 'RL', 'RL', 'URL', 'UL']
        ],
        [
            ['D', 'RD', 'RL', 'DL', 'RD', 'DL'],
            ['URD', 'URL', 'L', 'UR', 'UL', 'UD'],
            ['UD', 'RD', 'RL', 'RL', 'DL', 'UD'],
            ['UD', 'UR', 'DL', 'R', 'URL', 'UL'],
            ['UD', 'D', 'UR', 'RL', 'RL', 'RL'],
            ['UR', 'URL', 'RL', 'RL', 'RL', 'L']
        ],
        [
            ['D', 'RD', 'RL', 'RL', 'RDL', 'DL'],
            ['UD', 'UD', 'RD', 'L', 'UD', 'UD'],
            ['URD', 'URL', 'UL', 'RD', 'UL', 'UD'],
            ['UD', 'D', 'RD', 'UL', 'R', 'UDL'],
            ['UD', 'UD', 'UD', 'RD', 'DL', 'U'],
            ['UR', 'UL', 'UR', 'UL', 'UR', 'L']
        ]
    ]

    indices = {"12": 0, "63": 0, "52": 1, "24": 1, "44": 2, "64": 2,
               "11": 3, "14": 3, "53": 4, "46": 4, "51": 5, "35": 5,
               "21": 6, "26": 6, "41": 7, "34": 7, "32": 8, "15": 8}

    curmaze = mazes[indices[input("Enter coordinates of a circle [ex: '24' = 2nd column, 4th row] > ")]]
    start = [int(x)-1 for x in input("Enter coordinates of white square > ")[::-1]]
    goal = [int(x)-1 for x in input("Enter coordinates of red triangle > ")[::-1]]

    mazeFound = False

    def mazerun(pos, end, path, visited):
        if pos in visited: return
        global mazeFound
        if pos == end:
            mazeFound = True
            print('-'.join(wrap(''.join(path), 4)))
        else:
            if mazeFound: return
            visited.append(pos)
            for dir in curmaze[pos[0]][pos[1]]:
                if   dir == 'U': mazerun([pos[0]-1, pos[1]], end, path + ['U'], visited)
                elif dir == 'R': mazerun([pos[0], pos[1]+1], end, path + ['R'], visited)
                elif dir == 'D': mazerun([pos[0]+1, pos[1]], end, path + ['D'], visited)
                elif dir == 'L': mazerun([pos[0], pos[1]-1], end, path + ['L'], visited)
    
    mazerun(start, goal, [], [])    

def morse(edge: Edge):
    fl = input("Enter first letter in morse > ")

    if fl == "..-.": print("3.555 MHz")
    elif fl == "....": print("3.515 MHz")
    elif fl == ".-..": print("3.542 MHz")
    elif fl == "-": print("3.532 MHz")
    elif fl == "...-": print("3.595 MHz")
    elif fl == "-...":
        sl = input("Enter second letter in morse > ")

        if sl == ".": print("3.600 MHz")
        elif sl == "..": print("3.552 MHz")
        elif sl == "---":
            tl = input("Enter third letter in morse > ")

            if tl == "--": print("3.565 MHz")
            elif tl == "-..-": print("3.535 MHz")
        elif sl == ".-.":
            tl = input("Enter third letter in morse > ")

            if tl == ".": print("3.572 MHz")
            elif tl == "..": print("3.575 MHz")
    elif fl == "...":
        sl = input("Enter second letter in morse > ")

        if sl == "....": print("3.505 MHz")
        elif sl == ".-..": print("3.522 MHz")
        elif sl == "-":
            tl = input("Enter third letter in morse > ")

            if tl == ".": print("3.582 MHz")
            elif tl == "..": print("3.592 MHz")
            elif tl == ".-.": print("3.545 MHz")

def wireSeq(edge: Edge):
    redCount = 0
    blueCount = 0
    blackCount = 0

    redList = ["C", "B", "A", "AC", "B", "AC", "ABC", "AB", "B"]
    blueList = ["B", "AC", "B", "A", "B", "BC", "C", "AC", "A"]
    blackList = ["ABC", "AC", "B", "AC", "B", "BC", "AB", "C", "C"]

    for _ in range(4):
        wires = input("Enter wires on current panel > ").split(" ")

        out = []

        for x in wires:
            if x[0] == "r":
                if x[1] in redList[redCount]: out.append("Cut")
                else: out.append("Dont")
                redCount += 1
            elif x[0] == "b":
                if x[1] in blueList[blueCount]: out.append("Cut")
                else: out.append("Dont")
                blueCount += 1
            elif x[0] == "k":
                if x[1] in blackList[blackCount]: out.append("Cut")
                else: out.append("Dont")
                blackCount += 1
        
        print(", ".join(out) + ", Next")

def password(edge: Edge):
    passwords = [x.upper() for x in ["about", "after", "again", "below", "could", "every", "first", "found", "great",
                 "house", "large", "learn", "never", "other", "place", "plant", "point", "right",
                 "small", "sound", "spell", "still", "study", "their", "there", "these", "thing",
                 "think", "three", "water", "where", "which", "world", "would", "write"]]
    l = input("Please enter the first letter possibilities > ")
    for x in passwords[:]:
        if x[0] not in l:
            passwords.pop(passwords.index(x))
    if len(passwords) == 1:
        print(passwords[0])
        return
    l = input("Please enter the second letter possibilities > ")
    for x in passwords[:]:
        if x[1] not in l:
            passwords.pop(passwords.index(x))
    if len(passwords) == 1:
        print(passwords[0])
        return
    l = input("Please enter the third letter possibilities > ")
    for x in passwords[:]:
        if x[2] not in l:
            passwords.pop(passwords.index(x))
    if len(passwords) == 1:
        print(passwords[0])
        return
    l = input("Please enter fourth letter possibilities > ")
    for x in passwords[:]:
        if x[3] not in l:
            passwords.pop(passwords.index(x))
    if len(passwords) == 1:
        print(passwords[0])
        return
    l = input("Please enter the fifth letter possibilities > ")
    for x in passwords[:]:
        if x[4] not in l:
            passwords.pop(passwords.index(x))
    if len(passwords) == 1:
        print(passwords[0])

def compWires(edge: Edge):
    b2 = edge.totalBatteries >= 2
    even = int(edge.serialDigits[-1])%2 == 0
    p = "parallel" in edge.portsPresent
    possibilities = [[True, even, even, even], [False, b2, p, even], [True, True, False, p], [b2, b2, p, False]]

    wires = input("Enter wires > ").split(" ")

    acts = []

    for x in wires:
        top = 0 + (1 if "L" in x else 0) + (2 if "S" in x else 0)
        bottom = 0 + (1 if "r" in x else 0) + (2 if "b" in x else 0)
        acts.append(possibilities[top][bottom])
    
    print(", ".join([("Cut" if x else "Dont") for x in acts]))