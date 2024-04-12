#i forgor

from ktools import Edge
from num2words import num2words

def firstPastThePost(voters): pass
def lastPastThePost(voters): pass
def instantRunoff(voters): pass
def coombs(voters): pass
def bordaCount(voters): pass
def approvalVoting(voters): pass
def STV(voters): pass
def condorcet(voters): pass

def findMethod(edge: Edge):
    methodVals = {
        "FPTP": edge.aBatteries,
        "LPTP": edge.dBatteries*2,
        "IR": edge.litIndicatorCount*2,
        "Coomb": edge.unlitIndicatorCount*2,
        "BC": edge.portCount,
        "AV": edge.portPlates*2,
        "STV": int(edge.serialDigits[1]),
        "Condor": int(edge.serialDigits[-2]),
    }

    bracket = [[["FPTP", "LPTP"], ["IR", "Coomb"]], [["BC", "AV"], ["STV", "Condor"]]]
    bracket = [[x[0] if methodVals[x[0]] >= methodVals[x[1]] else x[1] for x in y] for y in bracket]
    bracket = [x[0] if methodVals[x[0]] <= methodVals[x[1]] else x[1] for x in bracket]
    bracket = bracket[0] if num2words(methodVals[bracket[0]]%20) <= num2words(methodVals[bracket[1]]%20) else bracket[1]

    return bracket

def presidentialElections(edge: Edge):
    methodFuncs = {
        "FPTP": firstPastThePost,
        "LPTP": lastPastThePost,
        "IR": instantRunoff,
        "Coomb": coombs,
        "BC": bordaCount,
        "AV": approvalVoting,
        "STV": STV,
        "Condor": condorcet
    }
    method = findMethod(edge)
    