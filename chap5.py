Python 3.4.3 (default, Oct 14 2015, 20:33:09) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> impost os
SyntaxError: invalid syntax
>>> import os
>>> os.getcwd()
'/home/vidhya'
>>> os.chdir("/Documents/work/materials/python/")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.chdir("/Documents/work/materials/python/")
FileNotFoundError: [Errno 2] No such file or directory: '/Documents/work/materials/python/'
>>> os.chdir("/Documents/work/materials/python")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.chdir("/Documents/work/materials/python")
FileNotFoundError: [Errno 2] No such file or directory: '/Documents/work/materials/python'
>>> os.chdir("./Documents/work/materials/python/")
>>> os.getc
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.getc
AttributeError: 'module' object has no attribute 'getc'
>>> os.getcwd()
'/home/vidhya/Documents/work/materials/python'
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		print(james)
		print(julie)
		print(mikey)
		print(sarah)

except: pass

['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']
['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']
['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38']
['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55']
>>> #SORTING
>>> data = [6, 3, 1, 2, 4, 5]
>>> print(data)
[6, 3, 1, 2, 4, 5]
>>> data.sort()
>>> print(data)
[1, 2, 3, 4, 5, 6]
>>> #copied-sorting
>>> data = [6, 3, 1, 2, 4, 5]
>>> sorted(data)
[1, 2, 3, 4, 5, 6]
>>> print(data)
[6, 3, 1, 2, 4, 5]
>>> #copied sorting->original value is untounched.
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		print(sorted(james))
		print(julie)
		print(mikey)
		print(sarah)

except: pass
KeyboardInterrupt
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		print(sorted(james))
		print(sorted(julie))
		print(sorted(mikey))
		print(sorted(sarah))

except: pass

['2-22', '2-34', '2.34', '2.45', '2:01', '2:01', '3.01', '3:10', '3:21']
['2-23', '2.11', '2.59', '2:11', '2:23', '3-10', '3-21', '3.21', '3:10']
['2.49', '2:22', '2:38', '3.01', '3.02', '3.02', '3:01', '3:02', '3:22']
['2-25', '2-55', '2.18', '2.58', '2:39', '2:54', '2:55', '2:55', '2:58']
>>> def sanitize_own(time):
	if "" in time
	
SyntaxError: invalid syntax
>>> def sanitize_own(time):
	if "-" in time:delimiter="-"
	elif ":" in time:delimter=":"
	else: return(time)
	(mins,secs)=time.split(delimiter)
	return(mins+"."+secs)

>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_james=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_james=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_james=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

>>> def sanitize_own(time):
	if "-" in time:delimiter="-"
	elif ":" in time:delimter=":"
	else: return(time)
	(mins,secs)=time.split(delimiter)
	return(mins+"."+secs)
try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

SyntaxError: invalid syntax
>>> 
>>> def sanitize_own(time):
	if "-" in time:delimiter="-"
	elif ":" in time:delimter=":"
	else: return(time)
	(mins,secs)=time.split(delimiter)
	return(mins+"."+secs)
with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))


SyntaxError: invalid syntax
>>> 
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
[DEBUG ON]
>>> def sanitize_own(time):
	if "-" in time:delimiter="-"
	elif ":" in time:delimter=":"
	else: return(time)
	(mins,secs)=time.split(delimiter)
	return(mins+"."+secs)
with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))
		
SyntaxError: invalid syntax
[DEBUG ON]
>>> def sanitize_own(time):
	if "-" in time:delimiter="-"
	elif ":" in time:delimter=":"
	else: return(time)
	(mins,secs)=time.split(delimiter)
	return(mins+"."+secs)
with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in james:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in james:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in james:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))
		
SyntaxError: invalid syntax
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",");
		julie=juf.readline().strip().split(",");
		mikey=mif.readline().strip().split(",");
		sarah=saf.readline().strip().split(",");

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in julie:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in mikey:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in sarah:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in julie:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in mikey:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in sarah:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

>>> 
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in julie:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in mikey:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in sarah:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))
		
SyntaxError: unexpected indent
>>> 
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	sanitized_james=[]
	for each_time in james:
		sanitized_james.append(sanitize_own(each_time))

	sanitized_julie=[]
	for each_time in julie:
		sanitized_julie.append(sanitize_own(each_time))

	sanitized_mikey=[]
	for each_time in mikey:
		sanitized_mikey.append(sanitize_own(each_time))

	sanitized_sarah=[]
	for each_time in sarah:
		sanitized_sarah.append(sanitize_own(each_time))


	print(sorted(sanitized_james))
	print(sorted(sanitized_julie))
	print(sorted(sanitized_mikey))
	print(sorted(sanitized_sarah))

	
Traceback (most recent call last):
  File "<pyshell#65>", line 9, in <module>
    sanitized_james.append(sanitize_own(each_time))
  File "<pyshell#46>", line 5, in sanitize_own
    (mins,secs)=time.split(delimiter)
UnboundLocalError: local variable 'delimiter' referenced before assignment
>>> def sanitize_own(time):
	if "-" in time:
		delimiter="-"
		(mins,secs)=time.split(delimiter)
		return(mins+"."+secs)
	elif ":" in time:
		delimter=":"
		(mins,secs)=time.split(delimiter)
		return(mins+"."+secs)
	else: return(time)

	
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in julie:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in mikey:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in sarah:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	sanitized_james=[]
	for each_time in james:
		sanitized_james.append(sanitize_own(each_time))

	sanitized_julie=[]
	for each_time in julie:
		sanitized_julie.append(sanitize_own(each_time))

	sanitized_mikey=[]
	for each_time in mikey:
		sanitized_mikey.append(sanitize_own(each_time))

	sanitized_sarah=[]
	for each_time in sarah:
		sanitized_sarah.append(sanitize_own(each_time))


	print(sorted(sanitized_james))
	print(sorted(sanitized_julie))
	print(sorted(sanitized_mikey))
	print(sorted(sanitized_sarah))

	
Traceback (most recent call last):
  File "<pyshell#71>", line 9, in <module>
    sanitized_james.append(sanitize_own(each_time))
  File "<pyshell#67>", line 8, in sanitize_own
    (mins,secs)=time.split(delimiter)
UnboundLocalError: local variable 'delimiter' referenced before assignment
>>> def sanitize_own(time):
	if "-" in time:
		(mins,secs)=time.split("-")
		return(mins+"."+secs)
	elif ":" in time:
		(mins,secs)=time.split(":")
		return(mins+"."+secs)
	else: return(time)

	
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	sanitized_james=[]
	for each_time in james:
		sanitized_james.append(sanitize_own(each_time))

	sanitized_julie=[]
	for each_time in julie:
		sanitized_julie.append(sanitize_own(each_time))

	sanitized_mikey=[]
	for each_time in mikey:
		sanitized_mikey.append(sanitize_own(each_time))

	sanitized_sarah=[]
	for each_time in sarah:
		sanitized_sarah.append(sanitize_own(each_time))


	print(sorted(sanitized_james))
	print(sorted(sanitized_julie))
	print(sorted(sanitized_mikey))
	print(sorted(sanitized_sarah))

	
['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		sanitized_james=[]
		for each_time in james:
			sanitized_james.append(sanitize_own(each_time))

		sanitized_julie=[]
		for each_time in julie:
			sanitized_julie.append(sanitize_own(each_time))

		sanitized_mikey=[]
		for each_time in mikey:
			sanitized_mikey.append(sanitize_own(each_time))

		sanitized_sarah=[]
		for each_time in sarah:
			sanitized_sarah.append(sanitize_own(each_time))


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> #list comprehension
>>> mins = [1, 2, 3]
>>> secs=[m*60 for m in mins]
>>> secs
[60, 120, 180]
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		#list comprehension 
		sanitized_james=[sanitize_own(each_time) for each_time in james]
		sanitized_julie=[sanitize_own(each_time) for each_time in julie]
		sanitized_mikey=[sanitize_own(each_time) for each_time in mikey]
		sanitized_sarah=[sanitize_own(each_time) for each_time in sarah]
		


		print(sorted(sanitized_james))
		print(sorted(sanitized_julie))
		print(sorted(sanitized_mikey))
		print(sorted(sanitized_sarah))

except: pass

['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass

['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> # remove duplication and get first three time from the list
>>> def remove_duplicate(time,list):
	if time not in list:
		return(time)

	
>>> def remove_duplicate(time,new_list):
	if time not in new_list:
		return(time)

	
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

                removed_dup_james=[remove_duplicate(each_time,remove_dup_james) fodr each_time in james]
                removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) fodr each_time in julie]
                removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) fodr each_time in mikey]
                removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) fodr each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

                removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
                removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) for each_time in julie]
                removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) for each_time in mikey]
                removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) for each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

                removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
                removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) for each_time in julie]
                removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) for each_time in mikey]
                removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) for each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

                removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
                removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) for each_time in julie]
                removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) for each_time in mikey]
                removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) for each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
		removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) for each_time in julie]
		removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) for each_time in mikey]
		removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) for each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass

>>> 
with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,remove_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,remove_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,remove_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)


Traceback (most recent call last):
  File "<pyshell#102>", line 8, in <module>
    removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
  File "<pyshell#102>", line 8, in <listcomp>
    removed_dup_james=[remove_duplicate(each_time,remove_dup_james) for each_time in james]
NameError: name 'remove_dup_james' is not defined
>>> try:
	with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
		james=jaf.readline().strip().split(",")
		julie=juf.readline().strip().split(",")
		mikey=mif.readline().strip().split(",")
		sarah=saf.readline().strip().split(",")

		removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
		removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
		removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
		removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

		#list comprehension 
		sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
		sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
		sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
		sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
		


		print(sanitized_james)
		print(sanitized_julie)
		print(sanitized_mikey)
		print(sanitized_sarah)


except: pass

>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
Traceback (most recent call last):
  File "<pyshell#106>", line 7, in <module>
    removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
  File "<pyshell#106>", line 7, in <listcomp>
    removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
NameError: name 'removed_dup_james' is not defined
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dupjames=[]
	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
Traceback (most recent call last):
  File "<pyshell#108>", line 8, in <module>
    removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
  File "<pyshell#108>", line 8, in <listcomp>
    removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
NameError: name 'removed_dup_james' is not defined
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=[]
	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
Traceback (most recent call last):
  File "<pyshell#110>", line 9, in <module>
    removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
  File "<pyshell#110>", line 9, in <listcomp>
    removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
NameError: name 'removed_dup_julie' is not defined
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=removed_dup_julie=removed_dup_mikey=removed_dup_sarah=[]
	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=removed_dup_julie=removed_dup_mikey=removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
			
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
			
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)			

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
['2.01', '2.11', '2.11', '2.18', '2.22', '2.22', '2.23', '2.23', '2.25', '2.34', '2.34', '2.38', '2.39', '2.45', '2.49', '2.54', '2.55', '2.55', '2.58', '2.58', '2.59', '3.01', '3.01', '3.02', '3.02', '3.10', '3.10', '3.21', '3.21', '3.21', '3.22']
['2.01', '2.11', '2.11', '2.18', '2.22', '2.22', '2.23', '2.23', '2.25', '2.34', '2.34', '2.38', '2.39', '2.45', '2.49', '2.54', '2.55', '2.55', '2.58', '2.58', '2.59', '3.01', '3.01', '3.02', '3.02', '3.10', '3.10', '3.21', '3.21', '3.21', '3.22']
['2.01', '2.11', '2.11', '2.18', '2.22', '2.22', '2.23', '2.23', '2.25', '2.34', '2.34', '2.38', '2.39', '2.45', '2.49', '2.54', '2.55', '2.55', '2.58', '2.58', '2.59', '3.01', '3.01', '3.02', '3.02', '3.10', '3.10', '3.21', '3.21', '3.21', '3.22']
['2.01', '2.11', '2.11', '2.18', '2.22', '2.22', '2.23', '2.23', '2.25', '2.34', '2.34', '2.38', '2.39', '2.45', '2.49', '2.54', '2.55', '2.55', '2.58', '2.58', '2.59', '3.01', '3.01', '3.02', '3.02', '3.10', '3.10', '3.21', '3.21', '3.21', '3.22']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
			
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
			
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)			

	#list comprehension 
	sanitized_james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	sanitized_julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	sanitized_mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sanitized_sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	


	print(sanitized_james)
	print(sanitized_julie)
	print(sanitized_mikey)
	print(sanitized_sarah)

	
['2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.58', '2.58']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
        removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
        removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
        removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_james[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			print(removed_dup_james[0:3])removed_dup_sarah.append(each_time)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
        removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_julie[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_mikey[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_julie[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_mikey[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)

			
['2.01', '2.22', '2.34']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in removed_dup_james])
	julie=sorted([sanitize_own(each_time) for each_time in removed_dup_julie])
	mikey=sorted([sanitize_own(each_time) for each_time in removed_dup_mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in removed_dup_sarah])
	
	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james)		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_julie[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_mikey[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
	print(removed_dup_sarah[0:3])

	
['2.01', '2.22', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
['2.18', '2.25', '2.39']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

	
	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in james])
	julie=sorted([sanitize_own(each_time) for each_time in julie])
	mikey=sorted([sanitize_own(each_time) for each_time in mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in sarah])
	
	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	removed_dup_james=[remove_duplicate(each_time,removed_dup_james) for each_time in james]
	removed_dup_julie=[remove_duplicate(each_time,removed_dup_julie) for each_time in julie]
	removed_dup_mikey=[remove_duplicate(each_time,removed_dup_mikey) for each_time in mikey]
	removed_dup_sarah=[remove_duplicate(each_time,removed_dup_sarah) for each_time in sarah]

	print(removed_dup_james)
	print(removed_dup_julie)
	print(removed_dup_mikey)
	print(removed_dup_sarah)

	
['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in james])
	julie=sorted([sanitize_own(each_time) for each_time in julie])
	mikey=sorted([sanitize_own(each_time) for each_time in mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in sarah])
	
	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james)		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_julie[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_mikey[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
	print(removed_dup_sarah[0:3])

	
['2.01', '2.22', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
['2.18', '2.25', '2.39']
>>> with open("ch5_data/james.txt")as jaf,open("ch5_data/julie.txt")as juf,open("ch5_data/mikey.txt")as mif,open("ch5_data/sarah.txt")as saf:
	james=jaf.readline().strip().split(",")
	julie=juf.readline().strip().split(",")
	mikey=mif.readline().strip().split(",")
	sarah=saf.readline().strip().split(",")

		

	#list comprehension 
	james=sorted([sanitize_own(each_time) for each_time in james])
	julie=sorted([sanitize_own(each_time) for each_time in julie])
	mikey=sorted([sanitize_own(each_time) for each_time in mikey])
	sarah=sorted([sanitize_own(each_time) for each_time in sarah])
	
	removed_dup_james=[]
	removed_dup_julie=[]
	removed_dup_mikey=[]
	removed_dup_sarah=[]
	for each_time in james:
		if each_time not in removed_dup_james:
			removed_dup_james.append(each_time)
	print(removed_dup_james[0:3])		
			
	for each_time in julie:
		if each_time not in removed_dup_julie:
			removed_dup_julie.append(each_time)
	print(removed_dup_julie[0:3])		
	for each_time in mikey:
		if each_time not in removed_dup_mikey:
			removed_dup_mikey.append(each_time)
	print(removed_dup_mikey[0:3])		
	for each_time in sarah:
		if each_time not in removed_dup_sarah:
			removed_dup_sarah.append(each_time)
	print(removed_dup_sarah[0:3])

	
['2.01', '2.22', '2.34']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
['2.18', '2.25', '2.39']
>>> def print():
	print("my new customised print function")

	
>>> print()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print()
  File "<pyshell#137>", line 2, in print
    print("my new customised print function")
TypeError: print() takes 0 positional arguments but 1 was given
>>> print("something")
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    print("something")
TypeError: print() takes 0 positional arguments but 1 was given
>>> from __future__ import print_function
>>> print()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    print()
  File "<pyshell#137>", line 2, in print
    print("my new customised print function")
TypeError: print() takes 0 positional arguments but 1 was given
>>> 

