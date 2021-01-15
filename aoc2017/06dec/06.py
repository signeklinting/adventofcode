from collections import defaultdict

#banks = [int(i) for i in open('06.sample', 'r+').readline().strip().split(' ')]
banks = [int(i) for i in open('06.in', 'r+').readline().strip().split('\t')]

reallocations = 0
states = set()

while tuple(banks) not in states:
	states.add(tuple(banks))
	i_highest, blocks = banks.index(max(banks)), max(banks)
	banks[i_highest] = 0
	
	for i in range(1, blocks + 1):
		banks[(i_highest + i) % len(banks)] += 1
	reallocations += 1

print(reallocations)
state = tuple(banks)
new_reallocations = 0
while True:
	i_highest, blocks = banks.index(max(banks)), max(banks)
	banks[i_highest] = 0
	
	for i in range(1, blocks + 1):
		banks[(i_highest + i) % len(banks)] += 1
	new_reallocations += 1

	if tuple(banks) == state:
		print(new_reallocations)
		break