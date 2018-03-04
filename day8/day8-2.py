import re

def characterSize(char):
	if char == "\\" or char == '"' :
		return 2
	return 1

charactersOriginalString = 0
charactersNewlyEncodedString = 0

with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

for line in lines:
	charactersOriginalString += len(line)
	indexChar = 0

	for char in line:
		charactersNewlyEncodedString += characterSize(char)

	charactersNewlyEncodedString += 2

print(charactersNewlyEncodedString - charactersOriginalString)
