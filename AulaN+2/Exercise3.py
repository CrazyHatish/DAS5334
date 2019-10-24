known = {}

def ack(m, n):
    if (m, n) in known:
        return known[(m, n)]

    if m == 0:
        known[(m, n)] = n+1
        return n+1
    elif m > 0 and n == 0:
        known[(m, n)] = ack(m-1, 1)
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        known[(m, n)] = ack(m-1, ack(m, n-1))
        return ack(m-1, ack(m, n-1))


print(ack(2, 223))
print(known)
