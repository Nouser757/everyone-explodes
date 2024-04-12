from ktools import Edge

def colorFlash(edge: Edge):
    sequence = input("Enter word sequence (colourWord, RYGBMW) > ").split(" ")
    colors = [x[0] for x in sequence]
    words = [x[1] for x in sequence]

    if colors[-1] == "r":
        if words.count("G") >= 3: print(f"Press Yes on {[i for i, x in enumerate(sequence) if x[0] == 'g' or x[1] == 'G'][2]+1}")
        elif colors.count("b") == 1: print(f"Press No on {words.index('M')+1}")
        else: print(f"Press Yes on {max(loc for loc, val in enumerate(sequence) if val[0] == 'w' or val[1] == 'W')+1}")

    elif colors[-1] == "y":
        if "gB" in sequence: print(f"Press Yes on {colors.index('g')+1}")
        elif "wW" in sequence or "rW" in sequence: print(f"Press Yes on {[i for i, x in enumerate(sequence) if x not in ['wW', 'mM', 'bB', 'gG', 'yY', 'rR']][1]+1}")
        else: print(f"Press No on {len([x for x in sequence if x[0] == 'm' or x[1] == 'M'])+1}")
    
    elif colors[-1] == "g":
        if len([x for i, x in enumerate(sequence) if i!=0 and x[0] != sequence[i-1][0] and x[1] == sequence[i-1][1]]) > 0: print("Press No on 5")
        if words.count("M") >= 3: print(f"Press No on {[i for i, x in enumerate(sequence) if x[0] == 'y' or x[1] == 'Y'][0]+1}")
        else: print(f"Press Yes on {[i for i, x in enumerate(sequence) if x in ['wW', 'mM', 'bB', 'gG', 'yY', 'rR']][0]+1}")
    
    elif colors[-1] == "b":
        if len([i for i, x in enumerate(sequence) if x not in ['wW', 'mM', 'bB', 'gG', 'yY', 'rR']]) >= 3: print(f"Press Yes on {[i for i, x in enumerate(sequence) if x not in ['wW', 'mM', 'bB', 'gG', 'yY', 'rR']][0]+1}")
        elif "yR" in sequence or "wY" in sequence: print(f"Press No on {sequence.index('rW')+1}")
        else: print(f"Press Yes on {max(loc for loc, val in enumerate(sequence) if val[0] == 'g' or val[1] == 'G')+1}")
    
    elif colors[-1] == "m":
        if len([x for i, x in enumerate(sequence) if i!=0 and x[0] == sequence[i-1][0] and x[1] != sequence[i-1][1]]) > 0: print("Press Yes on 3")
        elif words.count("Y") > colors.count("b"): print(f"Press No on {max(loc for loc, val in enumerate(words) if val == 'Y')+1}")
        else: print(f"Press No on {colors.index(words[6].lower())+1}")
    
    elif colors[-1] == "w":
        if colors[2] in [words[3].lower(), words[4].lower()]: print(f"Press No on {[i for i, x in enumerate(sequence) if x[0] == 'b' or x[1] == 'B'][0]+1}")
        elif "rY" in sequence: print(f"Press Yes on {max(i for i, x in enumerate(colors) if x == 'b')+1}")
        else: print("Press No")