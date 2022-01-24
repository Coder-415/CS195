#Write a universal launcher program that expects its command line arguments
#to contain the absolute path to a program in any language, followed by its 
#arguments. The wrapper should transparently run that program and exit with
#its exit value.

#Notes:
#Internals of Python Lnaguage
#Source vs Byte Code

#Byte code = language which is a portion of CPython program. Can be inspected
#which is useful for debugging. Stored only in memory or cached in a .pyc
#file. Created everytime you run a python code.

#CPython program = Interpretor & Execution platform of Python. Complies source
#code in just-in-time manner and executes/implements it.

#Global Interpretor Lock (GIL) ensures only one threads runs at one time but 
#limits thread performance. 

#Key terms: CPython dis GIL
#Key functions: compile(); eval();exec(); __cached__; dis(disassembler);
#subprocess.run()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

#assignment - write a python program that runs a program from the terminal/
#command line. No need to use dis in the homework. Focus on subprocess. 


#importing modules for subprocesses and cmd line input
import subprocess 
import sys


#defining s as cmd line input 
s = sys.argv[1:]


#Base cmd line argument receiver 
try: 

#Defining subprocess.run and instructing standard output to be piped
#and decoded. Honestly, I think you can just run the subprocess without 
#defining or printing and decoding it but adding it because it is relevant
#given recent content in the course. 
	p1 = subprocess.run(s,stdout=subprocess.PIPE)
	print(p1.stdout.decode())

#Providing path and argument(s) given
	print ("Path given: ",p1.args[0])
	print ("Argument(s) given: ",p1.args[1:],"\n")

#Using .returncode to pint the error code and specify if errors found
	if p1.returncode == 0:
		print("There are no errors, here is the return code: ", \
p1.returncode,"\n")
	elif p1.returncode != 0:
		print("There are errors, please see error note above. Here \
is the return code: ",p1.returncode,"\n")

#Using std.err to print error type if detected 	
	if p1.stderr == None:
		pass
	elif p1.stderr != None:
		print(p1.stderr)


#This allows for a sample process to run if no cmd line arguments entered 
except IndexError:
	p2 = subprocess.run(['/usr/bin/ls','-l'],stdout=subprocess.PIPE)
	print(p2.stdout.decode())
	print("Sample path: ",p2.args[0])
	print("Sample argument: ",p2.args[1:],"\n")
	if p2.returncode == 0:
		print("There are no errors, here is the return code: ", \
p2.returncode)
	elif p2.returncode !=0:
		print("There are are errors, please see error note above. \
Here is the return code: ", p2.returncode)
	if p2.stderr == None:
		pass
	elif p2.stderr != None:
		print(p2.stderr)
	print ("\nPlease try again by entering a command line argument, e.g.,\
'/usr/bin/ls -l'.\n")
	print ("Above is a sample result using 'ls' in long listing format.\n")


#Printing cleaner note if invalid file submitted 
except FileNotFoundError:
	print("\nPlease try again with a valid path. File not found.\n")
