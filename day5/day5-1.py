VOWELS = ["a","e","i","o","u"]
NOT_NICE = ["ab", "cd", "pq", "xy"]

with open("input.txt", "r") as file:
	lines = file.read().split("\n")
		
nice_string = 0

for line in lines:
	number_vowels = 0
	rule1 = False
	rule2 = False
	rule3 = True
	
	for letter in line:
		if letter in VOWELS:
			number_vowels += 1
	if number_vowels >= 3:
		rule1 = True
		
	for idx in range(len(line) - 1):
		letter = line[idx]
		if letter == line[idx+1]:
			rule2 = True

		double_letter = line[idx:idx+2]
		
		if double_letter in NOT_NICE:
			rule3 = False
	if rule1 and rule2 and rule3:
		nice_string += 1
print(nice_string)