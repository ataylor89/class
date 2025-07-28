import math

n = 20

if n % 2 != 0:
    raise ValueError("n has to be even")

def translate(x):
    sign = 1 if x > 0 else -1
    x = abs(x) % (2*math.pi)
    if x > math.pi:
        sign *= -1
        x = 2*math.pi - x
    if x > math.pi/2:
        x = math.pi - x
    return sign * x

def sin(x):
    x = translate(x)
    lb = 0
    for i in range(0, n):
        if i % 2 == 0:
            lb += x**(2*i+1) / math.factorial(2*i+1)
        else:
            lb -= x**(2*i+1) / math.factorial(2*i+1)
    ub = lb + x**(2*n+1) / math.factorial(2*n+1)
    return (lb, ub)

def test(x):
    (lb, ub) = sin(x)
    if isinstance(x, int):
        if lb == ub:
            print("sin(%d) = %.20f" %(x, lb))
        else:
            print("sin(%d) is between %.20f and %.20f" %(x, lb, ub))
    else:
        if lb == ub:
            print("sin(%f) = %.20f" %(x, lb))
        else:
            print("sin(%f) is between %.20f and %.20f" %(x, lb, ub))

test(1)
test(10)
test(1.2)
