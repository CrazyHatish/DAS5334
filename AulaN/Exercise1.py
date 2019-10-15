def nested_sum(l):
    s = 0
    for subl in l:
        s += sum(subl)

    return s

def one_liner(l):
    return sum([sum(subl) for subl in l])

print(nested_sum([[1, 2], [2, 3, 4], [8]]))
print(one_liner([[1, 2], [2, 3, 4], [8]]))
