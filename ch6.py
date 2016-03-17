Python 3.4.3 (default, Oct 14 2015, 20:33:09) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> class Athlete:
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.times=times

		
>>> sarah=Athlete()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sarah=Athlete()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> sarah=Athelete("sarah","2002-6-17",["2:58","1.56"])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sarah=Athelete("sarah","2002-6-17",["2:58","1.56"])
NameError: name 'Athelete' is not defined
>>> sarah=Athlete("sarah","2002-6-17",["2:58","1.56"])
>>> james=Athlete("james")
>>> type(sarah)
<class '__main__.Athlete'>
>>> type(james)
<class '__main__.Athlete'>
>>> sarah
<__main__.Athlete object at 0xb53ddd2c>
>>> james
<__main__.Athlete object at 0xb53dddac>
>>> james.dob
>>> sarah.dob
'2002-6-17'
>>> james.times
[]
>>> #first method
>>> def sanitize_own(time):
	if "-" in time:
		(mins,secs)=time.split("-")
		return(mins+"."+secs)
	elif ":" in time:
		(mins,secs)=time.split(":")
		return(mins+"."+secs)
	else: return(time)

>>> class Athlete:
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.times=times
	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times ]))[0:3])

	
>>> import os
>>> os.chdir("./Documents/work/materials/python/")
>>> os.getcwd()
'/home/vidhya/Documents/work/materials/python'
>>> def get_coach_data(filename):
	try:
		with open(filename)as f :
			data=f.readline()
		temp=data.strip.split(",")
		retrun(Athelte(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print(str(ioerr))
		return(None)

	
>>> james=get_coach_data("ch6_data/sarah2.txt")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    james=get_coach_data("ch6_data/sarah2.txt")
  File "<pyshell#35>", line 5, in get_coach_data
    temp=data.strip.split(",")
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> def get_coach_data(filename):
	try:
		with open(filename)as f :
			data=f.readline()
		temp=data.strip.split(",")
		return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print(str(ioerr))
		return(None)

	
>>> james=get_coach_data("ch6_data/sarah2.txt")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    james=get_coach_data("ch6_data/sarah2.txt")
  File "<pyshell#39>", line 5, in get_coach_data
    temp=data.strip.split(",")
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> def get_coach_data(filename):
	try:
		with open(filename)as f :
			data=f.readline()
		temp=data.strip().split(",")
		return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print(str(ioerr))
		return(None)

	
>>> james=get_coach_data("ch6_data/sarah2.txt")
>>> print(james.name)
Sarah Sweeney
>>> print(james.times)
['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55', '2:22', '2-21', '2.22']
>>> print(james.top3())
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(james.top3())
  File "<pyshell#22>", line 7, in top3
    return(sorted(set([sanitize(t) for t in self.times ]))[0:3])
  File "<pyshell#22>", line 7, in <listcomp>
    return(sorted(set([sanitize(t) for t in self.times ]))[0:3])
NameError: name 'sanitize' is not defined
>>> class Athlete:
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.times=times
	def top3(self):
		return(sorted(set([sanitize_own(t) for t in self.times ]))[0:3])

	
>>> print(james.top3())
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(james.top3())
  File "<pyshell#22>", line 7, in top3
    return(sorted(set([sanitize(t) for t in self.times ]))[0:3])
  File "<pyshell#22>", line 7, in <listcomp>
    return(sorted(set([sanitize(t) for t in self.times ]))[0:3])
NameError: name 'sanitize' is not defined
>>> james=get_coach_data("ch6_data/sarah2.txt")
>>> print(james.top3())
['2.18', '2.21', '2.22']
>>> class Athlete:
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.times=times
	def top3(self):
		return(sorted(set([sanitize_own(t) for t in self.times ]))[0:3])

	
>>> class Athlete:
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.times=times
	def top3(self):
		return(sorted(set([sanitize_own(t) for t in self.times ]))[0:3])
	def add_time(self,time):
		self.times.append(time)
	def add_list_times(self,time):
		self.times.extend(time)

		
>>> attach=Athlete("newname")
>>> attach.add_time("1.31")
>>> print(attach.top3())
['1.31']
>>> attach.add_times(["22","2.2"])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    attach.add_times(["22","2.2"])
AttributeError: 'Athlete' object has no attribute 'add_times'
>>> attach.add_list_times(["22","2.2"])
>>> print(attach.top3())
['1.31', '2.2', '22']
>>> class OwnList(list):
	def __init__(self,name):
		self.name=name

		
>>> jon=OwnList("vidhya")
\
>>> jon=OwnList("vidhya")
>>> type(jon)
<class '__main__.OwnList'>
>>> dir(jon)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'name', 'pop', 'remove', 'reverse', 'sort']
>>> class OwnList(list):
	def ownMethod(self,name):
		self.name=name

		
>>> jon=OwnList()
>>> type(jon)
<class '__main__.OwnList'>
>>> jon.ownMethod("vidhya")
>>> jon.name
'vidhya'
>>> class OwnList(list):
	def ownMethod2(self,name):
		self.name=name

		
>>> jon=OwnList()
>>> type(jon)
<class '__main__.OwnList'>
>>> jon.name
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    jon.name
AttributeError: 'OwnList' object has no attribute 'name'
>>> class AthleteList(list):
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.extend(times)
	def top3(self):
		return(sorted(set([sanitize_own(t) for t in self ]))[0:3])

	
>>> def get_coach_data(filename):
	try:
		with open(filename)as f :
			data=f.readline()
		temp=data.strip.split(",")
		return(AthleteList(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print(str(ioerr))
		return(None)

	
>>> james=get_coach_data("ch6_data/james2.txt")
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    james=get_coach_data("ch6_data/james2.txt")
  File "<pyshell#89>", line 5, in get_coach_data
    temp=data.strip.split(",")
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> def get_coach_data(filename):
	try:
		with open(filename)as f :
			data=f.readline()
		temp=data.strip().split(",")
		return(AthleteList(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print(str(ioerr))
		return(None)

	
>>> james=get_coach_data("ch6_data/james2.txt")
>>> print(james.times)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(james.times)
AttributeError: 'AthleteList' object has no attribute 'times'
>>> print(james.dob)
2002-3-14
>>> james.name
'James Lee'
>>> 
