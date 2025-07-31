import time
import argparse
import os
import pickle
from datetime import date

class Record(dict):
    def __init__(self, lb, ub, pr, approx, te, n):
        self["lower_bound"] = lb
        self["upper_bound"] = ub
        self["precision"] = pr
        self["approximation"] = approx
        self["time_elapsed"] = format("%f seconds" %te)
        self["number_of_terms"] = n
        today = date.today()
        self["timestamp"] = format("%d-%d-%d" %(today.year, today.month, today.day))

def calculate(n):
    if n < 2 or n % 2 != 0:
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

    if k == 0:
        raise ValueError("n is too small")

    approx = float(lbs[0:k])
    return (lb, ub, k-1, approx)

def load():
    if os.path.exists("pi.pickle"):
        with open("pi.pickle", "rb") as file:
            return pickle.load(file)
    return []

def save(record):
    records = load()
    records.append(record)

    with open("pi.pickle", "wb") as file:
        pickle.dump(records, file)

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
        assert n >= 2 and n % 2 == 0
    except:
        print("Unable to parse n as a positive even integer")
        return

    st = time.time()
    try:
        (lb, ub, pr, approx) = calculate(n)
    except ValueError as err:
        print(err)
        return
    te = time.time() - st

    print("lb = %s" %str(lb))
    print("ub = %s" %str(ub))
    print(f"π = {approx:.{pr-1}f}")
    print("Precision: %d digits of precision" %pr)
    print("Method: We used a Taylor series with %s terms" %args.numberofterms)
    print("Time elapsed: %f seconds" %te)

    if args.save:
        record = Record(lb, ub, pr, approx, te, args.numberofterms)
        save(record)

if __name__ == "__main__":
    main()
