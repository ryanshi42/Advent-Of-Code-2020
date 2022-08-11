def checkString(myString):
  myBool = True
  for char in myString:
    if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
      return False
  return True


def checkEye(myString):
  myList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if myString in myList:
    return True
  else:
    return False

with open('day4.in') as f:
  passports = f.read().split('\n\n')
  valid = 0
  for passport in passports: 
    myDict = {}
    for pLines in passport.split('\n'):
      for pLineEntry in pLines.split(' '):
        field = pLineEntry[:3]
        value = pLineEntry[4:]
        if field == 'byr' and int(value) >= 1920 and int(value) <= 2002:
          myDict[field] = value
        if field == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
          myDict[field] = value
        if field == 'eyr' and int(value) >= 2020 and int(value) <= 2030:
          myDict[field] = value
        if field == 'hcl' and value[0] == '#' and len(value) == 7 and checkString(value[1:]):
          myDict[field] = value
        if field == 'ecl' and checkEye(value):
          myDict[field] = value
        if field == 'pid' and len(value) == 9 and value.isnumeric():
          myDict[field] = value        
        if field == 'cid':
          myDict[field] = value   
        if field == 'hgt' and value[-2:] == 'cm' and int (value[:-2]) >= 150 and int (value[:-2]) <= 193:
          myDict[field] = value   
        if field == 'hgt' and value[-2:] == 'in' and int (value[:-2]) >= 59 and int (value[:-2]) <= 76:
          myDict[field] = value   

    if (len(myDict) == 8 or (len(myDict) == 7 and myDict.get('cid', -1) == -1)):
      valid += 1

  print(valid)