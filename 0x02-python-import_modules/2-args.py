#!/usr/bin/python3
import sys
argv = sys.argv
count = 0
for i in argv:
    count += 1
count -= 1
print("{}".format(count), end=' ')
if count == 0:
    print("arguments.")
elif count == 1:
    print("argument:\n{}: Hello".format(count))
else:
    num = 1
    print("arguments:")
    for i in range(count):
        print("{}: {}".format(num, argv[num]))
        num += 1
