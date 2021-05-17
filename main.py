import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("lower", type=int,  help="Number to start generation from.")
    parser.add_argument("upper", type=int, help="Number to end generation.")

    return parser


parser = get_parser()
args = parser.parse_args()

lower = args.lower
upper = args.upper

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
