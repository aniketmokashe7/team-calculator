import argparse
from calculator import add, subtract, multiply, divide
from advanced import sqrt, power, percentage

parser = argparse.ArgumentParser(description="Team Calculator")
subparsers = parser.add_subparsers(dest="cmd")

# Basic ops parser
basic = subparsers.add_parser("basic", help="basic operations: add, sub, mul, div")
basic.add_argument("op", choices=["add","sub","mul","div"])
basic.add_argument("a", type=float)
basic.add_argument("b", type=float)

# Advanced ops parser
adv = subparsers.add_parser("adv", help="advanced ops: sqrt, pow, pct")
adv.add_argument("op", choices=["sqrt","pow","pct"])
adv.add_argument("x", type=float)
adv.add_argument("--y", type=float, default=None)  # optional second arg

args = parser.parse_args()

if args.cmd == "basic":
    a, b = args.a, args.b
    if args.op == "add":
        print(add(a,b))
    elif args.op == "sub":
        print(subtract(a,b))
    elif args.op == "mul":
        print(multiply(a,b))
    elif args.op == "div":
        print(divide(a,b))

elif args.cmd == "adv":
    if args.op == "sqrt":
        print(sqrt(args.x))
    elif args.op == "pow":
        if args.y is None:
            raise SystemExit("pow requires --y")
        print(power(args.x, args.y))
    elif args.op == "pct":
        if args.y is None:
            raise SystemExit("pct requires --y (whole)")
        print(percentage(args.x, args.y))
else:
    parser.print_help()