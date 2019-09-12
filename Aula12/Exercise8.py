def format_num(n):
    return '{:06}'.format(n)

for i in range(1000000):
    if (format_num(i)[-4:] == format_num(i)[-1:-5:-1]
    and format_num(i+1)[-5:] == format_num(i+1)[-1:-6:-1]
    and format_num(i+2) == format_num(i+2)[::-1]):
        print(format_num(i))
