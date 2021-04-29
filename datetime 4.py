Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 4, 28, 11, 22, 8, 177826)
>>> import datetime
>>> datetime.MAXYEAR
9999
>>> datetime.MINYEAR
1
>>> datetime.date
<class 'datetime.date'>
>>> datetime.datetime.date
<method 'date' of 'datetime.datetime' objects>
>>> datetime.datetime.now()
datetime.datetime(2021, 4, 28, 11, 24, 30, 76990)
>>> datetime.sys
<module 'sys' (built-in)>
>>> datetime.datetime.hour
<attribute 'hour' of 'datetime.datetime' objects>
>>> datetime.datetime.hour()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    datetime.datetime.hour()
TypeError: 'getset_descriptor' object is not callable
>>> datetime.datetime.now()
datetime.datetime(2021, 4, 28, 11, 27, 40, 542698)
>>> datetime.timedelta(30)
datetime.timedelta(days=30)
>>> x=datetime.datetime.now()
>>> x
datetime.datetime(2021, 4, 28, 11, 28, 14, 588826)
>>> y=datetime.timedelta(30)
>>> x+y
datetime.datetime(2021, 5, 28, 11, 28, 14, 588826)
>>> from datetime import date
>>> today=date.today()
>>> today
datetime.date(2021, 4, 28)
>>> x=day.today()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=day.today()
NameError: name 'day' is not defined
>>> print(today.year)
2021
>>> print(today.day)
28
>>> import time
>>> x=time.time()
>>> x
1619589795.1497397
>>> y=time.localtime(time.time())
>>> y
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=28, tm_hour=11, tm_min=34, tm_sec=33, tm_wday=2, tm_yday=118, tm_isdst=0)
>>> z=time.asctime()
>>> z
'Wed Apr 28 11:35:22 2021'
>>> from datetime import datetime
>>> x=datetime.now()
>>> x
datetime.datetime(2021, 4, 28, 11, 37, 24, 999590)
>>> import datetime
>>> x=datetime.MAXYEAR
>>> x
9999
>>> y=datetime.MINYEAR
>>> y
1
>>> y=datetime.timedelta(10)
>>> y
datetime.timedelta(days=10)
>>> x=datetime.datetime.now()
>>> x+y
datetime.datetime(2021, 5, 8, 11, 39, 25, 452759)
>>> datetime.time
<class 'datetime.time'>
>>> import time
>>> x=time.time()
>>> x
1619590232.0744717
>>> y=time.localtime(time.time())
>>> y
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=28, tm_hour=11, tm_min=41, tm_sec=0, tm_wday=2, tm_yday=118, tm_isdst=0)
>>> time.asctime()
'Wed Apr 28 11:41:22 2021'
>>> from datetime import date
>>> x=today.date()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x=today.date()
AttributeError: 'datetime.date' object has no attribute 'date'
>>> x=today.date
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x=today.date
AttributeError: 'datetime.date' object has no attribute 'date'
>>> from datetime import date
>>> x=date.today()
>>> x
datetime.date(2021, 4, 28)
>>> x=date.today()
>>> x
datetime.date(2021, 4, 28)
>>> print(today.month)
4
>>> print(x.year)
2021
>>> print(x.day)
28
>>> datetime.date(2021,4,21)
datetime.date(2021, 4, 21)
>>> import time
>>> x=time.time()
>>> x
1619590608.4522307
>>> time.localtime(time.time())
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=28, tm_hour=11, tm_min=47, tm_sec=14, tm_wday=2, tm_yday=118, tm_isdst=0)
>>> time.asctime()
'Wed Apr 28 11:47:53 2021'
>>> import datetime
>>> datetime.MAXYEAR
9999
>>> datetime.MINYEAR
1
>>> datetime.timedelta(3)
datetime.timedelta(days=3)
>>> datetime.datetime.now()+datetime.timedelta(3)
datetime.datetime(2021, 5, 1, 11, 52, 6, 74198)
>>> from datetime import date
>>> date.replace
<method 'replace' of 'datetime.date' objects>
>>> date.replace(8/9/2021)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    date.replace(8/9/2021)
TypeError: descriptor 'replace' for 'datetime.date' objects doesn't apply to a 'float' object
>>> date.today()
datetime.date(2021, 4, 28)
>>> from datetime import date
>>> today=date.today()
>>> def age(birthdate):
	today=date.today()
	age=(today.year-birthday.year),((today.month,today.day)<(birth.month,birth.day))
	print(age)

	
>>> age(1998,3,5)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    age(1998,3,5)
TypeError: age() takes 1 positional argument but 3 were given
>>> from datetime import date
>>> def age(birthdate):
	today=date.today()
	age=(today.year-birthdate.year),((today.month,today.day)<(birth.month,birth.day))
	print(age)

	
>>> import datetime
>>> x=datetime.date(1998,3,5)
>>> today=date.today()
>>> age=(today.year-x.year),(today.month-x.month),(today.day-x.day)
>>> print("age is:"age "years")
SyntaxError: invalid syntax
>>> print(age)
(23, 1, 23)
>>> import datetime
>>> x=datetime.date(1998,3,5)
>>> today=date.today()
>>> age=(today.year-x.year),(today.month-x.month),(today.day-x.day)
>>> import datetime
>>> x=datetime.date(1998,3,5)
>>> today=date.today()
>>> age=(today.year-x.year)-((today.month,today.day) <(x.month,x.day))
>>> print(age)
23
>>> import datetime
>>> from datetime import date
>>> class sample():
	def display(self):
		x=datetime.date(1998,3,5)
		today=date.today()
		year=(today.year-x.year)
		month=(today.month-x.month)
		day=(today.day-x.day)
		print("{}year,{}month,{}days".format(year,month,day))

		
>>> s=sample()
>>> s.display()
23year,1month,23days
>>> import datetime
>>> datetime.MAXYEAR
9999
>>> import datetime
>>> from datetime import date
>>> date.weekday()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    date.weekday()
TypeError: unbound method date.weekday() needs an argument
>>> date.weekday
<method 'weekday' of 'datetime.date' objects>
>>> x=date.today()
>>> x
datetime.date(2021, 4, 28)
>>> print(x.weekday())
2
>>> x:int
>>> x=56.7
>>> x
56.7
>>> import datetime
>>> datetime.date(2012,6,7)
datetime.date(2012, 6, 7)
>>> datetime.datetime.now()
datetime.datetime(2021, 4, 28, 12, 58, 19, 76274)
>>> from datetime import date
>>> datetime.date(2021,5,7)
datetime.date(2021, 5, 7)
>>> 
============ RESTART: C:/Users/dhanya/AppData/Local/Programs/Python/Python39/t2.py ============
Traceback (most recent call last):
  File "C:/Users/dhanya/AppData/Local/Programs/Python/Python39/t2.py", line 2, in <module>
    x=datetime.date(4040,5,6)
NameError: name 'datetime' is not defined
>>> 
============ RESTART: C:/Users/dhanya/AppData/Local/Programs/Python/Python39/t2.py ============
>>> x
datetime.date(4506, 6, 7)
>>> 
>>> import datetime
>>> datetime.date(5050,5,5)
datetime.date(5050, 5, 5)
>>> datetime.datetime.now()
datetime.datetime(2021, 4, 28, 13, 32, 42, 236278)
>>> import time
>>> x=time.time()
>>> x
1619597099.557653
>>> x=time.localtime(time.time())
>>> x
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=28, tm_hour=13, tm_min=35, tm_sec=23, tm_wday=2, tm_yday=118, tm_isdst=0)
>>> x=time.asctime()
>>> x
'Wed Apr 28 13:38:23 2021'
>>> from datetime import date
>>> date.today()
datetime.date(2021, 4, 28)
>>> today.year
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    today.year
NameError: name 'today' is not defined
>>> x=date.today()
>>> x.year
2021
>>> x.month
4
>>> date.day
<attribute 'day' of 'datetime.date' objects>
>>> date.day()
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    date.day()
TypeError: 'getset_descriptor' object is not callable
>>> date.today()
datetime.date(2021, 4, 28)
>>> 