from collections import defaultdict

rows = []
#for line in open('02.sample', 'r+').readlines():
for line in open('02.in', 'r+').readlines():
	rows.append(sorted([int(i) for i in line.strip().split('\t')])[::-1])
	#rows.append(sorted([int(i) for i in line.strip().split(' ')])[::-1])

chcksum = 0
for r in rows:
	chcksum += max(r) - min(r)
print(chcksum)

divisible = 0
for r in rows:
	for i in range(len(r) - 1):
		for j in range(i + 1, len(r)):
			if (r[i] % r[j]) == 0:
				divisible += (r[i] // r[j])
print(divisible)
