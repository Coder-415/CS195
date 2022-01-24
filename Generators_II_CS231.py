#Write a program that demonstrates a generator yielding one timestamp at a time from /etc/httpd/logs/access_log & peer review due 9/13.


time_stamp = (line.split(" ")[3] for line in open("/etc/httpd/logs/access_log"))

print ([next(time_stamp) for i in range (1)])


