#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def sign_check(sign):
    idx = 0
    signs = ['+', '-', '*', '/']
    for i in signs:
        if i == sign:
            return idx
        idx += 1
    return -1


def calculation(num1, num2, operand):
    operands = [add, sub, mul, div]
    return (operands[operand](num1, num2))


if __name__ == "__main__":

    cmd_arg = sys.argv
    if (len(cmd_arg[1:]) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sig = cmd_arg[2]
    index = sign_check(sig)
    if (index == -1):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(cmd_arg[1])
        b = int(cmd_arg[3])
        result = calculation(a, b, index)
        print("{} {} {} = {}".format(a, sig, b, result))
