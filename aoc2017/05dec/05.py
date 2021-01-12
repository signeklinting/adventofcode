from collections import defaultdict

#instructions = [int(line.strip()) for line in open('05.sample', 'r+').readlines()]
instructions = [int(line.strip()) for line in open('05.in', 'r+').readlines()]


def offset_part1(instructions):

	instr = list(instructions)

	current = 0
	cnt = 0
	while current in range(len(instr)):
		step = instr[current]
		instr[current] += 1
		current += step
		cnt += 1
	return cnt


def offset_part2(instructions):

	instr = list(instructions)

	current = 0
	cnt = 0
	while current in range(len(instr)):
		step = instr[current]
		if step >= 3:
			instr[current] -= 1
		else:
			instr[current] += 1	
		current += step
		cnt += 1
	return cnt

print(offset_part1(instructions))
print(offset_part2(instructions))