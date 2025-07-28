import math

def translate(x):
    sign = -1 if x < 0 else 1
    x = abs(x) % (2*math.pi)
    if x > math.pi/2:
        x = math.pi - x
    return sign * x

def sin(x):
    n = 30
    if n % 2 != 0:
        raise ValueError("n has to be even")
    x = translate(x)
    lb = 0
    for i in range(0, n):
        if i % 2 == 0:
            lb += x**(2*i+1) / math.factorial(2*i+1)
        else:
            lb -= x**(2*i+1) / math.factorial(2*i+1)
    ub = lb + x**(2*n+1) / math.factorial(2*n+1)
    if lb != ub:
        raise ValueError("n is too small")
    return lb

def cos(x):
    n = 30
    if n % 2 != 0:
        raise ValueError("n has to be even")
    x = translate(x)
    lb = 0
    for i in range(0, n):
        if i % 2 == 0:
            lb += x**(2*i) / math.factorial(2*i)
        else:
            lb -= x**(2*i) / math.factorial(2*i)
    ub = lb + x**(2*n) / math.factorial(2*n)
    if lb != ub:
        raise ValueError("n is too small")
    return lb

print("sin(0) = %f" %sin(0))
print("sin(1) = %f" %sin(1))
print("sin(10) = %f" %sin(10))
print("sin(1.2) = %f" %sin(1.2))
print("cos(0) = %f" %cos(0))
print("cos(1) = %f" %cos(1))
