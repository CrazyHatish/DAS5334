def chop(l):
    del l[0]
    del l[-1]

my_list = [1, 2, 3, 4, 5]
print(chop(my_list), my_list)
