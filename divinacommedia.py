import operator
file = open('dante.txt')
occurences = {}

for line in file:
	words = line.split(' ')
	for word in words:
		word = word.strip()
		if len(word) <= 3:
			continue
		occurences[word] = occurences.get(word, 0) + 1

occurences = sorted( occurences.items(), key=operator.itemgetter(1) )

print(occurences[-20:])
file.close()