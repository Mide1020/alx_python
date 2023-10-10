#!/usr/bin/python
import sys

def print_args():
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name itself

    # Print the number of arguments and the list of arguments
    if num_args == 1:
        print("1 argument:")
    elif num_args > 1:
        print(f"{num_args} arguments:")
    else:
        print("0 arguments.")

    # Print the arguments, if any
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_args()
