#Write a program that estimates the number of words in the text /users/abrick/resources/urantia.txt

import sys
import re

arg = (sys.argv[1:])

if len(arg)== 0:
	print("\nPlease enter a valid file name.\n")
else:
	file_name = arg
	with open(file_name[0],'r') as f:

#Opening up file with zero index to avoid error

		words = [line.split() for line in f]

#Splitting up lines to enable counting 

		words = re.findall("\w+",str(words))

#Using 're' to find all strings containing combinations of word characters

		print("\nThe number of words in the file is: ",f'{len(words):,}')

