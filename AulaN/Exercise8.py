from random import randint

def has_duplicates(l):
    if len(l) > 1:
        new_list = sorted(l)
        for i in range(len(l) - 1):
            if new_list[i] == new_list[i+1]:
                return True

    return False

birthdays_lists = []

for _ in range(10000):
    bday_list = []

    for _ in range(23):
        bday_list.append(randint(1, 365))

    birthdays_lists.append(bday_list)

duplicates_list = list(filter(has_duplicates, birthdays_lists))

print("{} de 10000 turmas têm aniversários coincidentes ({:.2f}%)".format(len(duplicates_list), len(duplicates_list)/100))
