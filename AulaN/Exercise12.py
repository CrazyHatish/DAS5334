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

reverse_pairs = []

for word in word_list:
	if word != word[::-1]:
		if bisect(word_list, word[::-1]):
			reverse_pairs.append([word, word[::-1]])

print(reverse_pairs)