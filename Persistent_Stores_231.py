#Name: Alexei Schnakenburg
#Due Date: 11/22/2020
#Class: Compi Sci 231 

#Assignment: write a CSV-to-JSON translator that expects a path to a CSV file 
#as an argument and for each line prints out a JSON object encapsulating that 
#record. 

#------------------------------------------------------------------------------
#-----------------------------------------------------------------------------

#importing modules
import json 
import csv
import sys
import os.path

#defining test
test = '/users/abrick/resources/ew.csv'

#creating test function
def test_run():

#opening and displaying csv

	with open(test,'r') as f1:	
		print("Below is the content of the original csv:\n\n",f1.read(),sep='')
	with open(test,'r') as csvFile1:
                
#opening and csv reading csv

		result1 = csv.reader(csvFile1)

#writing csv file to json file line by line

		with open('json_results','w') as jsonFile1:
                        for lines in result1:
                                json.dump(lines,jsonFile1,indent=2)
	print("Here is the line by line JSON encapsulation: \n")
	with open('json_results','r') as output:
		print(output.read())
	print("\nThe above is a sample result.Please try again with a valid \
CSV path. For example,'",test,"'.Thank you.\n",sep='')

try:

#providing for cmd line arguments

	s = sys.argv[1]

#ensuring extensions provided are .csv

	if os.path.splitext(s)[1] != '.csv':
		test_run()
		print ("The file provided does not have a .csv extension.\n")	
		sys.exit()
	with open (s,'r') as f:
                print("Below is the content of the original csv:\n\n",f.read(),sep='')
	with open (s,'r') as csvFile:
		result = csv.reader(csvFile)
		with open('json_results','w') as jsonFile:
			for lines in result:
				json.dump(lines,jsonFile,indent=2)
	print("Here is the line by line	JSON encapsulation: \n")
	with open('json_results','r') as output:
		print (output.read())
except (IndexError,FileNotFoundError,IsADirectoryError,SyntaxError):
	test_run()

#Kept running into error regarding reader and dict reader not being 
#Json serializable. Any advice?

