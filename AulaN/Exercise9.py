def has_duplicates(l):
    if len(l) > 1:
        new_list = sorted(l)
        for i in range(len(l) - 1):
            if new_list[i] == new_list[i+1]:
                return True

    return False


def delete_duplicates(l):
	while has_duplicates(l):
		new_list = sorted(l)
		
		for i in range(len(l) - 1):
			if new_list[i] == new_list[i+1]:
				l.remove(new_list[i])

my_list = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,5,5,6]
delete_duplicates(my_list)
print(my_list)