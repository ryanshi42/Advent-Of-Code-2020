import sys


with open('day5.in') as f:
  argList = f.readlines()

  maxSeatId = -99

  d = {}

  def parseRow(fiveStr, lo, hi):
    if lo == hi or fiveStr == '':
      return hi
    elif fiveStr[0] == 'F':
      return parseRow(fiveStr[1:], lo, (lo + hi) // 2)
    else:
      return parseRow(fiveStr[1:], (lo + hi + 1) // 2, hi)

  def parseCol(fiveStr, lo, hi):
    if lo == hi or fiveStr == '':
      return hi
    elif fiveStr[0] == 'L':
      return parseCol(fiveStr[1:], lo, (lo + hi) // 2)
    else:
      return parseCol(fiveStr[1:], (lo + hi + 1) // 2, hi)

  for arg in argList:
    row, col = parseRow(arg[:7], 0, 127), parseCol(arg[7:], 0, 7)
    seatId = row * 8 + col
    d[seatId] = True
    if seatId > maxSeatId:
      maxSeatId = seatId
  for idx in range(maxSeatId):
    if d.get(idx, False) == False and d.get(idx + 1, False) == True and d.get(idx - 1, False) == True:
      print(idx)
  print(maxSeatId)

# if you like functional programming, this looks very intuitive
with open(sys.argv[1], "r") as f:
    seats = (
        f.read()
        .strip()
        .replace("B", "1")
        .replace("F", "0")
        .replace("R", "1")
        .replace("L", "0")
        .split("\n")
    )

print(f"Part 1: {max([int(s, 2) for s in seats])}")
