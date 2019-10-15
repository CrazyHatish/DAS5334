def cumsum(l):
    s = []
    for i in range(len(l)):
        s.append(sum(l[:i+1]))

    return s

print(cumsum([1, 2, 3, 4, 5]))
