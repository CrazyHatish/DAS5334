word_list = []
with open('words.txt', 'r') as f:
    word_list = f.read().splitlines()

for word in word_list:
    if len(word) >= 6:
        for i in range(len(word)-5):
            if (word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]):
                print(word)
