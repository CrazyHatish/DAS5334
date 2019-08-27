def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

a = input("Input a: ")
b = input("Input b: ")
c = input("Input c: ")
n = input("Input n: ")
check_fermat(int(a), int(b), int(c), int(n))
