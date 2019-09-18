def func(n, i=0):
	print(n)
	if len(str(n)) == 1:
		return (n, i)
	else:
		new_num = 1
		for num in str(n):
			new_num *= int(num)
		return func(new_num, i+1)