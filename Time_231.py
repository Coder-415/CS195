
#Demonstrate the use of a generator that indicates for each event in access_log the number of seconds elapsed since the most recent midnight

from datetime import datetime

#timestamp = (line[:line.find(']')+1] for line in open('/etc/httpd/logs/access_log'))

#timestamp  = (line.split(" ")[3:5] for line in open('/etc/httpd/logs/access_log'))

#format_time = "%d/%m/%y %H:%M:%S.%f"

#time_object = datetime.strptime(timestamp,format_time)

#midnight = datetime (hour=0)


#for times in open('/etc/httpd/logs/access_log'):
#	try: 
#		datetime.strptime(elements, "%d/%b/%Y:%H:%M:%S %z")
#		timestamp = times 
#	except (ValueError, TypeError):
#		pass

#timestamp =[]

#def find_times():
#	for times in open('/etc/httpd/logs/access_log'):
#		try:
#			datetime.strptime(times, "%d/%b/%Y:%H:%M:%S %z")
#			global timestamp
#			timestamp = times
#		except (ValueError, TypeError):
#			pass

#find_times()

#def time_since_midnight():
	#for times in open('/etc/httpd/logs/access_log'):
        	#try:
                	#datetime.strptime(times, "%d/%b/%Y:%H:%M:%S %z")
                	#timestamp = times 
        	#except (ValueError, TypeError):
                	#pass
#	delta1 = timestamp - datetime.time(hour = 0, minute = 0, second = 0)
	
	#for times in timestamp:
	#timestamp = (line.split(" ")[3:5] for line in open('/etc/httpd/logs/access_log')) - datetime.time.min
	#yield timestamp - datetime.time.min
	#delta1 = timestamp-datetime.time.min
	#yield delta1


open('/etc/httpd/logs/access_log',"r") 

#def get_times():
	#for times in open('/etc/httpd/logs/access_log',"r"):
	#	try: 
	#		yield datetime.strptime(times,"%d/%b/%Y:%H:%M:%S %z")
	#	except (ValueError, TypeError):
	#		pass
	#	global time1
	#	time1 = times

#from dateutil.parser import parse


#f = (line.split(" ")[3] for line in open('/etc/httpd/logs/access_log'))

def time_since_midnight():
	f = (line.split(" ")[3] for line in open('/etc/httpd/logs/access_log'))
	midnight = datetime.min
	#time_stamp = yield datetime.strptime('/etc/httpd/logs/access_log',"%d/%b/%Y %H:%M:%S %z")              
	time_stamp = []
	for lines in f:
#open('/etc/httpd/logs/access_log'):
		try: 
			time_stamp = datetime.strptime(f,"%H:%M:%S")
			#print (time_stamp)
			#time_stamp = parse()	
			#global delta1
			#delta1 = time_stamp - midnight
			#print((time_stamp-midnight).seconds,"elapsed")
		except (ValueError, TypeError):
			pass
		#delta1 = time_stamp-midnight
		#print((delta1).seconds,"elapsed")
		#yield ((time_stamp-midnight).seconds,"seconds elapsed")
		#print (time_stamp)
			
#time_since_midnight()

#print ("Tried working on this for close to five hours and kept running into errors. Looking forward to reading feedback and seeing other people's examples.Sorry for the clutter.")

print ([next(time_since_midnight()) for _ in range (1)])

#  * I can tell you worked really hard on this and you were very close!
#  You can add f as a parameter in your time_since_midnight definition. The
#  way you split your lines in f = (line.split...) actually splits each
#  line into two separate components: the timestamp and timezone. So,
#  replace [3:5] with just [3]. Since you're splitting on the space, delete
#  the first bracket in the string. That should format the timestamp
#  correctly in order to try: time_stamp = datetime.strptime(f,"%H:%M:%S").
#  Good job!
