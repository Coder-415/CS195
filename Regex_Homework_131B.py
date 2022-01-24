#Write a program that indicates the single greatest integer in the text /users/abrick/resources/urantia.txt

import sys
import re 

arg = (sys.argv[1:])

x = "/users/abrick/resources/urantia.txt"

def largest_integer(file_name):
	file = open(file_name)
	numbers = [line.split() for line in file]
	numbers = max(re.findall("\d+",str(numbers)))	
	print("\nThe single greatest integer in the file",file_name,"is: ","{:,}".format(int(numbers)),"\n")
	
	#Using max value of regex findall function specified to look for integers and made to be greedy

if len(arg) == 0:
	largest_integer(x)
else:
	try:
		y = "".join(arg)
		largest_integer(y)
	except FileNotFoundError:
		largest_integer(x) 
