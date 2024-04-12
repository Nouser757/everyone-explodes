from ktools import Edge, a1z26

def ledEncryption(edge: Edge):
    colours = input("Enter LED colours > ").split(" ")

    multipliers = ["red", "green", "blue", "yellow", "purple", "orange"]
    for c in colours:
        letters = [a1z26(x)-1 for x in input("Enter letters (clockwise from TL) > ").split(" ")]
        for i, x in enumerate(letters):
            if (x * (multipliers.index(c)+2)) % 26 == letters[(i+2)%4]:
                print(a1z26(x+1)) 
                break