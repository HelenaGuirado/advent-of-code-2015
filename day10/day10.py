INPUT = "1321131112"

def compute(input):
    string = ""
    pos = 0
    while pos < len(input):
        char = input[pos]
        if pos + 2 < len(input) and input[pos:pos+3] == char * 3:
            string += "3" + char
            pos += 3
        elif pos + 1 < len(input) and input[pos:pos+2] == char * 2:
            string += "2" + char
            pos += 2
        else:
            string += "1" + char
            pos += 1
    return string

output = INPUT

for idx in range(40):
    output = compute(output)
part_1 = len(output)

for idx in range(10):
    output = compute(output)
part_2 = len(output)

print("Day 10 part 1 result: " + str(part_1))
print("Day 10 part 2 result: " + str(part_2))