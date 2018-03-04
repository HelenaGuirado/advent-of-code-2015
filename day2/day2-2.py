f = open("input.txt", "r")
content = f.read()

presents = content.split("\n")

ribbon = 0

for dimension in presents:
	l, w, h = map(int, dimension.split("x"))
	
	if l <= w and l <= h:
		side1 = l
		if w <= h:
			side2 = w
		else:
			side2 = h
	elif w <= l and w <= h:
		side1 = w
		if l <= h:
			side2 = l
		else:
			side2 = h
	else:
		side1 = h
		if l <= w:
			side2 = l
		else:	
			side2 = w
			
	wrap = (side1 + side2) * 2
	bow = l * w * h
	
	ribbon += wrap + bow

print(ribbon)
