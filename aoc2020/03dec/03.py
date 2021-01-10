

def count_trees(forest, slope = (1, 3)):
	
	tree_count = 0

	forest_rows = len(forest[0])
	forest_levels = len(forest)
	coord = (0, 0) 	# level, position

	while coord[0] != forest_levels - 1:
		coord = (coord[0] + slope[0], (coord[1] + slope[1]) % forest_rows)

		if forest[coord[0]][coord[1]] == "#":
			tree_count += 1
	return tree_count


forest = []

'''
for line in open('03.sample', 'r+').readlines():
	forest.append(line.strip())
'''

for line in open('03.in', 'r+').readlines():
	forest.append(line.strip())

print(count_trees(forest))


slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
multiply = 1

for slope in slopes:
	multiply *= count_trees(forest, slope=slope)
print(multiply)