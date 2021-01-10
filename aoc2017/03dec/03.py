from math import floor, sqrt, ceil

i = 49

if int(sqrt(i)) % 2 == 0:
	sqbase_inner = int(sqrt(i)) - 1
	sqbase = int(sqrt(i)) + 1
else:
	sqbase_inner = int(sqrt(i))
	sqbase = int(sqrt(i)) + 2

corner_inner = (sqbase_inner - 1) // 2
corner = (sqbase - 1) // 2
from_corner = (i - sqbase_inner ** 2) % (sqbase_inner + 1)
dist_hort = corner
dist_vert = corner - from_corner
print(dist_hort + dist_vert)






