#Write a program that indicates whether there are fewer than one, exactly one, or more than one duplicated command line argument


#Importing Module
import sys 

#Defining scope
arg = (sys.argv[1:])

#Enabling bold text
start = "\033[1m"
end = "\033[0m"

#Error proofing
if len(arg) == 0:
        print ("\nThere are", start + "no command line arguments" + end, "provided, please enter some.\n")

else:

#Creating list of duplicates
	duplicates = []

#Populating list of duplicates
	for item in arg:
		if arg.count(item) > 1:
                	duplicates.append(item)

#Sorting set of unique duplicate values wihout distinction for case
	ds = sorted(set(duplicates),key = str.casefold)

#Creating flow 
	if len(duplicates) == 0:
        	print ("\nThere are",start + "fewer than one" +  end, "duplicated command line arguments.\n")
	elif len(set(duplicates)) == 1:
        	print ("\nThere is", start + "exactly one" + end,"duplicated command line argument and it is:","".join(ds),"\n")
	else:
		print("\nThere are",start + "more than one" + end,"duplicated command line arguments and here is a sorted list of the arguments duplicated:",",".join(ds),"\n")
