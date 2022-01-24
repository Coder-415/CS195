#Name: Alexei Schnakenburg
#Class: CS 231 
#Date: 12/6/2020

#Assignment: Write a program that outputs a PGM file that smoothly fades from
#white at the left to black at the right.
#-----------------------------------------------------------------------------

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
obj = {str(Interval_Width*i-Interval_Width)+':'+str(Interval_Width*i):[] for i \
in list (range(1,Interval_Num+1))}

#Populating buckets using if statements (likely to be easier way)
def bucket():
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
G1b =[]

bucket()

#Populating list with length of each bucket 
for list in obj:
  G1b.append(len(obj[list]))

#Placeholder
IW = 0

#Using for loop and unicode to create histogram
for values in G1b:
 print (u'\u2B1B' * (int(values/1500)),"{:<5,}".format(values),'['\
,Interval_Width*IW,':',Interval_Width+(Interval_Width*IW),']',sep='') 
 IW += 1 

#Offered user input but not allowed by course policy
#k = float(input("\nWhat direction do you want to shift the histogram?: \n"))

k = 6.4

print("\nThe histogram values have been shifted by ",k," and the new \
histogram values have been saved as'Translation_231.pgm'. Please see the \
updated histogram below.\n",sep= '')


#Saving .pgm with shifted histogram
with open('Translation_231.pgm','w') as T1:
 pixl = []
 for items in pixles:
  pixl.append(items + k)
 T1.write(str(pixl))

#Know there's a better way but rebucketed modified values
def bucket_1():
 for pixle in pixl:
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


#opening modified histogram
with open('Translation_231.pgm','rb') as T1a:
 
#clearing list and dictionary (but keeping keys)
 G1b.clear()
 for value in obj.values():
  del value[:]

 bucket_1()
 for list in obj:
  G1b.append(len(obj[list]))
 IW = 0
 for values in G1b:
  print (u'\u2B1B' * (int(values/1500)),"{:<5,}".format(values),'['\
,Interval_Width*IW,':',Interval_Width+(Interval_Width*IW),']',sep='')
  IW += 1
