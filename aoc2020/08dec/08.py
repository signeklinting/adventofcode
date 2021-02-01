from collections import defaultdict

instructions = []

for line in open('08.in', 'r+').readlines():
#for line in open('08.sample', 'r+').readlines():
	instructions.append(tuple(line.strip().split(' ')))


def run_program(instructions):
	accumulator = 0
	i = 0
	visited = set()
	terminated = False

	while True:
		instr = instructions[i]
		if instr[0] == 'nop':
			i += 1
		elif instr[0] == 'jmp':
			i += int(instr[1])
		elif instr[0] == 'acc':
			i += 1
			accumulator += int(instr[1])
		if i in visited:
			return accumulator, terminated
		elif i == len(instructions):
			terminated = True
			return accumulator, terminated
		else:
			visited.add(i)


def find_bug(instructions):
	for i, instr in enumerate(instructions):
		if instr[0] == 'jmp':
			instructions[i] = ('nop', instr[1])
			if run_program(instructions)[1]:
				return run_program(instructions)[0]
			instructions[i] = ('jmp', instr[1])
		elif instr[0] == 'nop':
			instructions[i] = ('jmp', instr[1])	
			if run_program(instructions)[1]:
				return run_program(instructions)[0]
			instructions[i] = ('nop', instr[1])
		
# First puzzle
print(run_program(instructions))

# Second puzzle
print(find_bug(instructions))