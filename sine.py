import math

n = 6

if n % 2 != 0:
    raise ValueError("n has to be even")

def sin(x):
    lb = 0
    for i in range(0, n):
        if i % 2 == 0:
            lb += x**(2*i+1) / math.factorial(2*i+1)
        else:
            lb -= x**(2*i+1) / math.factorial(2*i+1)
    ub = lb + x**(2*n+1) / math.factorial(2*n+1)
    return (lb, ub)

(lb, ub) = sin(1)
print("sin(1) is between %.10f and %.10f" %(lb, ub))
