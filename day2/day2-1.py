f = open("input.txt", "r")
content = f.read()

presents = content.split("\n")

square = 0

for dimension in presents:
	l, w, h = map(int, dimension.split("x"))
	side1 = l*w
	side2 = w*h
	side3 = l*h
	square += (side1 + side2 + side3) * 2
	
	if side1 <= side2 and side1 <= side3:
		square += + side1 
	elif side2 <= side1 and side2 <= side3:
		square += side2
	else:
		square += side3

print(square)
