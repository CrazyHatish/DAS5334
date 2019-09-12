def uses_only(word, letters):
    return set(word).issubset(set(letters))

print(uses_only('batata', 'btxa'))
