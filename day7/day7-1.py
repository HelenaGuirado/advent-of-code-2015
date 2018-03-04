import re
from collections import defaultdict

BITMAX = 0xFFFF

class Gate:
	def __init__(self, inputSymbol1, inputSymbol2, outputSymbol, operation):
		self.inputSymbol1 = inputSymbol1
		self.inputSymbol2 = inputSymbol2
		self.outputSymbol = outputSymbol
		self.operation = operation

gates = []
wiresValue = {}

def andGate(inputSymbol1, inputSymbol2):
	return inputSymbol1 & inputSymbol2 & BITMAX

def orGate(inputSymbol1, inputSymbol2):
	return inputSymbol1 | inputSymbol2 & BITMAX

def lsifhtGate(inputSymbol1, inputSymbol2):
	return inputSymbol1 << inputSymbol2 & BITMAX

def rshitfGate(inputSymbol1, inputSymbol2):
	return inputSymbol1 >> inputSymbol2 & BITMAX

def notGate(inputSymbol1):
	return BITMAX ^ inputSymbol1 & BITMAX

def getValue(inputSymbol):
	if re.match(numberPattern, inputSymbol):
		return int(inputSymbol)

	if inputSymbol in wiresValue:
		return int(wiresValue[inputSymbol])

	return None

with open('input.txt', 'r') as file:
   lines = file.read().split('\n')

instructionsPattern = re.compile('[A-Z]+')
valuesPattern = re.compile('[a-z0-9]+')
numberPattern = re.compile('[0-9]+')

for line in lines:
	instruction = instructionsPattern.findall(line)
	values = valuesPattern.findall(line)

	if len(instruction) == 0:
		instruction.append("affect")

	if len(values) == 2:
		gate = Gate(values[0], None, values[1], instruction[0])
	else:
		gate = Gate(values[0], values[1], values[2], instruction[0])

	gates.append(gate)

while 'a' not in wiresValue:
	for gate in gates:
		if gate.outputSymbol not in wiresValue:
			value1 = getValue(gate.inputSymbol1)

			if gate.inputSymbol2 != None:
				value2 = getValue(gate.inputSymbol2)

			if (value1 != None and gate.inputSymbol2 == None) or (value1 != None and value2 != None and gate.inputSymbol2 != None):
				if gate.operation == "NOT":
					wiresValue[gate.outputSymbol] = notGate(value1)

				elif gate.operation == "AND":
					wiresValue[gate.outputSymbol] = andGate(value1, value2)

				elif gate.operation == "OR":
					wiresValue[gate.outputSymbol] = orGate(value1, value2)

				elif gate.operation == "LSHIFT":
					wiresValue[gate.outputSymbol] = lsifhtGate(value1, value2)

				elif gate.operation == "RSHIFT":
					wiresValue[gate.outputSymbol] = rshitfGate(value1, value2)

				else:
					wiresValue[gate.outputSymbol] = value1

print(wiresValue['a'])
