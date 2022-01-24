#Write a program that reports the median and mode(s) of the numeric command line arguments, using functions that determine these statistics

import sys 
import statistics #Loading modules required 

x = sys.argv[1:]

numbers = []

for n in x:
	if n.isdigit():
		numbers.append(int(n)) #Creating list of numbers to enable the calculation of the medium even if words are present in list

numbers_list = ', '.join([str(elem) for elem in numbers])
#Breaking up numbers list to make it more clean


if len (numbers) > 0: 
	print("\nThese are the numbers you entered: ", numbers_list)
	
	print("\nThe median of the numbers you entered is - ", statistics.median(numbers))

	try: 
		print("\nThe mode of the values you entered is - ", statistics.mode(x),"\n")
	except statistics.StatisticsError:
		from collections import Counter
		from itertools import groupby
		#Loading modules to count values and groupby 

		freqs = groupby(Counter(numbers).most_common(),lambda values:values[1])
		#Iterating through values in numbers list to identify  most common values

		most_freqs = [val for val, count in next(freqs)[1]]
		#Using for loop to select only most common values

		mode_list = ', '.join([str(elem) for elem in most_freqs])

		print("\nThere are multiple modes, these are their values: ",mode_list,"\n")
		#Error proofing in case there is no mode e.g same number of multiple values
else: 
        print("\nPlease enter some numbers!\n") #Error proofing to ensure values are entered
