from os import system, name
from datetime import datetime
from ktools import Edge

edge = Edge()

def clear():
    _ = system('cls') if name == 'nt' else system('clear')

def setedge(_):
    global edge

    tm = edge.totalModuleCount = int(input("Enter # of modules [including needies] > "))
    rm = edge.needyModuleCount = int(input("Enter # of needy modules > "))
    edge.regularModuleCount = tm - rm

    s = edge.serial = input("Enter serial [] > ")
    sl = edge.serialLetters = "".join([c for c in s if c.isalpha()])
    edge.serialLetterCount = len(sl)
    edge.serialVowel = any(char in ["A", "E", "I", "O", "U"] for char in sl)
    edge.serialDigits = "".join([c for c in s if c.isdigit()])
    edge.serialDigitSum = sum([int(c) for c in s if c.isdigit()])
    edge.serialDigitCount = 6 - len(sl)

    a = edge.aBatteries = int(input("Enter # of A batteries > "))
    d = edge.dBatteries = int(input("Enter # of D batteries > "))
    edge.totalBatteries = a+d
    edge.batteryHolders = a/2 + d

    i = edge.indicators = input("Enter indicators [ex: 'lSND uBOB lCAR']> ").split(" ")
    if i == ['']: i = edge.indicators = []
    edge.indicatorLabels = [x[1:] for x in i]
    ic = edge.indicatorCount = len(i)
    lc = edge.litIndicatorCount = len([x for x in i if x[0]=='l'])
    edge.unlitIndicatorCount = ic - lc

    p = edge.portsRaw = [element[1:-1].split("/") if element != "[]" else [] for element in input("Enter ports [ex: '[dvid/rca/ps2] [rca] []]'> ").split(" ")] #thanks chatgpt
    if p == [['']]: p = edge.portsRaw = []
    edge.portsPresent = list({x for sublist in p for x in sublist})
    edge.portCount = len([x for sublist in p for x in sublist])
    edge.portFrequency = {x: sublist.count(x) for sublist in p for x in sublist}
    edge.portPlates = len(p)

    edge.timestamp = datetime.now()

from vanilla import button, wires, keypad, simon, memory, whosOnFirst, maze, morse, wireSeq, password, compWires
from cooking import cooking
from resistors import resistors
from decimation import decimation
from charactershift import characterShift
from colorflash import colorFlash
from followtheleader import followTheLeader
from ledencryption import ledEncryption

from WIP.rainbowarrows import rainbowArrows
from WIP.presidentialelections import presidentialElections
from WIP.count69420 import count69420
from WIP.synapsecipher import synapseCipher
from WIP.wavetapping import wavetapping
from WIP.gameofants import gameOfAnts

modules = {"EDGE": setedge, "B": button, "W": wires, "Kp": keypad, "S": simon, "Mem": memory, "Wof": whosOnFirst, "Mz": maze, "Mc": morse, "Wseq": wireSeq, 
           "P": password, "Cw": compWires, "Cg": cooking, "Re": resistors, "Dec": decimation, "Cs": characterShift, "Cf": colorFlash, "Ftl": followTheLeader,
           "Lede": ledEncryption, "Uarr": rainbowArrows, 'Pe': presidentialElections, "Ct69": count69420, 'Scip': synapseCipher, 'Wv': wavetapping, 'ant': gameOfAnts}

while True:
    clear()
    mod = input('Enter module repository symbol, EDGE = edgework > ')
    modules.get(mod, lambda _ : print("Module not implemented"))(edge)
    input("Press enter to continue.")