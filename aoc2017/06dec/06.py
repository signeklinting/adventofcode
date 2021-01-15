from collections import defaultdict

#banks = [int(i) for i in open('06.sample', 'r+').readline().strip().split(' ')]
banks = [int(i) for i in open('06.in', 'r+').readline().strip().split('\t')]


current_state = list(banks)
reallocations = 0
repeated = 0
states = [list(current_state)]

# Puzzle 1 & 2
while repeated < 2:
	i_highest, blocks = current_state.index(max(current_state)), max(current_state)
	reallocations += 1
	
	current_state[i_highest] = 0

	for i in range(1, blocks + 1):
		current_state[(i_highest + i) % len(current_state)] += 1
	
	if current_state in states:
		print(reallocations)
		repeated += 1
		reallocations = 0
		states = []
	
	states.append(list(current_state))

