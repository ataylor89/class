# To test this program, type the following commands in Terminal or shell:
# % python testparser.py -e 10 -s
# % python testparser.py -e 10
# % python testparser.py
# % python testparser.py --exponent 20 --save
# % python testparser.py --save
# % python testparser.py --exponent 30

import argparse

parser = argparse.ArgumentParser(
        prog='testparser',
        description='We are testing out the argparse library',
        epilog='This text should appear at the bottom')

parser.add_argument('-e', '--exponent', required=True)
parser.add_argument('-s', '--save', action='store_true')

args = parser.parse_args()

print("Exponent = %s" %args.exponent)
print("Save = %s" %args.save)
