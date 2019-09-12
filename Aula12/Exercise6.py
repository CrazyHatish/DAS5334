def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True


abecedarian_words = []
with open('words.txt', 'r') as f:
    abecedarian_words = list(filter(is_abecedarian, f.read().splitlines()))

print(abecedarian_words)
