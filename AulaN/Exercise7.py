def has_duplicates(l):
    if len(l) > 1:
        new_list = sorted(l)
        for i in range(len(l) - 1):
            if new_list[i] == new_list[i+1]:
                return True

    return False

my_list = [1, 2, 5, 4, 8]
print(has_duplicates(my_list))

