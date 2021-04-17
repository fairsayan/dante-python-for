import operator
occurrences = {}

with open('dante.txt') as file:
	for line in file:
		words = line.split(' ')
		for word in words:
			word = word.strip()
			if len(word) <= 3:
				continue
			occurrences[word] = occurrences.get(word, 0) + 1

	occurrences = sorted( occurrences.items(), key=operator.itemgetter(1), reverse=True )

	print(occurrences[:20])
