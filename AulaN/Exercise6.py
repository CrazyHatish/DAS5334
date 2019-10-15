def is_anagram(s1, s2):
    l1 = list(s1)
    l2 = list(s2)

    return sorted(l1) == sorted(l2)

print(is_anagram("batata", "tatbaa"))

