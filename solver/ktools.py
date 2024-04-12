from prodict import Prodict
from typing import List, Dict
from datetime import datetime

class Edge(Prodict):
    totalModuleCount: int
    needyModuleCount: int
    regularModuleCount: int

    serial: str
    serialLetterCount: int
    serialDigitCount: int
    serialLetters: str
    serialVowel: bool
    serialDigits: str
    serialDigitSum: int

    aBatteries: int
    dBatteries: int
    totalBatteries: int
    batteryHolders: int

    indicators: List[str]
    indicatorLabels: List[str]
    indicatorCount: int
    litIndicatorCount: int
    unlitIndicatorCount: int

    portsRaw: List[list[str]]
    portsPresent: List[str]
    portCount: int
    portFrequency = Dict[str, int]
    portPlates: int

    timestamp: datetime


def rangify(N, diff, minValue=1, maxValue=None): #thanks chatgpt
    '''Repeatedly adds/subtracts diff from N until N is within minValue and maxValue, inclusive, if min/max are unspecified they default to 1/diff'''
    if maxValue==None: maxValue=diff
    while N < minValue or N > maxValue:
        if N < minValue:
            N += diff
        else:
            N -= diff
    return N

def a1z26(input):
    if type(input) == str: return ord(input.lower()) - 96
    elif type(input) == int: return chr(rangify(input, 26, 1, 26) + 96).upper()
    
def caesar(str, shift):
    return ''.join([a1z26(rangify(a1z26(x)+shift, 26, 1, 26)) for x in str])