f = open("input.txt", "r")
content = f.read()

floor = 0
position  = 0

for loop in range(len(content)):
  if content[loop] == '(':
    floor += 1
  else:
    floor -= 1
  position  += 1
  if floor < 0:
    print(position )
    break
