from ktools import Edge

bandLookup = ["silver", "gold", "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]

def resistors(edge: Edge):
    
    primaryIn, secondaryIn = ("A", "B") if int(edge.serialDigits[0]) % 2 == 0 else ("B", "A")
    primaryOut, secondaryOut = ("C", "D") if int(edge.serialDigits[-1]) % 2 == 0 else ("D", "C")

    targetResistance = int(edge.serialDigits[:2]) * (10 ** min(edge.totalBatteries, 6))

    resistor1 = input("Enter top resistor bands > ").split(" ")
    resistor2 = input("Enter bottom resistor bands > ").split(" ")

    print(resistor1)
    print(resistor2)

    resistor1 = (((bandLookup.index(resistor1[0])-2)*10) + (bandLookup.index(resistor1[1])-2)) * (10 ** (bandLookup.index(resistor1[2]) - 2))
    resistor2 = (((bandLookup.index(resistor2[0])-2)*10) + (bandLookup.index(resistor2[1])-2)) * (10 ** (bandLookup.index(resistor2[2]) - 2))

    primaryToSecondary = "lFRK" in edge.indicators
    secondaryToSecondary = (edge.dBatteries > 0) and not primaryToSecondary

    if targetResistance == 0: 
        print(f"{primaryIn} -> {primaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> {secondaryOut}")
    elif targetResistance == resistor1:
        print(f"{primaryIn} -> Top Resistor -> {primaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> Top Resistor -> {secondaryOut}")
    elif targetResistance == resistor2:
        print(f"{primaryIn} -> Bottom Resistor -> {primaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> Bottom Resistor -> {secondaryOut}")
    elif targetResistance > resistor1 and targetResistance > resistor2:
        print(f"{primaryIn} -> Top Resistor -> Bottom Resistor -> {primaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> Top Resistor -> Bottom Resistor -> {secondaryOut}")
    elif targetResistance < resistor1 and targetResistance < resistor2:
        print(f"{primaryIn} -> Top Resistor -> {primaryOut}")
        print(f"{primaryIn} -> Bottom Resistor -> {primaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> Top Resistor -> {secondaryOut}")
        if primaryToSecondary: print(f"{primaryIn} -> Bottom Resistor -> {secondaryOut}")
    
    if secondaryToSecondary: print(f"{secondaryIn} -> {secondaryOut}")