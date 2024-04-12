#not done, didnt finish cause manual had an ambiguity

from ktools import Edge, a1z26
from sympy import isprime
from numpy import base_repr

def shift(l,n):
  return l[n:] + l[:n]

def synapseCipher(edge: Edge):
  encWord = input("Enter encrypted word [page 1, top] > ").upper()

  #step 1: superposition
  key = input("Enter keyword [page 2, top] > ").upper()
  key = "".join(dict.fromkeys(key)) #strip duplicate letters
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  alphabet = ''.join([x for x in alphabet if x not in key])
  #key = list((key+alphabet) if isprime(edge.portCount) else (alphabet+key))
  key = list(alphabet+key) #testcase
  wordA = input("Enter word A [page 2, mid] > ").upper()
  wordB = input("Enter word B [page 2, bot] > ").upper()
  decWord = []
  for i, l in enumerate(wordA):
    dist = shift(key, key.index(l)).index(wordB[i])
    decWord.append(shift(key, key.index(encWord[i]))[dist])
  encWord = ''.join(decWord)
  
  #step 2: logical tenary manipulation
  nums = [list(base_repr(a1z26(x), 3, 2)[-3:]) for x in encWord]
  binA = input("Enter first binary string [page 3, top] > ")
  binB = input("Enter second binary string [page 3, mid] > ")
  key = []
  #if int(edge.serialDigits[0])%2 == int(edge.SerialDigits[-1])%2:
  if True: #testcase
    for i in range(3): key.append(1 if binA[i] != binB[i] else 0)
    for i in range(3): key.append(1 if binA[i+3] == binB[i+3] else 0)
  else:
    for i in range(3): key.append(1 if binA[i] == binB[i] else 0)
    for i in range(3): key.append(1 if binA[i+3] != binB[i+3] else 0)
  print(key)
  for i, b in enumerate(key):
    print(i, b)
    if b == 0: continue
    for j, x in enumerate(nums[i]): nums[i][j] = str((int(x)+1)%3) #increment all digits by 1, wrapping back around
  nums = [''.join(x) for x in nums]
  decWord = [a1z26(int(x, 3)) if x != '000' else a1z26(int('111', 3)) for x in nums]
  encWord = ''.join(decWord)

  #step 3: double square rotation
  
