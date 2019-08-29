def gcd(a, b):
    na = max(a, b)
    nb = min(a, b)
    if nb == 0:
        return na
    else:
        return gcd(nb, na % nb)


print(gcd(26, 7))
