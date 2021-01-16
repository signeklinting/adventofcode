from collections import defaultdict, Counter

info = defaultdict(list)
weights = {}
towers = set()
aboves = set()
for line in open('07.in', 'r+').readlines():
#for line in open('07.sample', 'r+').readlines():
	line = line.strip()
	line = line.split(' -> ')
	tower, weight = line[0].split(' ')
	weights[tower] = int(weight[1:-1])
	towers.add(tower)
	info[tower]
	
	if len(line) > 1:
		for a in line[1].split(', '):
			aboves.add(a)
			info[tower].append(a)

bottom = list(towers^aboves)[0]
print(bottom)

def cal_weight(tower):
	if info[tower] == []:
		return weights[tower]
	
	sub_weights = []
	for a in info[tower]:
		sub_weights.append(cal_weight(a))

	if len(set(sub_weights)) == 1:
		return weights[tower] + sum(sub_weights)
	
	else:
		for w in set(sub_weights):
			if Counter(sub_weights)[w] == 1:
				wrong = w
				break
		i = [i for i, w in enumerate(sub_weights) if w == wrong][0]
		diff = sub_weights[(i + 1) % len(sub_weights)] - sub_weights[i]
		wrong_tower = info[tower][i]
		print(diff)
		print(wrong_tower)
		print(weights[wrong_tower] + diff)
		return weights[tower] + sum(sub_weights) + diff

print(cal_weight(bottom))

