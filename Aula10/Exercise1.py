from math import sqrt

def mysqrt(a, x):
    Ɛ = 0.02
    while True:
        y = (x + a/x) / 2
        if abs(y-x) <= Ɛ:
            return y
        x = y

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(9):
        my = mysqrt(a+1, (a+1)*2/3)
        msqrt = sqrt(a+1)
        print("{:.1f} {:<13f} {:<13f} {:<13f}".format(a+1, my, msqrt, abs(my - msqrt)))

test_square_root()
