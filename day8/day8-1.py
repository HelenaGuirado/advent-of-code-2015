import re

def characterSize(chars):
	if re.match(hexaCharacterPattern, chars):
		return 4
	elif re.match(escapedCharacterPattern, chars[0:2]):
		return 2
	return 1

escapedCharacterPattern = re.compile('\\\\.{1}')
hexaCharacterPattern = re.compile('\\\\x[a-z0-9]{2}')

charactersString = 0
charactersMemory = 0

with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

for line in lines:
	charactersString += len(line)
	indexChar = 1

	while indexChar < len(line) - 1:
		indexChar += characterSize(line[indexChar:indexChar+4])
		charactersMemory += 1

print(charactersString - charactersMemory)
