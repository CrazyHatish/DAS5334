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

letters = list(ascii_lowercase)

words = word_list[:]
best_letters = []
for _ in range(5):
    filtered_words = [list(filter(lambda w: avoids(w, letter), words)) for letter in letters]
    words = min(filtered_words)
    best_letter = filtered_words.index(min(filtered_words))
    best_letters.append(letters[best_letter])
    letters.remove(letters[best_letter])

print(best_letters)
