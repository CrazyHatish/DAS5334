def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    return word[::-1] == word

def dumb_way(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    else:
        return dumb_way(middle(word))

print(dumb_way("joceecoj"))

