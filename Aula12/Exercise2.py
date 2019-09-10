def has_no_e(word):
    return 'e' not in word

with open('words.txt', 'r') as file:
    for line in file:
        if has_no_e(line):
            print(line.strip())
