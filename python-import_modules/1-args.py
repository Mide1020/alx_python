#!/usr/bin/python
import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("No arguments were passed.")
else:
    if num_args == 1:
     print("1 argument:")
    else:
        print("{} arguments were passed:".format(num_args))

    for i, arg in enumerate(args, 1):
        print("{}:{}".format(i, arg))
if __name__  == "__main__":
    print()