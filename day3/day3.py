with open('day3.in') as f:
  trees = f.readlines()
  x = 0
  y = 0
  returnSum = 0
  while y != len(trees):
    if trees[y][x] == '#':
      returnSum += 1
    
    x = (x + 3) % (len(trees[0]) - 1)
    y += 1
  print(returnSum)

with open('day3.in') as f:
  trees = f.readlines()
  prod = 1

  for (dx, dy) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    x = 0
    y = 0
    returnSum = 0
    while y < len(trees):
      if trees[y][x] == '#':
        returnSum += 1
      
      x = (x + dx) % (len(trees[0]) - 1)
      y += dy
    prod *= returnSum
  print(prod)
