from math import sqrt


def data_manhattan(i):

	if i == 1:
		return 0
	else: 
		# The base of the square were the data is located
		if int(sqrt(i)) % 2 == 0:
			sq_base = int(sqrt(i)) + 1
		else:
			sq_base = int(sqrt(i)) + 2
			if i == (sq_base - 2) ** 2:
				sq_base -= 2
		
		# The level, meaning the distance from the center (data = 1)
		sq_level = (sq_base - 1) // 2

		# The data values in the corners:
		first_corner = (sq_base - 2) ** 2 + sq_base  - 1
		last_corner = sq_base ** 2
		step = sq_base - 1
		corners = [i for i in range(first_corner, last_corner + 1, step)]
		
		# The distance from each corner
		dist_corners = []
		for c in corners:
			dist_corners.append(abs(c - i))
		
		return sq_level - sorted(dist_corners)[0] + sq_level

tests = [1, 12, 23, 1024]
for i in tests:
	print(data_manhattan(i))

my_input = 289326
print(data_manhattan(my_input))

moves = {
	'U': (0, 1),
	'D': (0, -1),
	'R': (1, 0),
	'L': (-1, 0),
	'N': (1, 0)
}

grid = {(0, 0):1}
current_coord = (0, 0)
sq_base = 1
sq_level = 1

cnt = 0
state = 'N'

value = 0
while value < my_input:
	current_coord = (current_coord[0] + moves[state][0], current_coord[1] + moves[state][1])

	if state == 'N':
		state = 'U'
	elif state == 'U':
		if current_coord[1] == sq_level:
			state = 'L'
	elif state == 'L':
		if current_coord[0] == - sq_level:
			state = 'D'
	elif state == 'D':
		if current_coord[1] == - sq_level:
			state = 'R'
	elif state == 'R':
		if current_coord[0] == sq_level:
			state = 'N'
			sq_base += 2
			sq_level += 1
	
	value = 0
	for i in (0, 1, -1):
		for j in (0, 1, -1):
			if i != 0 or j != 0:
				if (current_coord[0] + i, current_coord[1] + j) in grid.keys():
					value += grid[(current_coord[0] + i, current_coord[1] + j)]
	grid[current_coord] = value

print(value)	