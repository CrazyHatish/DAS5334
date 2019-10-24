def invert_dict(d):
    inverted = dict()
    for key in d:
        inverted.setdefault(d[key], [])
        inverted[d[key]].append(key)
    return inverted

print(invert_dict({'a': 4, 'b': 4, 'c': 1, 'd':1, 'e': 5}))
