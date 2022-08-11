with open('day2.in') as f:
    argList = f.readlines()
    returnSum = 0
    for arg in argList:
      manipList = arg.split(' ')
      lo = int(manipList[0].split('-')[0])
      hi = int(manipList[0].split('-')[1])
      aim = manipList[1][0]

      password = manipList[2]

      if (password.count(aim) >= lo and password.count(aim) <= hi):
        returnSum += 1

      
    print(returnSum)

with open('day2.in') as f:
    argList = f.readlines()
    returnSum = 0
    for arg in argList:
      manipList = arg.split(' ')
      lo = int(manipList[0].split('-')[0])
      hi = int(manipList[0].split('-')[1])
      aim = manipList[1][0]

      password = manipList[2]

      if ((password[lo - 1] == aim and password[hi - 1] != aim) or (password[lo - 1] != aim and password[hi - 1] == aim)):
        returnSum += 1

      
    print(returnSum)