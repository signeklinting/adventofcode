from collections import defaultdict

bags = defaultdict(list)

#for line in open('07.sample', 'r+').readlines():
for line in open('07.in', 'r+').readlines():
	bag, content = line.strip()[:-1].split( ' bags contain ')
	content_items = []
	if 'no' not in content:
		for item in content.split(', '):
			content_items.append((item.split(' ')[0], ' '.join(item.split(' ')[1:-1])))
	
	bags[bag] = content_items

n_colors = 0
my_bag_color = 'shiny gold'


for color in bags.keys():
	if color != my_bag_color:
		queue = [color]
		visisted = {color}

		while queue:
			current_color = queue.pop()
			if current_color == my_bag_color:
				n_colors += 1
				break
			new_colors = bags[current_color]

			for num, new_color in new_colors:
				if new_color not in visisted:
					queue.insert(0, new_color)
print(n_colors)
