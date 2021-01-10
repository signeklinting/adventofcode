

def find_seat(boarding_card, total_rows=128, total_seats=8, split_at=7):

	char_row = boarding_card[:split_at]
	char_seat = boarding_card[split_at:]

	min_row = 0
	max_row = total_rows
	for char in char_row:
		if char == "F":
			max_row -= (max_row-min_row)/2
		else:
			min_row += (max_row-min_row)/2
	
	min_seat = 0
	max_seat = total_seats
	for char in char_seat:
		if char == "L":
			max_seat -= int((max_seat-min_seat)/2)
		else:
			min_seat += int((max_seat-min_seat)/2)

	return int(min_row * 8 + min_seat)

boarding_cards = []

'''
for line in open('05.sample', 'r+').readlines():
	boarding_cards.append(line.strip())
'''

for line in open('05.in', 'r+').readlines():
	boarding_cards.append(line.strip())

all_seat_ids = []
for r in range(128):
	for s in range(8):
		all_seat_ids.append(r * 8 + s)

all_scanned_ids = []
for bc in boarding_cards:
	all_scanned_ids.append(find_seat(bc))
print(max(all_scanned_ids))

missing = list(set(all_seat_ids)-set(all_scanned_ids))
for m in missing:
	if m + 1 in all_scanned_ids:
		if m - 1 in all_scanned_ids:
			print(m)
