import sys

arg = sys.argv[1]
print(arg[::-1])

if not sys.argv[1]:
	print ("You failed to add a command line argument")
