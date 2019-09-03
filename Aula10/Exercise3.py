from math import factorial as fac
from math import sqrt

def estimate_pi():
    current_sum = 0
    current_term = 1
    k = 0
    while current_term > 1e-15:
        current_term = ((fac(4*k)*(1103+26390*k))/((fac(k)**4)*396**(4*k)))
        current_sum += current_term
        k += 1
    return ((2*sqrt(2)/9801)*current_sum)**-1

print(estimate_pi())
