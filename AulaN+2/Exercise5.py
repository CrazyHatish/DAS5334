def rotate_word(word):
    words = []
    for i in range(1, len(word)):
        new_word = word[i:] + word[:i]
        words.append(new_word)

    return words


def translate_word(word, x):
    rotated = ''
    for letter in word:
        (A, Z) = (ord('a'), ord('z')) if letter.islower() else (ord('A'), ord('Z'))
        if ord(letter) + x < A:
            rotated += chr(ord(letter) + x + Z - A + 1)
        elif ord(letter) + x > Z:
            rotated += chr(ord(letter) + x - Z + A - 1)
        else:
            rotated += chr(ord(letter) + x)

    return rotated

words = {}

with open("words.txt", "r") as file:
    for word in file:
        words[word.strip('\n')] = {"translated": [], "rotated": []}

i = 1
length = len(words)

for word in words:
    for rotation in rotate_word(word):
        words[word]["rotated"].append(rotation) if rotation in words else None
    for n in range(1, 26):
        translated = translate_word(word, n)
        words[word]["translated"].append(translated) if translated in words else None

    print("{}/{}".format(i, length))
    i += 1

[print("{} - Rotacionado: {}; Translacionado: {}".format(word, words[word]["rotated"], words[word]["translated"])) for word in words if words[word]["rotated"] != [] or words[word]["translated"] != []]
