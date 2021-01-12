from collections import defaultdict


no_duplicates = 0
no_anagrams = 0

#for line in open('04.sample', 'r+').readlines():
for line in open('04.in', 'r+').readlines():
	line = line.strip()

	word_count = defaultdict(int)
	word_anagrams = defaultdict(int)
	for word in line.split(' '):
		word_count[word] += 1
		word_anagrams[tuple(sorted([i for i in word]))] += 1
	
	for v in word_count.values():
		if v > 1:
			break
	else:
		no_duplicates += 1

	for v in word_anagrams.values():
		if v > 1:
			break
	else:
		no_anagrams += 1

print(no_duplicates)
print(no_anagrams)



