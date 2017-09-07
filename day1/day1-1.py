f = open("input.txt", "r")
content = f.read()

result = content.count('(') - content.count(')')

print(result)