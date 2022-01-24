#Write a program that prints out the command line arguments it receives, in alphabetical order and without duplicates

import sys #Loading module required 

length = len(sys.argv) #Determining number of command line arguments 

def no_duplicates(values):
	return list (dict.fromkeys(values)) #Removing duplicates by creatng a dictionary from the list and then returning values from dictionary to list
x = (sys.argv[1:]) #Identifying what to sort
a = sorted(no_duplicates(x)) #Sorting values and using function to remove duplicates
a.sort(key=str.casefold) #Ensuring that case does not affect sorting

if length > 1: 
	print ("\nThe command line arguments received in alphabetical and/or numerical order and without duplicates are: \n",a,"\n")
else: 
	print ("\nProgram has no Command Line Arguments\n")
	
