
passwords = {}

'''
for line in open('02.sample', 'r+').readlines():
	rule, string = line.strip().split(': ')
	count, letter = rule.split(' ')
	count = [int(i) for i in count.split('-')]

	passwords[string] = tuple(count + [letter])
'''

for line in open('02.in', 'r+').readlines():
	rule, string = line.strip().split(': ')
	count, letter = rule.split(' ')
	count = [int(i) for i in count.split('-')]

	passwords[string] = tuple(count + [letter])


counter = 0
for string, rule in passwords.items():
	if string.count(rule[2]) in range(rule[0], rule[1] + 1):
		counter += 1
print(counter)


counter = 0
for string, rule in passwords.items():
	if (string[rule[0]-1] == rule[2]) ^ (string[rule[1]-1] == rule[2]):
		counter += 1
print(counter)