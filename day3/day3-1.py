with open("input.txt", "r") as file:
	content = file.read()

house = set()
x = 0
y = 0
house.add((x,y))

for direction in content:
	if direction == ">":
		x += 1
	elif direction == "<":
		x -= 1
	elif direction == "^":
		y += 1
	else:
		y -= 1
	house.add((x,y))
	
print(len(house))
