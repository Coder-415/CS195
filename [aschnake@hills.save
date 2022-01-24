#Implement two algorithms which demonstrably reach the same conclusion and use profile or cProfile to time them both


#import modules

import cProfile
import time, random
from time import perf_counter


#simple while loop slowly addes to produce value of 10,000,000

def slow():
	x = 0
	while x < 10000000:
		x += 1.0 

#demonstrating that both have the same value and object type

	print ("The product of slow() is: ",'{:,}'.format(x))
	print(type(x))


#getting much faster result using a for loop 

def pythonic():
	y = 0
	for i in range(10000000):
		y += 1.0

#demonstrating that both functions produce same result and object type

	print("The product of pythonic() is: ",'{:,}'.format(y))
	print (type(y))


#Calling each function with cProfile

cProfile.run('slow()')
cProfile.run('pythonic()')

# Question - Tried using __name__=='__main__' to run both functions with same cProfile but ran into difficulties. Any guidance? 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Alternative way to is to use perf_counter but was not the assignment

#start1 = time.perf_counter()
#slow()
#elapsed1 = time.perf_counter() - start1
#print("The time elapsed to produce slow() was:",elapsed1,"seconds")

#start2=time.perf_counter()
#pythonic()
#elapsed2 = time.perf_counter() - start2
#print("The time elapsed to produce pythonic() was:", elapsed2,"seconds")

#Tells which is faster which is one advantage. Not sure how to compare function call times yet between two cProfile calls. Any tips?

#def fastest():
#	if elapsed2 < elapsed1: 
#		print("pythonic() is faster")
#	elif  elapsed1 <  elapsed2:
#		print ("slow() is faster")
#	else:
#		print("Neither is faster")

#fastest()
