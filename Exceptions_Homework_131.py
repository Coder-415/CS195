#Extend the last program so that non-numeric arguments are regarded as integers with value equivalent to their length in characters

import sys
import statistics

def Count_Strings(item,arglist):
        try:
            	return int(item)
        except ValueError:
                return len(item)
                return int(item)

output = [Count_Strings(arg, sys.argv[1:]) for arg in sys.argv[1:]]
output.sort(reverse=True)

if len(sys.argv[1:])== 0:
	print("\nThere are no command line arguments. Plese enter some values!\n")
else:
	print ('-'*80) 
	print("These are the values which you entered: \n",sys.argv[1:])
	print("\nThese are the values entered with any strings having been converted to integers based on their character length(sorted from highest to lowest):\n", output)
	print("\nThe median of the values you entered is - ", statistics.median(output))
	try:
		print("\nThe mode of the values you entered is - ", statistics.mode(output),"\n")
		print ('-'*80) 
	except statistics.StatisticsError:
		from collections import Counter
		from itertools import groupby
		#Loading modules to count values and groupby 

		freqs = groupby(Counter(output).most_common(),lambda values:values[1])
		#Iterating through values in numbers list to identify  most common values

		most_freqs = [val for val, count in next(freqs)[1]]
		#Selecting only most common values

		mode_list = ' ,'.join([str(elem) for elem in most_freqs])
		#Converting to string

		print("\nThere are multiple modes, these are their values: ",mode_list) 
		#Error proofing in case there is more than one mode
		
		print ('-'*80)
