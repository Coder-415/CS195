#Name:Alexei Schnakenburg
#Class: CS 231

#Task - Write a program that expects as argument the path to a greyscale ASCII
#PGM file, and prints out a sixteen-bucket histogram counting the pixles at 
#each level of grey, i.e., indicate the dimensions of any PGM files whose
#pathnames are passed as arguments. 
#----------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Importing Modules
import sys
import re
import math

#Error proofing using sample and try 
Sample = '/users/abrick/resources/maquinna.pgm'

try:
 f1 = sys.argv[1]
except (IndexError,ValueError,FileNotFoundError):
 f1 = Sample
 print("Please try again with a valid pgm file")

#Using provided info for parsing .pgm files
with open(f1) as content:
 parts = re.split(r'\s+',re.sub(r'#.*',r'\n',content.read()))
 x_dim, y_dim, depth = int(parts[1]),int(parts[2]),int(parts[3])
 pixles = [int(n) for n in parts[4:] if n]
 assert len (pixles) == x_dim * y_dim

#Defining Terms
Range = int((max(pixles))-(min(pixles)))     	
Interval_Num = int(16)
#Using math modules to round up as opposed to float
Interval_Width = int(math.ceil(Range/Interval_Num))

#Providing Information
print("There are this many pixle values:","{:,}".format(len(pixles)))
print("The highest value pixle is:",max(pixles))
print("The lowest value pixle is:",min(pixles))
print("The range of pixle values is:",Range)
print("The width of interval class is:",Interval_Width)

#Using dictionary comprehension to create 16 buckets
obj = {str(Interval_Width*i-Interval_Width)+':'+str(Interval_Width*i):[] for i in list (range(1,Interval_Num+1))}

#Populating buckets using if statements (likely to be easier way)
for pixle in pixles:
 if pixle in range (0,Interval_Width):
  obj['0:16'].append(pixle)
 elif Interval_Width>pixle<Interval_Width*2:
  obj['16:32'].append(pixle)
 elif Interval_Width*2>pixle<Interval_Width*3:       	     
  obj['32:48'].append(pixle)
 elif Interval_Width*3>pixle<Interval_Width*4:       	     
  obj['48:64'].append(pixle)
 elif Interval_Width*4>pixle<Interval_Width*5:       	     
  obj['64:80'].append(pixle)
 elif Interval_Width*5>pixle<Interval_Width*6:       	     
  obj['80:96'].append(pixle)
 elif Interval_Width*6>pixle<Interval_Width*7:       	     
  obj['96:112'].append(pixle)
 elif Interval_Width*7>pixle<Interval_Width*8:       	     
  obj['112:128'].append(pixle)
 elif Interval_Width*8>pixle<Interval_Width*9:       	     
  obj['128:144'].append(pixle)
 elif Interval_Width*9>pixle<Interval_Width*10:       	     
  obj['144:160'].append(pixle)
 elif Interval_Width*10>pixle<Interval_Width*11:       	     
  obj['160:176'].append(pixle)
 elif Interval_Width*11>pixle<Interval_Width*12:       	     
  obj['176:192'].append(pixle)
 elif Interval_Width*12>pixle<Interval_Width*13:       	     
  obj['192:208'].append(pixle)
 elif Interval_Width*13>pixle<Interval_Width*14:       	     
  obj['208:224'].append(pixle)
 elif Interval_Width*14>pixle<Interval_Width*15:       	     
  obj['224:240'].append(pixle)
 elif Interval_Width*15>pixle<=Interval_Width*16:       	     
  obj['240:256'].append(pixle)

#Creating empty list
G1b = []

#Populating list with length of each bucket 
for list in obj:
 G1b.append(len(obj[list])) 

#Placeholder
IW = 0

#Using for loop and unicode to create histogram
for values in G1b:
 print (u'\u2B1B' * (int(values/1500)),"{:<5,}".format(values),'[',Interval_Width*IW,':',Interval_Width+(Interval_Width*IW),']',sep='') 
 IW += 1
