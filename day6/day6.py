import sys

with open('day6.in') as f:
  print(sum([len(set(arg.replace('\n',''))) for arg in f.read().split('\n\n')]))

with open('day6.in') as f:
  print(sum([arg.count(char) == arg.count('\n') + 1 for arg in f.read().split('\n\n') for char in set(arg)]))