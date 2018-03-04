with open("input.txt", "r") as file:
	content = file.read()
	
sHouse = set()
rHouse = set()

xSanta = 0
ySanta = 0
xRobo = 0
yRobo = 0

sHouse.add((xSanta, ySanta))

for direction in range(len(content)):
	if direction % 2 == 0:
		if content[direction] == ">":
			xRobo += 1
		elif content[direction] == "<":
			xRobo -= 1
		elif content[direction] == "^":
			yRobo += 1
		else:
			yRobo -= 1
		rHouse.add((xRobo,yRobo))
	else:
		if content[direction] == ">":
			xSanta += 1
		elif content[direction] == "<":
			xSanta -= 1
		elif content[direction] == "^":
			ySanta += 1
		else:
			ySanta -= 1
		sHouse.add((xSanta,ySanta))
		
total = rHouse.union(sHouse)
print(len(total))