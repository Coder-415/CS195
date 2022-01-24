#Adapt last week's program so that it prints out all the command line arguments, with any duplicated ones shown in all uppercase due 4/5.

import sys 
arg  = sys.argv[1:]

values = []

#Error proofing
if len(arg) == 0:
        print ("\nThere are no command line arguments provided, please enter some.\n")

#Using for loop to populate list
else:
	for item in arg:

#using .upper() to make duplicated values uppercase
		if arg.count(item) > 1:
			values.append(item.upper())
#adding non-duplicated values to list without uppercase
		else:
			values.append(item)

#converting list to dictionary to remove duplicates and reconverting to list once duplicates are removed
	values = list(dict.fromkeys(values))

#converting list to string to enable readibility
	values = str(values)[1:-1]
	print("\nHere is a list of given command line arguments without duplicates. Values which were duplicated are in all upper case:\n\n",values,"\n")
