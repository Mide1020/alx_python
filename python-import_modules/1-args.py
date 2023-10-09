#!/usr/bin/python
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name itself

# Print the number of arguments and the list of arguments
if num_args == 0:
    print("Number of argument(s): 0.")
    print(".")
else:
    print(f"Number of argument(s): {num_args}.")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
