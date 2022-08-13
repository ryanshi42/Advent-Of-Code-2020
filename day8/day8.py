from collections import defaultdict

with open('day8.in') as f:
  commands = f.read().split('\n')
  
  end = len(commands)
  j = 0
  while j < end:
    i = 0
    indexes = defaultdict(dict)
    accum = 0
    terminated = True
    print(j)
    command = commands[j]
    if command[:3] == "nop":
      mod = commands[j].replace('nop', 'jmp')
    elif command[:3] == "jmp":
      mod = commands[j].replace('jmp', 'nop')
    else:
      j += 1
      continue
    commands = commands[:j] + [mod] + commands[j+1:]
    while i != end:
      indexes[i] = True
      command = commands[i]
      i += 1
      if command[:3] == "nop":
        continue
      elif command[:3] == "acc":
        if command[4] == '-':
          accum -= int(command[5:])
        else:
          accum += int(command[5:])
      elif command[:3] == "jmp":
        if command[4] == '-':
          i -= int(command[5:])
          i -= 1
        else:
          i += int(command[5:])
          i -= 1
        if indexes.get(i, False) == True:
          print('part 1 answer is =', accum)
          terminated = False
          break
    
    if terminated:
      print('part 2 answer is =', accum)
      exit(0)

    command = commands[j]
    if command[:3] == "nop":
      mod = commands[j].replace('nop', 'jmp')
    elif command[:3] == "jmp":
      mod = commands[j].replace('jmp', 'nop')
    else:
      j += 1
      continue
    commands = commands[:j] + [mod] + commands[j+1:]

    j += 1
