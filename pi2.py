import time
st = time.time()
import argparse

def calculate(n):
    if n <= 0 or n % 2 != 0:
        raise ValueError("n has to be a positive even integer")

    lb = 0
    ub = 0

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
    return (lb, ub, approx)

def main():
    parser = argparse.ArgumentParser(
            prog="pi2.py",
            description="Calculate π using a Taylor series with n terms",
            epilog="What's the exact value of π? Perfect integrity.")

    parser.add_argument("-n", "--numberofterms", required=True)
    parser.add_argument("-s", "--save", action="store_true")

    args = parser.parse_args()

    try:
        n = int(float(args.numberofterms))
        assert n > 0 and n % 2 == 0
    except:
        raise ValueError("Unable to parse n as a positive even integer")

    (lb, ub, approx) = calculate(n)
    k = len(str(approx))

    print("lb = %s" %str(lb))
    print("ub = %s" %str(ub))
    print(f"π = {approx:.{k-2}f}")
    print("Precision: %d digits of precision" %(k-1))
    print("Method: We used a Taylor series with %s terms" %args.numberofterms)
    print("Time elapsed: %f seconds" %(time.time() - st))

if __name__ == "__main__":
    main()
