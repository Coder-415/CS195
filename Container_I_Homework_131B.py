#Container_I_Homework_131B.py

import sys

if len(sys.argv) > 1:
	args_only = sys.argv [1:]
	reversed_args = args_only [::-1]
	print ("".join(reversed_args))
else:
	print("Run this program again w/ command line arguments, and\
 it will print those arguments in reverse order.")


