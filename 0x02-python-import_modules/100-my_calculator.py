#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if len(sys.argv) == 4:
        if operator == '+':
            result = add(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '-':
            result = sub(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '*':
            result = mul(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '/':
            result = div(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")

    else:
        print("Usage: {} {} {} {}".format(sys.argv[0], a, operator, b))
        sys.exit(1)
