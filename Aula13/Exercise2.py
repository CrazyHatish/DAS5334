# Jeito feio v
def matching_strings():
	letters = ["a", "b", "c"]
	word_list = []
	for first in letters:
		for second in letters:
			for third in letters:
				for fourth in letters:
					for fifth in letters:
						for sixth in letters:
							word = first + second + third + fourth + fifth + sixth
							if (((first == 'a' and sixth == 'a') or first != 'a')
							and word.count('a') == word.count('b')
							and word.count('c') <= word.count('a')):
								word_list.append(word)

	return word_list

print("{} strings possuem estas propriedades".format(len(matching_strings())))

# Jeito bonito v
from itertools import product

def matching_strings2():
	word_list = []
	for word in product('abc', repeat=6):
		string = ''.join(word)
		if (((string[0] == 'a' and string[-1] == 'a') or string[0] != 'a')
		and string.count('a') == string.count('b')
		and string.count('c') <= string.count('a')):
			word_list.append(string)
	return word_list

print("{} strings possuem estas propriedades".format(len(matching_strings2())))