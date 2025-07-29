import time
st = time.time()

lb = 0
ub = 0
n = 10**9

for i in range(0, n):
    if i % 2 == 0:
        lb += 1/(2*i+1)
    else:
        lb += -1/(2*i+1)

ub = lb + 1/(2*n+1)
lb *= 4
ub *= 4

precision = 9
if str(lb)[0:precision] == str(ub)[0:precision]:
    approx = float(str(lb)[0:precision])
    print("π = %.07f" %approx)
else:
    print("The lower bound and the upper bound do not match for this precision.")

print("Calculated Pi with n=%d and precision=%d in %f seconds" %(n, precision, time.time() - st))
