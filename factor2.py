import time
st = time.time()
from sympy import factorint

n = 884496532433
factors = factorint(n)
print(factors)
print("Factored 884496532433 in %f seconds" %(time.time() - st))
