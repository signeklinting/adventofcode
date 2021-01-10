from collections import Counter, defaultdict

answers = defaultdict(list)
n_group = 1

#for line in open('06.sample', 'r+').readlines():
for line in open('06.in', 'r+').readlines():	
	if line != '\n':
		answers[n_group].append(line.strip())
	else:
		n_group += 1

n_questions = 0
n_all_yes = 0
for group, questions in answers.items():
	counts = Counter(''.join(questions))
	group_size = len(questions)
	n_questions += len(counts.keys())
	n_all_yes += len([q for q, c in counts.items() if c == len(questions)])
	
print(n_questions)
print(n_all_yes)