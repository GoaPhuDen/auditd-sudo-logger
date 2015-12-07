#!/usr/bin/python

import re
import time


def convertTime(input_time):
	just_time = float(input_time[input_time.find("(")+1:input_time.find(".")])
	converted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(just_time))
	return converted

def user(auid):
	auid = auid[auid.find("=")+1:]
	if auid == '1000':
		return "Travis"
	else:
		return "Unknown user"

def command(input):
	command = input[input.find('"')+1:-1]
	return command

test_string = 'type=SYSCALL msg=audit(1445222463.561:74670): arch=c000003e syscall=59 success=yes exit=0 a0=cbed68 a1=cc3ac8 a2=ca9008 a3=7ffe25bc6f20 items=2 ppid=11508 pid=11659 auid=1000 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0 ses=26 comm="vi" exe="/usr/bin/vim.basic" key=(null)'


items = re.split(" ", test_string)

#Converts epoch time into a human readable format
converted_time = convertTime(items[1])
print converted_time

#finds user ID, compares to list
user_id = user(items[13])
print user_id

#displays command used
print items[24]
command_short = command(items[24])
print command_short

#Displays command path
print items[25]
command_path = command(items[25])
print command_path


print "%s | User: %s | Command: %s | Path: %s" %  (converted_time, user_id, command_short, command_path)
