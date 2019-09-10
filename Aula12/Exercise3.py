from string import ascii_lowercase

def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

forbidden_word = input('Enter the forbidden word: ')
matching_words = []

with open('words.txt', 'r') as file:
    word_list = [word.strip() for word in file]

for word in word_list:
    if avoids(word, forbidden_word):
        matching_words.append(word)

print(len(matching_words))

letters = ascii_lowercase
five_letters = []
for i in letters:
    for j in letters:
        for k in letters:
            for l in letters:
                if len(set([i, j, k, l])) == 4:
                    five_letters.append(i+j+k+l+'a')

biggest_set = []
best_word = ''
i = 1
for five_word in five_letters:
    matching_words = []
    for word in word_list:
        if avoids(word.strip(), five_word):
            matching_words.append(word.strip())
    if len(matching_words) > len(biggest_set):
        biggest_set = matching_words[:]
        best_word = five_word
    print("{} / {}".format(i, len(five_letters)))
    i += 1

print(best_word)

