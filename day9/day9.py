from collections import Counter

with open('day9.in') as f:
  argList = [int(arg) for arg in f.read().split('\n')]
  p = argList[:25]
  
  def sumOf(ls, target):
    c1 = dict(Counter(ls))
    for key in c1.keys():
      if c1.get(target - key, -1) != -1:
        return True
    return False
  
  k = 25
  while sumOf(p, argList[k]):
    p = p[1:]
    p.append(argList[k])
    k += 1
  print(argList[k])
  print(k)

p1Res = 500
p1Target = 10884537

with open('day9.in') as f:
  # brute force solution
  # a better way is to use prefix sum, but I was too lazy to implement that
  argList = [int(arg) for arg in f.read().split('\n')]
  i = 0
  j = p1Res
  k = p1Res

  exit(0)
  while i <= p1Res:
    while i < j:
      if sum(argList[i:j]) == p1Target:
        print(min(argList[i:j] + max(argList[i:j])))
        exit(0) 
      j -= 1
    j = k
    i += 1
    