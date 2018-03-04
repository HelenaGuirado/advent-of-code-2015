import re
import itertools

CASE = 1000

with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

gridX, gridY = CASE, CASE;
lights = [[0 for x in range(gridX)] for y in range(gridY)]
lights_lit = 0
pattern = re.compile('(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)')

for line in lines:
	matches = pattern.findall(line)
	match = list(itertools.chain.from_iterable(matches))
	line1 = int(match[1])
	line2 = int(match[3])
	col1 = int(match[2])
	col2 = int(match[4])
	
	if match[0] == 'turn on':
		while line1 <= line2:
			while col1 <= col2:
				lights[line1][col1] = 1
				col1 += 1	
			col1 = int(match[2])
			line1 += 1
			
	if match[0] == 'turn off':
		while line1 <= line2:
			while col1 <= col2:
				lights[line1][col1] = 0
				col1 += 1	
			col1 = int(match[2])
			line1 += 1
			
	if match[0] == 'toggle':
		while line1 <= line2:
			while col1 <= col2:
				if(lights[line1][col1] == 0):
					lights[line1][col1] = 1
				else:
					lights[line1][col1] = 0
				col1 += 1	
			col1 = int(match[2])
			line1 += 1

for lightX in range(CASE):
	for lightY in range(CASE):
		if lights[lightX][lightY] == 1:
			lights_lit += 1

print(lights_lit)