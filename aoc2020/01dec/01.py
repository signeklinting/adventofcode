from collections import defaultdict


def find_sum_of_two(expense_report, target_sum=2020):

	numbers = {}
	for n in expense_report:
		if (target_sum - n) in numbers:
			return (target_sum - n) * n
		numbers[n] = None
	return None


def find_sum_of_three(expense_report, target_sum=2020):

	for n in expense_report:
		res = find_sum_of_two(expense_report, target_sum= 2020 - n)
		if res:
			return res * n	

expense_report = []

'''
for line in open('01.sample', 'r+').readlines():
	expense_report.append(int(line.strip()))
'''

for line in open('01.in', 'r+').readlines():
	expense_report.append(int(line.strip()))


print(find_sum_of_two(expense_report))
print(find_sum_of_three(expense_report))