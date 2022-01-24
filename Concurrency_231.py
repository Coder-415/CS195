#Task - Write a program that creates a pool of workers to all at once check 
#whether or not the files whose pathnames are passed in are encoded in UTF-8

#Key Terms: Threading; Multiprocess; Futures
#-------------------------------------------------------------------------
#------------------------------------------------------------------------


#Importing relevant modules

import sys
import os
from concurrent.futures import ThreadPoolExecutor
import codecs


#Allowing for both user input and a back up 

try:
	f = sys.argv[1]
except IndexError:
	f = '/users/abrick/resources'
	print("\nplease try entering a valid file or directory path\n")


#Defining Pool

pool = ThreadPoolExecutor(max_workers=3)


#Function will try to open file if inidiviudal file or will otherwise use 
#'os.walk' for directory

def try_utf8(data):
	try:
		try: 

#Using codecs.open to encode file using 'utf-8' and enforcing strict errors 

			codecs.open(data,encoding = 'utf-8',errors="strict").readlines()
			print(data,"\033[1m" + "\033[92m" + "valid utf-8" + "\033[0m")
		except UnicodeDecodeError:
			print(data,"\033[1m" + "\033[91m" + "not valid utf-8" + "\033[0m")
		except PermissionError:
			print(data,"\033[4m" + "unable to access" + "\033[0m")
	except: 

#Using os.walk to generate files names if directory provided 

		for subdir,dirs,files in os.walk(data):
			for filename in files:	

#Defining filepath to provide file path name including subdirectory and file 
#name while separating pathname components 

				filepath = subdir + os.sep + filename
				try:
					codecs.open(filepath,encoding = 'utf-8',errors="strict").readlines()
					print(filepath,"\033[1m" + "\033[92m" + "valid utf-8" + "\033[0m")
				except UnicodeDecodeError:
					print(filepath,"\033[1m" + "\033[91m" + "not valid utf-8" + "\033[0m")
				except PermissionError:
					print(filepath,"\033[4m" + "unable to access" + "\033[0m")


#Calling pool to action  

pool.submit(try_utf8(f))
