def rotate_word(string, x):
    rotated = ''
    for letter in string:
        (A, Z) = (ord('a'), ord('z')) if letter.islower() else (ord('A'), ord('Z'))
        if ord(letter) + x < A:
            rotated += chr(ord(letter) + x + Z - A + 1)
        elif ord(letter) + x > Z:
            rotated += chr(ord(letter) + x - Z + A - 1)
        else:
            rotated += chr(ord(letter) + x)

    return rotated

print(rotate_word('JooJ', 13))
