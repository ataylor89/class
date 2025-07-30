import argparse

parser = argparse.ArgumentParser(
        prog='testparser',
        description='We are testing out the argparse library',
        epilog='This text should appear at the bottom')

parser.add_argument('-e', '--exponent')
parser.add_argument('-s', '--save', action='store_true')

args = parser.parse_args()

print("Exponent = %s" %args.exponent)
print("Save = %s" %args.save)
