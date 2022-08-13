from collections import defaultdict
from functools import lru_cache

myDict = defaultdict(dict)

with open('day7.in') as f:
  bagList = f.read().split('\n') 
  for bags in bagList:
    parseList = bags.split(' ')
    if ' '.join(parseList[3:]) != "contain no other bags.":
      innerBags = (' '.join(parseList[4:])).split(', ')
      for innerBag in innerBags:
        args = innerBag.split(' ')
        myDict[' '.join(parseList[:2])][' '.join(args[1:3])] = int(args[0])
    else:
      myDict[' '.join(parseList[:2])] = {}
  
  t = 'shiny gold'

  @lru_cache(maxsize=256)
  def colourIn(target, bag):
    if target in myDict[bag]:
      return True
    else: 
      return any([colourIn(target, b) for b in myDict[bag]])
  p1 = sum([colourIn(t, b) for b in myDict])
  print(p1)

  sumDict = defaultdict(dict)

  def bagsIn(bag):
    if myDict[bag] == {}:
      return 1
    else:
      return sum([bagsIn(b) * myDict[bag][b] for b in myDict[bag]]) + 1

  p2 = bagsIn(t) - 1

  # this code runs better
  # def bagsIn(bag):
  #   return sum([(bagsIn(b) + 1) * myDict[bag][b] for b in myDict[bag]])

  # p2 = bagsIn(t)
  print(p2)