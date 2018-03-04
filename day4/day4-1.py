import hashlib
import re

with open("input.txt", "r") as file:
	content = file.read()
	
i = 0
hash_okay = True

while hash_okay:
	hash = content + str(i)
	hashed = hashlib.md5(hash.encode('utf-8')).hexdigest()
	pattern = re.search('^0{5}\w+', hashed)
	if pattern is not None:
		hash_okay = False
	else:
		i += 1
print(i)