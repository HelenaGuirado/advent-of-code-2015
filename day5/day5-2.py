with open("input.txt", "r") as file:
	lines = file.read().split("\n")
	
nice_string = 0

for line in lines:
	rule1 = False
	rule2 = False
	array_dl = {}
	
	for idx in range(len(line)):
		double_letter = line[idx:idx+2]
		if double_letter in array_dl:
			if idx - array_dl[double_letter] > 1:
				rule1 = True
		else:
			array_dl[double_letter] = idx
		
	for idx in range(len(line) - 2):
		letter = line[idx]

		if letter == line[idx+2]:
			rule2 = True
	
	if rule1 and rule2:
		nice_string += 1
print(nice_string)