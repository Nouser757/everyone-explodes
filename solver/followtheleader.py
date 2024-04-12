from ktools import Edge, a1z26

numdict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12
}

def followTheLeader(edge: Edge):
    wires = input("Enter wires (colourFromTo, use hex) > ").split(" ")

    wireGoes = [x[1:] for x in wires]
    wireStarts = [x[1] for x in wires]

    if "rj45" in edge.portsPresent and "45" in wireGoes: current = wireGoes.index("45")
    elif str(edge.totalBatteries) in wireStarts: current = wireStarts.index(str(edge.totalBatteries))
    elif str(edge.serialDigits[0]) in wireStarts: current = wireStarts.index(str(edge.serialDigits[0]))
    elif "lCLR" in edge.indicators:
        print("Cut all wires in descending numerical order")
        return
    else: current = 0
    end = (current - 1) % len(wires)
    
    while current != end:
        if current == (end+1) % len(wires): 
            print(f"Cut {wires[current]}")
            condition = (a1z26(edge.serialLetters[0])-1) % 13
            direction = -1 if wires[current][0] in ["r", "g", "w"] else 1
            prevcut = True
            current = (current + 1) % len(wires)
        else:
            conditionTable = [wires[(current-1)%len(wires)][0] not in ["y", "b", "g"],
                              numdict[wires[(current-1)%len(wires)][2]]%2 == 0,
                              prevcut,
                              wires[(current-1)%len(wires)][0] in ["r", "b", "k"],
                              len(set([wires[(current-1)%len(wires)][0], wires[(current-2)%len(wires)][0], wires[(current-3)%len(wires)][0]])) < 3,
                              (wires[(current-1)%len(wires)][0] == wires[current][0] and wires[(current-2)%len(wires)][0] != wires[current][0]) or (wires[(current-1)%len(wires)][0] != wires[current][0] and wires[(current-2)%len(wires)][0] == wires[current][0]),
                              wires[(current-1)%len(wires)][0] in ["y", "w", "g"],
                              not prevcut,
                              numdict[wires[(current-1)%len(wires)][1]] != numdict[wires[(current-1)%len(wires)][2]]-1,
                              wires[(current-1)%len(wires)][0] not in ["w", "k", "r"],
                              wires[(current-1)%len(wires)][0] != wires[(current-2)%len(wires)][0],
                              numdict[wires[(current-1)%len(wires)][2]] > 6,
                              not (wires[(current-1)%len(wires)][0] in ["w", "k"] and wires[(current-2)%len(wires)][0] in ["w", "k"])]
            
            #print(conditionTable, condition+1, wires[current])
            print(f"{'Cut' if conditionTable[condition] else 'Dont cut'} {wires[current]}")
            prevcut = conditionTable[condition]
            condition = (condition + direction) % 13
            current = (current + 1) % len(wires)
    conditionTable = [wires[(current-1)%len(wires)][0] not in ["y", "b", "g"], numdict[wires[(current-1)%len(wires)][2]]%2 == 0, prevcut, wires[(current-1)%len(wires)][0] in ["r", "b", "k"], len(set([wires[(current-1)%len(wires)][0], wires[(current-2)%len(wires)][0], wires[(current-3)%len(wires)][0]])) < 3, (wires[(current-1)%len(wires)][0] == wires[current][0] and wires[(current-2)%len(wires)][0] != wires[current][0]) or (wires[(current-1)%len(wires)][0] != wires[current][0] and wires[(current-2)%len(wires)][0] == wires[current][0]), wires[(current-1)%len(wires)][0] in ["y", "w", "g"], not prevcut, numdict[wires[(current-1)%len(wires)][1]] != numdict[wires[(current-1)%len(wires)][2]]-1, wires[(current-1)%len(wires)][0] not in ["w", "k", "r"], wires[(current-1)%len(wires)][0] != wires[(current-2)%len(wires)][0], numdict[wires[(current-1)%len(wires)][2]] > 6, not (wires[(current-1)%len(wires)][0] in ["w", "k"] and wires[(current-2)%len(wires)][0] in ["w", "k"])]
    #print(conditionTable, condition+1, wires[current])
    print(f"{'Cut' if conditionTable[condition] else 'Dont cut'} {wires[current]}")