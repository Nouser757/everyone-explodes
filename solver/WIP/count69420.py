#doesnt work, too lazy to fix

from ktools import Edge

def rdzanu(n): return ((str(n).count('4')+str(n).count('7')) % 2 == 1)
def arceus(n): return any(str(n)[i:i+2] in str(n)[i+2:] for i in range(len(str(n))-1)) #thanks chatgpt
def meh(n): return any(n == x ** y for x in range(2, int(n ** 0.5) + 1) for y in range(2, int(n ** 0.5) + 1)) #thanks chatgpt
def depresso(n): return all([str(n).count(i) != 2 for i in range(10)])
def bomber(n): return (len(set(str(n))) <= 2)
def asmir(n):
  parity = (int(str(n)[0]) >= 5)
  for x in str(n)[1:]:
    if (int(x) >= 5) == parity: return False
    else: parity = not parity
  return True
def eltrick(n):
  s = 0
  for x in str(n):
    if x in ["0", "6", "9"]: s +=1
    elif x == "8": s += 2
  return (s % 2 == 0)
def gwen(n):
  n = [int(x) for x in str(n)]
  for i in range(len(list)):
    m = n.copy()
    m.remove(i)
    if sorted(m) == m: return True
  return False
def ghostsalt(n): return hex(n)[-1] in ["8", "9", "a", "b", "c", "d", "e", "f"]
def kabewm(n):
  n = str(n)
  while len(n) != 1: n = str(sum([int(x) for x in n]))
  return (n % 2 == 0)
def cooldoom(n):
  pass


def count69420(edge: Edge):
  ln = int(input("Enter first number > "))
