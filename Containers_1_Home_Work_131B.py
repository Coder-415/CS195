import sys

arg = sys.argv[1]
#print(arg[::-1])


if not sys.argv[1]: 
	print ("You have failed to add a command line argument")
else:
	print(arg[::-1])

