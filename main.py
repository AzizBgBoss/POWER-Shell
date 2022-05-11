#if you'll modifying the shell, please consider crediting to the creator which is me AzizBgBoss.
#https://github.com/AzizBgBoss/POWER-Shell

print("POWER shell by AzizBgBoss || Version: 0.1b\n")
history = []

while True:
  
  line=input('>> ')
  
  if line=='':
    print("No command entered. Type 'kill' to quit.")
    continue
  try:
    command=line.split()[0]
  except:
    print("No command entered. Type 'kill' to quit.")
    continue
  
  if command=='kill':
    print("Shell stopped.")
    break
  
  elif command=='help':
    print("\nPOWER shell created by AzizBgBoss v0.1b.\n\nkill: Quits the shell.\nhelp: POWER shell manual. (This menu)\nprint: Prints a string.\nvar *variable* = *value*: defines a variable.\nvar *variable*: prints the value of a variable.\nhistory: shows you the commands history.\n\nRemember, spaces matter!\n")
  
  elif command=="print":
    print(line.replace("print",'',1).replace(" ",'',1))

  elif command=="var":
    elements=line.split()
    if len(elements)==1:
      print("No variables called or declared. Spaces matter!")
      continue
    elif len(elements)==2:
      try:
        print(globals()[elements[1]])
      except:
        print("Error: Variable "+elements[1]+" is not defined")
    elif len(elements)>=4 and elements[2]=='=':
      globals()[elements[1]]=line.replace("var "+elements[1]+" = ",'')
    else:
      print("Error: Wrong syntax. Type 'help'. Spaces matter!")

  elif command=="history":
    print("\n".join(history))
  
  else:
    print("Error: Command not recognized. Type 'help' for help.")

  history.append(line)
