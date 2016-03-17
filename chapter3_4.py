Python 3.4.3 (default, Oct 14 2015, 20:33:09) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/home/vidhya'
>>> os.chdir("/Documents/work/materials/python/modules")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.chdir("/Documents/work/materials/python/modules")
FileNotFoundError: [Errno 2] No such file or directory: '/Documents/work/materials/python/modules'
>>> os.chdir("./Documents/work/materials/python/modules")
>>> os.getcwd()
'/home/vidhya/Documents/work/materials/python/modules'
>>> data=open("sketch.txt")
>>> print(data.readline())
Man: Is this the right room for an argument?

>>> print(data.readline())
Other Man: I've told you once.

>>> p
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> print(data.readline())
Man: No you haven't!

>>> data.seek(0)
0
>>> data.seek(2)
2
>>> 
>>> data.tell(2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.tell(2)
TypeError: tell() takes no arguments (1 given)
>>> data.tell()
2
>>> data.seek(0)
0
>>> data.tell()
0
>>> for each_data in data:
	print(each_data,end="")

	
Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!
Other Man: I'm telling you, I did!
Man: You did not!
Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?
Man: Ah! (taking out his wallet and paying) Just the five minutes.
Other Man: Just the five minutes. Thank you.
Other Man: Anyway, I did.
Man: You most certainly did not!
Other Man: Now let's get one thing quite clear: I most definitely told you!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh look, this isn't an argument!
(pause)
Other Man: Yes it is!
Man: No it isn't!
(pause)
Man: It's just contradiction!
Other Man: No it isn't!
Man: It IS!
Other Man: It is NOT!
Man: You just contradicted me!
Other Man: No I didn't!
Man: You DID!
Other Man: No no no!
Man: You did just then!
Other Man: Nonsense!
Man: (exasperated) Oh, this is futile!!
(pause)
Other Man: No it isn't!
Man: Yes it is!
>>> for each_data in data:
	print(each_data)

	
>>> 
>>> data.seek(0)
0
>>> for each_data in data:
	print(each_data)

	
Man: Is this the right room for an argument?

Other Man: I've told you once.

Man: No you haven't!

Other Man: Yes I have.

Man: When?

Other Man: Just now.

Man: No you didn't!

Other Man: Yes I did!

Man: You didn't!

Other Man: I'm telling you, I did!

Man: You did not!

Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?

Man: Ah! (taking out his wallet and paying) Just the five minutes.

Other Man: Just the five minutes. Thank you.

Other Man: Anyway, I did.

Man: You most certainly did not!

Other Man: Now let's get one thing quite clear: I most definitely told you!

Man: Oh no you didn't!

Other Man: Oh yes I did!

Man: Oh no you didn't!

Other Man: Oh yes I did!

Man: Oh look, this isn't an argument!

(pause)

Other Man: Yes it is!

Man: No it isn't!

(pause)

Man: It's just contradiction!

Other Man: No it isn't!

Man: It IS!

Other Man: It is NOT!

Man: You just contradicted me!

Other Man: No I didn't!

Man: You DID!

Other Man: No no no!

Man: You did just then!

Other Man: Nonsense!

Man: (exasperated) Oh, this is futile!!

(pause)

Other Man: No it isn't!

Man: Yes it is!

>>> data.tell()
1092
>>> for each_data in data:
	print(each_data,end="")

	
>>> data.seek(0)
0
>>> for each_data in data:
	print(each_data,end="")

	
Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!
Other Man: I'm telling you, I did!
Man: You did not!
Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?
Man: Ah! (taking out his wallet and paying) Just the five minutes.
Other Man: Just the five minutes. Thank you.
Other Man: Anyway, I did.
Man: You most certainly did not!
Other Man: Now let's get one thing quite clear: I most definitely told you!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh look, this isn't an argument!
(pause)
Other Man: Yes it is!
Man: No it isn't!
(pause)
Man: It's just contradiction!
Other Man: No it isn't!
Man: It IS!
Other Man: It is NOT!
Man: You just contradicted me!
Other Man: No I didn't!
Man: You DID!
Other Man: No no no!
Man: You did just then!
Other Man: Nonsense!
Man: (exasperated) Oh, this is futile!!
(pause)
Other Man: No it isn't!
Man: Yes it is!
>>> data.tell()
1092
>>> for each_data in data:
	print(each_data,end="")

	
>>> data.close()
>>> for each_data in data:
	print(each_data,end="")

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for each_data in data:
ValueError: I/O operation on closed file.
>>> data.open()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> help(split)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    help(split)
NameError: name 'split' is not defined
>>> help(split())
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    help(split())
NameError: name 'split' is not defined
>>> help(each_line.split)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    help(each_line.split)
NameError: name 'each_line' is not defined
>>> data=open("sketch.txt")
>>> for each_data in data:
	(person,line_said)=each_data.split(":")
	print(person,end=" ")
	print(line_said,end="")

	
Man  Is this the right room for an argument?
Other Man  I've told you once.
Man  No you haven't!
Other Man  Yes I have.
Man  When?
Other Man  Just now.
Man  No you didn't!
Other Man  Yes I did!
Man  You didn't!
Other Man  I'm telling you, I did!
Man  You did not!
Other Man  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man  Just the five minutes. Thank you.
Other Man  Anyway, I did.
Man  You most certainly did not!
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    (person,line_said)=each_data.split(":")
ValueError: too many values to unpack (expected 2)
>>> for each_data in data:
	person=each_data.split(":")
	print(person,end=" ")
	print(line_said,end="")

	
['Man', " Oh no you didn't!\n"]  You most certainly did not!
['Other Man', ' Oh yes I did!\n']  You most certainly did not!
['Man', " Oh no you didn't!\n"]  You most certainly did not!
['Other Man', ' Oh yes I did!\n']  You most certainly did not!
['Man', " Oh look, this isn't an argument!\n"]  You most certainly did not!
['(pause)\n']  You most certainly did not!
['Other Man', ' Yes it is!\n']  You most certainly did not!
['Man', " No it isn't!\n"]  You most certainly did not!
['(pause)\n']  You most certainly did not!
['Man', " It's just contradiction!\n"]  You most certainly did not!
['Other Man', " No it isn't!\n"]  You most certainly did not!
['Man', ' It IS!\n']  You most certainly did not!
['Other Man', ' It is NOT!\n']  You most certainly did not!
['Man', ' You just contradicted me!\n']  You most certainly did not!
['Other Man', " No I didn't!\n"]  You most certainly did not!
['Man', ' You DID!\n']  You most certainly did not!
['Other Man', ' No no no!\n']  You most certainly did not!
['Man', ' You did just then!\n']  You most certainly did not!
['Other Man', ' Nonsense!\n']  You most certainly did not!
['Man', ' (exasperated) Oh, this is futile!!\n']  You most certainly did not!
['(pause)\n']  You most certainly did not!
['Other Man', " No it isn't!\n"]  You most certainly did not!
['Man', ' Yes it is!\n']  You most certainly did not!
>>> help(each_data.split)
Help on built-in function split:

split(...) method of builtins.str instance
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

>>> for each_data in data:
	person=each_data.split(":",1)
	print(person,end=" ")
	print(line_said,end="")

	
>>> data.seek(0)
0
>>> for each_data in data:
	(person,line_said)=each_data.split(":",1)
	print(person,end=" ")
	print(line_said,end="")

	
Man  Is this the right room for an argument?
Other Man  I've told you once.
Man  No you haven't!
Other Man  Yes I have.
Man  When?
Other Man  Just now.
Man  No you didn't!
Other Man  Yes I did!
Man  You didn't!
Other Man  I'm telling you, I did!
Man  You did not!
Other Man  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man  Just the five minutes. Thank you.
Other Man  Anyway, I did.
Man  You most certainly did not!
Other Man  Now let's get one thing quite clear: I most definitely told you!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh look, this isn't an argument!
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    (person,line_said)=each_data.split(":",1)
ValueError: need more than 1 value to unpack
>>> each_line = "I tell you, there's no such thing as a flying circus."
>>> each_line.find(':')
-1
>>> each_line = "I tell you: there's no such thing as a flying circus."
>>> each_line.find(':')
10
>>> data.tell()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    data.tell()
OSError: telling position disabled by next() call
>>> for each_data in data:
	(person,line_said)=each_data.split(":",1)
	print(person,end=" ")
	print(line_said,end="")

	
Other Man  Yes it is!
Man  No it isn't!
Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    (person,line_said)=each_data.split(":",1)
ValueError: need more than 1 value to unpack
>>> data=open("sketch.txt")
>>> for each_data in data:
	if not each_data.find(:)==-1:
		(person,line_said)=each_data.split(":",1)
		print(person,end=" ")
		print(line_said,end="")
		
SyntaxError: invalid syntax
>>> for each_data in data:
	if not each_data.find(":")==-1:
		(person,line_said)=each_data.split(":",1)
		print(person,end=" ")
		print(line_said,end="")
	else: print(each_data,end="")

	
Man  Is this the right room for an argument?
Other Man  I've told you once.
Man  No you haven't!
Other Man  Yes I have.
Man  When?
Other Man  Just now.
Man  No you didn't!
Other Man  Yes I did!
Man  You didn't!
Other Man  I'm telling you, I did!
Man  You did not!
Other Man  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man  Just the five minutes. Thank you.
Other Man  Anyway, I did.
Man  You most certainly did not!
Other Man  Now let's get one thing quite clear: I most definitely told you!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh look, this isn't an argument!
(pause)
Other Man  Yes it is!
Man  No it isn't!
(pause)
Man  It's just contradiction!
Other Man  No it isn't!
Man  It IS!
Other Man  It is NOT!
Man  You just contradicted me!
Other Man  No I didn't!
Man  You DID!
Other Man  No no no!
Man  You did just then!
Other Man  Nonsense!
Man  (exasperated) Oh, this is futile!!
(pause)
Other Man  No it isn't!
Man  Yes it is!
>>> for each_data in data:
	if not each_data.find(":")==-1:
		(person,line_said)=each_data.split(":",1)
		print(person,end=" ")
		print(line_said,end="")

	
>>> 
>>> data.seek(0)
0
>>> for each_data in data:
	if not each_data.find(":")==-1:
		(person,line_said)=each_data.split(":",1)
		print(person,end=" ")
		print(line_said,end="")

		
Man  Is this the right room for an argument?
Other Man  I've told you once.
Man  No you haven't!
Other Man  Yes I have.
Man  When?
Other Man  Just now.
Man  No you didn't!
Other Man  Yes I did!
Man  You didn't!
Other Man  I'm telling you, I did!
Man  You did not!
Other Man  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man  Just the five minutes. Thank you.
Other Man  Anyway, I did.
Man  You most certainly did not!
Other Man  Now let's get one thing quite clear: I most definitely told you!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh no you didn't!
Other Man  Oh yes I did!
Man  Oh look, this isn't an argument!
Other Man  Yes it is!
Man  No it isn't!
Man  It's just contradiction!
Other Man  No it isn't!
Man  It IS!
Other Man  It is NOT!
Man  You just contradicted me!
Other Man  No I didn't!
Man  You DID!
Other Man  No no no!
Man  You did just then!
Other Man  Nonsense!
Man  (exasperated) Oh, this is futile!!
Other Man  No it isn't!
Man  Yes it is!
>>> data.seek(0)
0
>>> for each_data in data:
	if not each_data.find(":")==-1:
		print(each_data.split(":",1))

		
['Man', ' Is this the right room for an argument?\n']
['Other Man', " I've told you once.\n"]
['Man', " No you haven't!\n"]
['Other Man', ' Yes I have.\n']
['Man', ' When?\n']
['Other Man', ' Just now.\n']
['Man', " No you didn't!\n"]
['Other Man', ' Yes I did!\n']
['Man', " You didn't!\n"]
['Other Man', " I'm telling you, I did!\n"]
['Man', ' You did not!\n']
['Other Man', " Oh I'm sorry, is this a five minute argument, or the full half hour?\n"]
['Man', ' Ah! (taking out his wallet and paying) Just the five minutes.\n']
['Other Man', ' Just the five minutes. Thank you.\n']
['Other Man', ' Anyway, I did.\n']
['Man', ' You most certainly did not!\n']
['Other Man', " Now let's get one thing quite clear: I most definitely told you!\n"]
['Man', " Oh no you didn't!\n"]
['Other Man', ' Oh yes I did!\n']
['Man', " Oh no you didn't!\n"]
['Other Man', ' Oh yes I did!\n']
['Man', " Oh look, this isn't an argument!\n"]
['Other Man', ' Yes it is!\n']
['Man', " No it isn't!\n"]
['Man', " It's just contradiction!\n"]
['Other Man', " No it isn't!\n"]
['Man', ' It IS!\n']
['Other Man', ' It is NOT!\n']
['Man', ' You just contradicted me!\n']
['Other Man', " No I didn't!\n"]
['Man', ' You DID!\n']
['Other Man', ' No no no!\n']
['Man', ' You did just then!\n']
['Other Man', ' Nonsense!\n']
['Man', ' (exasperated) Oh, this is futile!!\n']
['Other Man', " No it isn't!\n"]
['Man', ' Yes it is!\n']
>>> for each_data in data:
	if not each_data.find(":")==-1:
		print(len(each_data.split(":",1)))

		
>>> data.seek(0)
0
>>> for each_data in data:
	if not each_data.find(":")==-1:
		print(len(each_data.split(":",1)))

		
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
>>> data.seek(0)
0
>>> for each_data in data:
	try:
		(person,said)=each_data.split(":",1)
		print(person)
		print("::: ",end="")
		print(said,end="")

	except:pass

	
Man
:::  Is this the right room for an argument?
Other Man
:::  I've told you once.
Man
:::  No you haven't!
Other Man
:::  Yes I have.
Man
:::  When?
Other Man
:::  Just now.
Man
:::  No you didn't!
Other Man
:::  Yes I did!
Man
:::  You didn't!
Other Man
:::  I'm telling you, I did!
Man
:::  You did not!
Other Man
:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man
:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man
:::  Just the five minutes. Thank you.
Other Man
:::  Anyway, I did.
Man
:::  You most certainly did not!
Other Man
:::  Now let's get one thing quite clear: I most definitely told you!
Man
:::  Oh no you didn't!
Other Man
:::  Oh yes I did!
Man
:::  Oh no you didn't!
Other Man
:::  Oh yes I did!
Man
:::  Oh look, this isn't an argument!
Other Man
:::  Yes it is!
Man
:::  No it isn't!
Man
:::  It's just contradiction!
Other Man
:::  No it isn't!
Man
:::  It IS!
Other Man
:::  It is NOT!
Man
:::  You just contradicted me!
Other Man
:::  No I didn't!
Man
:::  You DID!
Other Man
:::  No no no!
Man
:::  You did just then!
Other Man
:::  Nonsense!
Man
:::  (exasperated) Oh, this is futile!!
Other Man
:::  No it isn't!
Man
:::  Yes it is!
>>> for each_data in data:
	try:
		(person,said)=each_data.split(":",1)
		print(person)
		print("::: ")
		print(said)

	except:pass

	
>>> data.seek(0)
0
>>> for each_data in data:
	try:
		(person,said)=each_data.split(":",1)
		print(person)
		print("::: ")
		print(said)

	except:pass

	
Man
::: 
 Is this the right room for an argument?

Other Man
::: 
 I've told you once.

Man
::: 
 No you haven't!

Other Man
::: 
 Yes I have.

Man
::: 
 When?

Other Man
::: 
 Just now.

Man
::: 
 No you didn't!

Other Man
::: 
 Yes I did!

Man
::: 
 You didn't!

Other Man
::: 
 I'm telling you, I did!

Man
::: 
 You did not!

Other Man
::: 
 Oh I'm sorry, is this a five minute argument, or the full half hour?

Man
::: 
 Ah! (taking out his wallet and paying) Just the five minutes.

Other Man
::: 
 Just the five minutes. Thank you.

Other Man
::: 
 Anyway, I did.

Man
::: 
 You most certainly did not!

Other Man
::: 
 Now let's get one thing quite clear: I most definitely told you!

Man
::: 
 Oh no you didn't!

Other Man
::: 
 Oh yes I did!

Man
::: 
 Oh no you didn't!

Other Man
::: 
 Oh yes I did!

Man
::: 
 Oh look, this isn't an argument!

Other Man
::: 
 Yes it is!

Man
::: 
 No it isn't!

Man
::: 
 It's just contradiction!

Other Man
::: 
 No it isn't!

Man
::: 
 It IS!

Other Man
::: 
 It is NOT!

Man
::: 
 You just contradicted me!

Other Man
::: 
 No I didn't!

Man
::: 
 You DID!

Other Man
::: 
 No no no!

Man
::: 
 You did just then!

Other Man
::: 
 Nonsense!

Man
::: 
 (exasperated) Oh, this is futile!!

Other Man
::: 
 No it isn't!

Man
::: 
 Yes it is!

>>> for each_data in data:
	try:
		(person,said)=each_data.split(":",1)
		print(person,end="")
		print("::: ",end="")
		print(said,end="")

	except:pass

	
>>> data.seek(0)
0
>>> for each_data in data:
	try:
		(person,said)=each_data.split(":",1)
		print(person,end="")
		print("::: ",end="")
		print(said,end="")

	except:pass

	
Man:::  Is this the right room for an argument?
Other Man:::  I've told you once.
Man:::  No you haven't!
Other Man:::  Yes I have.
Man:::  When?
Other Man:::  Just now.
Man:::  No you didn't!
Other Man:::  Yes I did!
Man:::  You didn't!
Other Man:::  I'm telling you, I did!
Man:::  You did not!
Other Man:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man:::  Just the five minutes. Thank you.
Other Man:::  Anyway, I did.
Man:::  You most certainly did not!
Other Man:::  Now let's get one thing quite clear: I most definitely told you!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh look, this isn't an argument!
Other Man:::  Yes it is!
Man:::  No it isn't!
Man:::  It's just contradiction!
Other Man:::  No it isn't!
Man:::  It IS!
Other Man:::  It is NOT!
Man:::  You just contradicted me!
Other Man:::  No I didn't!
Man:::  You DID!
Other Man:::  No no no!
Man:::  You did just then!
Other Man:::  Nonsense!
Man:::  (exasperated) Oh, this is futile!!
Other Man:::  No it isn't!
Man:::  Yes it is!
>>> data.seek(0)
0
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except:pass
except:print("data file is missing")

Man:::  Is this the right room for an argument?
Other Man:::  I've told you once.
Man:::  No you haven't!
Other Man:::  Yes I have.
Man:::  When?
Other Man:::  Just now.
Man:::  No you didn't!
Other Man:::  Yes I did!
Man:::  You didn't!
Other Man:::  I'm telling you, I did!
Man:::  You did not!
Other Man:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man:::  Just the five minutes. Thank you.
Other Man:::  Anyway, I did.
Man:::  You most certainly did not!
Other Man:::  Now let's get one thing quite clear: I most definitely told you!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh look, this isn't an argument!
Other Man:::  Yes it is!
Man:::  No it isn't!
Man:::  It's just contradiction!
Other Man:::  No it isn't!
Man:::  It IS!
Other Man:::  It is NOT!
Man:::  You just contradicted me!
Other Man:::  No I didn't!
Man:::  You DID!
Other Man:::  No no no!
Man:::  You did just then!
Other Man:::  Nonsense!
Man:::  (exasperated) Oh, this is futile!!
Other Man:::  No it isn't!
Man:::  Yes it is!
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except ValueError:pass
except:print("data file is missing")

Man:::  Is this the right room for an argument?
Other Man:::  I've told you once.
Man:::  No you haven't!
Other Man:::  Yes I have.
Man:::  When?
Other Man:::  Just now.
Man:::  No you didn't!
Other Man:::  Yes I did!
Man:::  You didn't!
Other Man:::  I'm telling you, I did!
Man:::  You did not!
Other Man:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man:::  Just the five minutes. Thank you.
Other Man:::  Anyway, I did.
Man:::  You most certainly did not!
Other Man:::  Now let's get one thing quite clear: I most definitely told you!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh look, this isn't an argument!
Other Man:::  Yes it is!
Man:::  No it isn't!
Man:::  It's just contradiction!
Other Man:::  No it isn't!
Man:::  It IS!
Other Man:::  It is NOT!
Man:::  You just contradicted me!
Other Man:::  No I didn't!
Man:::  You DID!
Other Man:::  No no no!
Man:::  You did just then!
Other Man:::  Nonsense!
Man:::  (exasperated) Oh, this is futile!!
Other Man:::  No it isn't!
Man:::  Yes it is!
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except ValueError:pass
except:print("data file is missing")

Man:::  Is this the right room for an argument?
Other Man:::  I've told you once.
Man:::  No you haven't!
Other Man:::  Yes I have.
Man:::  When?
Other Man:::  Just now.
Man:::  No you didn't!
Other Man:::  Yes I did!
Man:::  You didn't!
Other Man:::  I'm telling you, I did!
Man:::  You did not!
Other Man:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man:::  Just the five minutes. Thank you.
Other Man:::  Anyway, I did.
Man:::  You most certainly did not!
Other Man:::  Now let's get one thing quite clear: I most definitely told you!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh look, this isn't an argument!
Other Man:::  Yes it is!
Man:::  No it isn't!
Man:::  It's just contradiction!
Other Man:::  No it isn't!
Man:::  It IS!
Other Man:::  It is NOT!
Man:::  You just contradicted me!
Other Man:::  No I didn't!
Man:::  You DID!
Other Man:::  No no no!
Man:::  You did just then!
Other Man:::  Nonsense!
Man:::  (exasperated) Oh, this is futile!!
Other Man:::  No it isn't!
Man:::  Yes it is!
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except ValueError:pass
except:print("data file is missing")

data file is missing
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except ValueError:pass
except IOError:print("data file is missing")

data file is missing
>>> try:
	data=open("sketch.txt")
	for each_data in data:
		try:
			(person,said)=each_data.split(":",1)
			print(person,end="")
			print("::: ",end="")
			print(said,end="")

		except ValueError:pass
except IOError:print("data file is missing")

Man:::  Is this the right room for an argument?
Other Man:::  I've told you once.
Man:::  No you haven't!
Other Man:::  Yes I have.
Man:::  When?
Other Man:::  Just now.
Man:::  No you didn't!
Other Man:::  Yes I did!
Man:::  You didn't!
Other Man:::  I'm telling you, I did!
Man:::  You did not!
Other Man:::  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man:::  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man:::  Just the five minutes. Thank you.
Other Man:::  Anyway, I did.
Man:::  You most certainly did not!
Other Man:::  Now let's get one thing quite clear: I most definitely told you!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh no you didn't!
Other Man:::  Oh yes I did!
Man:::  Oh look, this isn't an argument!
Other Man:::  Yes it is!
Man:::  No it isn't!
Man:::  It's just contradiction!
Other Man:::  No it isn't!
Man:::  It IS!
Other Man:::  It is NOT!
Man:::  You just contradicted me!
Other Man:::  No I didn't!
Man:::  You DID!
Other Man:::  No no no!
Man:::  You did just then!
Other Man:::  Nonsense!
Man:::  (exasperated) Oh, this is futile!!
Other Man:::  No it isn't!
Man:::  Yes it is!
>>>  data.seek()
 
SyntaxError: unexpected indent
>>> data.seek()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    data.seek()
TypeError: seek() takes at least 1 argument (0 given)
>>> data=open("nofile",w)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    data=open("nofile",w)
NameError: name 'w' is not defined
>>> data=open("nofile","w")
>>> data=open("nofile1","w+")
>>> data=open("nofile1","a")
>>> try:
	man_file = open('man_data.txt', 'w')
	other_file = open('other_data.txt', 'w')
	print("man_string", file=man_file)
	print("other_man_string", file=other_file)
except IOError:
	print('File error.')

finally:
	man_file.close()
	other_file.close()

	
>>> try:
	man_file = open('man_data.txt', 'w')
	other_file = open('other_data.txt')
	print("man_string", file=man_file)
	print("other_man_string", file=other_file)
except IOError:
	print('File error.')

finally:
	man_file.close()
	other_file.close()

	
File error.
>>> data.seek(0)
0
>>> data.tell()
0
>>> print(len(data))
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print(len(data))
TypeError: object of type '_io.TextIOWrapper' has no len()
>>> print(data)
<_io.TextIOWrapper name='nofile1' mode='a' encoding='UTF-8'>
>>> data=open("sketch.txt")
>>> if data in locals()
SyntaxError: invalid syntax
>>> 
>>> if "data" in locals():
	print("its der")

	
its der
>>> print(locals())
{'__loader__': <class '_frozen_importlib.BuiltinImporter'>, 'line_said': ' Yes it is!\n', 'other_file': <_io.TextIOWrapper name='other_data.txt' mode='r' encoding='UTF-8'>, '__warningregistry__': {("unclosed file <_io.TextIOWrapper name='sketch.txt' mode='r' encoding='UTF-8'>", <class 'ResourceWarning'>, 1): True, ("unclosed file <_io.TextIOWrapper name='nofile1' mode='w+' encoding='UTF-8'>", <class 'ResourceWarning'>, 1): True, 'version': 0, ("unclosed file <_io.TextIOWrapper name='nofile1' mode='a' encoding='UTF-8'>", <class 'ResourceWarning'>, 1): True, ("unclosed file <_io.TextIOWrapper name='sketch.txt' mode='r' encoding='UTF-8'>", <class 'ResourceWarning'>, 2): True, ("unclosed file <_io.TextIOWrapper name='nofile' mode='w' encoding='UTF-8'>", <class 'ResourceWarning'>, 1): True}, '__builtins__': <module 'builtins' (built-in)>, 'os': <module 'os' from '/usr/lib/python3.4/os.py'>, 'said': ' Yes it is!\n', '__package__': None, 'man_file': <_io.TextIOWrapper name='man_data.txt' mode='w' encoding='UTF-8'>, '__spec__': None, 'person': 'Man', 'each_data': 'Man: Yes it is!\n', 'each_line': "I tell you: there's no such thing as a flying circus.", 'data': <_io.TextIOWrapper name='sketch.txt' mode='r' encoding='UTF-8'>, '__doc__': None, '__name__': '__main__'}
>>> 
