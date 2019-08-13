def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_twice(print_twice, 'spam')
do_four(print, 'spam')
