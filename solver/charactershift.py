from ktools import Edge, a1z26
from itertools import product

def characterShift(edge: Edge):
    letters = [a1z26(x) for x in input("Enter letters > ").split(" ")]
    numbers = [int(x) for x in input("Enter numbers > ").split(" ")]


    X = edge.portCount + edge.serialLetterCount
    Y = edge.indicatorCount + edge.serialDigitCount
    difftable = [3, X, -Y, Y-edge.portPlates, int(edge.serialDigits[-1]), (X*2)-edge.batteryHolders, edge.litIndicatorCount+Y-edge.unlitIndicatorCount, (X if "lSIG" in edge.indicators else Y), X+Y-edge.indicatorCount+edge.dBatteries, (X if edge.totalBatteries > 3 else -X)+(Y if edge.indicatorCount else -Y)]

    for l, n in product(letters, numbers):
        if a1z26(l+difftable[n]) in edge.serialLetters: print(f"{a1z26(l)} {n}")