#!/usr/bin/python3
import calculator_1 as cal
if __name__ == "__main__":
    a = 10
    b = 5
    addition = cal.add(a, b)
    subtraction = cal.add(a, b)
    multiplication = cal.mul(a, b)
    division = cal.div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addition))
    print("{:d} - {:d} = {:d}".format(a, b, subtraction))
    print("{:d} * {:d} = {:d}".format(a, b, multiplication))
    print("{:d} / {:d} = {:d}".format(a, b, division))
