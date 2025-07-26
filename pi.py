lb = 0
ub = 0
n = 10000

for i in range(0, n):
    if i % 2 == 0:
        lb += 1/(2*i+1)
    else:
        lb += -1/(2*i+1)

ub = lb + 1/(2*n+1)
lb *= 4
ub *= 4

print("π is between %f and %f" %(lb, ub))
