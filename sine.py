import math

n = 6

if n % 2 != 0:
    raise ValueError("n has to be even")

def translate(x):
    sign = -1 if x < 0 else 1
    x = abs(x) % (2*math.pi)
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

def isinteger(x):
    return float(x).is_integer()

def test(x):
    (lb, ub) = sin(x)
    if isinteger(x):
        print("sin(%d) is between %.20f and %.20f" %(x, lb, ub))
    else:
        print("sin(%f) is between %.20f and %.20f" %(x, lb, ub))

test(1)
test(10)
test(1.2)
