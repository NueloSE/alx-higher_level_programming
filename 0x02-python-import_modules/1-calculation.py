#!/usr/bin/python3
import calculator_1 as cal
if __name__ == "__main__":
    a = 10
    b = 5
    addition = cal.add(a, b)
    subtraction = cal.add(a, b)
    multiplication = cal.mul(a, b)
    division = cal.div(a, b)

    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, subtraction))
    print("{} * {} = {}".format(a, b, multiplication))
    print("{} / {} = {}".format(a, b, division))
