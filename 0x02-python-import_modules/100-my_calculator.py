#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if len(sys.argv) == 4:
        operatorDict = {"+": add, "-": sub, "*": mul, "/": div}
        result = operatorDict[operator](a, b)
        if operator not in operatorDict.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            print("{} {} {} = {}".format(a, operator, b, result))
