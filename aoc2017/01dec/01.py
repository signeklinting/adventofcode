from collections import defaultdict

#captcha = open('01.sample', 'r+').readline().strip()
captcha = open('01.in', 'r+').readline().strip()

n = 0
for i, d in enumerate(captcha):
	if captcha[(i + 1) % len(captcha)] == d:
		n += int(d)
print(n)

m = 0
for i, d in enumerate(captcha):
	if captcha[(i + len(captcha) // 2) % len(captcha)] == d:
		m += int(d)
print(m)