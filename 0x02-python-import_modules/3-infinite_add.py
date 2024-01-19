#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cmd_arg = sys.argv
    result = 0
    for arg in cmd_arg[1:]:
        result += int(arg)
    print("{}".format(result))
