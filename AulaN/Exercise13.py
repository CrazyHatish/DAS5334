def bisect(l, word):
	new_l = l[:]
	length = len(new_l)
	index = int(length/2)
	i = index

	while length > 1:
		if word == new_l[i]:
			return index

		elif word > new_l[i]:
			new_l = new_l[i:]
			length = len(new_l)
			i = int(length/2)
			index += i

		else:
			new_l = new_l[:i]
			length = len(new_l)
			i = int(length/2)
			index -= length - i

	return None

word_list = []

with open('words.txt', 'r') as file:
	for line in file:
		word_list.append(line.strip())

interlock = []
i = 0
num_words = len(word_list)

for word in word_list:
        i += 1
        print("{}/{} (1/2)".format(i, num_words))
        word1 = word[::2]
        word2 = word[1::2]
        if bisect(word_list, word1) and bisect(word_list, word2):
                interlock.append([word1, word2, word])

i = 0

for word in word_list:
        i += 1
        print("{}/{} (2/2)".format(i, num_words))
        word1 = word[::3]
        word2 = word[1::3]
        word3 = word[2::3]
        if bisect(word_list, word1) and bisect(word_list, word2) and bisect(word_list, word3):
                interlock.append([word1, word2, word3, word])

print(interlock)
