import time
st = time.time()

lb = 0
ub = 0
n = 10**7

for i in range(0, n):
    if i % 2 == 0:
        lb += 1/(2*i+1)
    else:
        lb += -1/(2*i+1)

ub = lb + 1/(2*n+1)
lb *= 4
ub *= 4

lbs = str(lb)
ubs = str(ub)
k = 1
while k <= len(lbs) and k <= len(ubs) and lbs[0:k] == ubs[0:k]:
    k += 1
k -= 1

approx = float(lbs[0:k])

print(f"lb = {lb:.{k}f}")
print(f"ub = {ub:.{k}f}")
print(f"π = {approx:.{k-2}f}")
print("Calculated Pi with n=%d in %f seconds" %(n, time.time() - st))
