# Decorate print() such that (A) it refuses to print anything under ten characters long and (B) only five calls are allowed, and 
# demonstrate these restrictions when the program is run

# Grade - 0/100 (Review notes on the bottom)

# '*' works with lists/tuples and sends as positional arguments
#* = unpacks values in specified list as positional arguments and passes them through the function. Cannot raise more or fewer(unless separate provided) arguments than function.  
#*args = receives a tuple containing the positional arugments beyond the formal paramter list (any number of arguments), i.e., beyond specified positional arguments.
#	Being a tuple, *args are iterable and can accept inbuilt functions, e.g., "sum". May need to be unpacked using '*' to work with. 

# '**' works with dictionaries and sends as keyword arguments
#** = unpacks a dictionary and passes its items as keyword arguments to the function. Cannot raise more or fewer (unless separate provided) arguments than function.
#**kwargs = receives a dictionary and unpacks all key word arguments starting after the formal parameter list.
#	Cannot pass a dictionary as a positional argument to **kawargs without unpacking the dictionary and passing the items in dictionary as keyword argument 



#This function decorates items pased in and prints them out but refuses to print anything under ten characters long and only allows for five calls.
#I opted for a more flexible approach that would not lead to Type errors if more or fewer than five inputs were given while only printing the first five


#Added the ability for the user to add command line arguments 
import sys
C_line = (sys.argv[1:])


#function allows user to enter as many arguments as he/she likes but will only produce result for first five calls 
def limited_print(*args):
	for values in args[0:5]:
		if len(str(values)) >= 10:
			print(values) 
		else:
			print("-"*50)

#Defaults to no command line arguments while allowing for command line argument. Uses '*' to call command line, if values entered. 
if not C_line:
	print ("\n", "These are the values with more ten characters or more:","\n")
	limited_print(434,343,343,3434.4343434343,'will not print items with less than ten characters')
	print("\n","You can also try using command line arguments","\n")
else: 
	print ("\n", "These are the values with more ten characters or more:","\n")
	limited_print(*C_line)
	

# A decorator is just an add-on to a function without changing its
# functionality - that concept has been misunderstood here. This program
# just created a function using print (no decoration at all) to mimic the
# results for the assignment's requirements.
# 
# E.g. @classmethoc, @accepts(int,int), @returns(float)
# In addition to other functionalities, decorates are a cleaner way to use builtins 
# This includes defining a function, defining a class, add attributes to a function,
# enforce function arguments and return types, and declaring a class implements a particular,
# set of of interface(s).
