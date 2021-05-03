Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calendar
>>> a=calendar.TextCalendar(0)
>>> a.year
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.year
AttributeError: 'TextCalendar' object has no attribute 'year'
>>> a.formatyear(2020)
'                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'
>>> a.formatmonthname(2020,4)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.formatmonthname(2020,4)
TypeError: formatmonthname() missing 1 required positional argument: 'width'
>>> a.formatmonthname(2020,3,1)
'March 2020'
>>> a.formatmonth(2021,3)
'     March 2021\nMo Tu We Th Fr Sa Su\n 1  2  3  4  5  6  7\n 8  9 10 11 12 13 14\n15 16 17 18 19 20 21\n22 23 24 25 26 27 28\n29 30 31\n'
>>> a.yeardatescalendar(2021,3)
[[[[datetime.date(2020, 12, 28), datetime.date(2020, 12, 29), datetime.date(2020, 12, 30), datetime.date(2020, 12, 31), datetime.date(2021, 1, 1), datetime.date(2021, 1, 2), datetime.date(2021, 1, 3)], [datetime.date(2021, 1, 4), datetime.date(2021, 1, 5), datetime.date(2021, 1, 6), datetime.date(2021, 1, 7), datetime.date(2021, 1, 8), datetime.date(2021, 1, 9), datetime.date(2021, 1, 10)], [datetime.date(2021, 1, 11), datetime.date(2021, 1, 12), datetime.date(2021, 1, 13), datetime.date(2021, 1, 14), datetime.date(2021, 1, 15), datetime.date(2021, 1, 16), datetime.date(2021, 1, 17)], [datetime.date(2021, 1, 18), datetime.date(2021, 1, 19), datetime.date(2021, 1, 20), datetime.date(2021, 1, 21), datetime.date(2021, 1, 22), datetime.date(2021, 1, 23), datetime.date(2021, 1, 24)], [datetime.date(2021, 1, 25), datetime.date(2021, 1, 26), datetime.date(2021, 1, 27), datetime.date(2021, 1, 28), datetime.date(2021, 1, 29), datetime.date(2021, 1, 30), datetime.date(2021, 1, 31)]], [[datetime.date(2021, 2, 1), datetime.date(2021, 2, 2), datetime.date(2021, 2, 3), datetime.date(2021, 2, 4), datetime.date(2021, 2, 5), datetime.date(2021, 2, 6), datetime.date(2021, 2, 7)], [datetime.date(2021, 2, 8), datetime.date(2021, 2, 9), datetime.date(2021, 2, 10), datetime.date(2021, 2, 11), datetime.date(2021, 2, 12), datetime.date(2021, 2, 13), datetime.date(2021, 2, 14)], [datetime.date(2021, 2, 15), datetime.date(2021, 2, 16), datetime.date(2021, 2, 17), datetime.date(2021, 2, 18), datetime.date(2021, 2, 19), datetime.date(2021, 2, 20), datetime.date(2021, 2, 21)], [datetime.date(2021, 2, 22), datetime.date(2021, 2, 23), datetime.date(2021, 2, 24), datetime.date(2021, 2, 25), datetime.date(2021, 2, 26), datetime.date(2021, 2, 27), datetime.date(2021, 2, 28)]], [[datetime.date(2021, 3, 1), datetime.date(2021, 3, 2), datetime.date(2021, 3, 3), datetime.date(2021, 3, 4), datetime.date(2021, 3, 5), datetime.date(2021, 3, 6), datetime.date(2021, 3, 7)], [datetime.date(2021, 3, 8), datetime.date(2021, 3, 9), datetime.date(2021, 3, 10), datetime.date(2021, 3, 11), datetime.date(2021, 3, 12), datetime.date(2021, 3, 13), datetime.date(2021, 3, 14)], [datetime.date(2021, 3, 15), datetime.date(2021, 3, 16), datetime.date(2021, 3, 17), datetime.date(2021, 3, 18), datetime.date(2021, 3, 19), datetime.date(2021, 3, 20), datetime.date(2021, 3, 21)], [datetime.date(2021, 3, 22), datetime.date(2021, 3, 23), datetime.date(2021, 3, 24), datetime.date(2021, 3, 25), datetime.date(2021, 3, 26), datetime.date(2021, 3, 27), datetime.date(2021, 3, 28)], [datetime.date(2021, 3, 29), datetime.date(2021, 3, 30), datetime.date(2021, 3, 31), datetime.date(2021, 4, 1), datetime.date(2021, 4, 2), datetime.date(2021, 4, 3), datetime.date(2021, 4, 4)]]], [[[datetime.date(2021, 3, 29), datetime.date(2021, 3, 30), datetime.date(2021, 3, 31), datetime.date(2021, 4, 1), datetime.date(2021, 4, 2), datetime.date(2021, 4, 3), datetime.date(2021, 4, 4)], [datetime.date(2021, 4, 5), datetime.date(2021, 4, 6), datetime.date(2021, 4, 7), datetime.date(2021, 4, 8), datetime.date(2021, 4, 9), datetime.date(2021, 4, 10), datetime.date(2021, 4, 11)], [datetime.date(2021, 4, 12), datetime.date(2021, 4, 13), datetime.date(2021, 4, 14), datetime.date(2021, 4, 15), datetime.date(2021, 4, 16), datetime.date(2021, 4, 17), datetime.date(2021, 4, 18)], [datetime.date(2021, 4, 19), datetime.date(2021, 4, 20), datetime.date(2021, 4, 21), datetime.date(2021, 4, 22), datetime.date(2021, 4, 23), datetime.date(2021, 4, 24), datetime.date(2021, 4, 25)], [datetime.date(2021, 4, 26), datetime.date(2021, 4, 27), datetime.date(2021, 4, 28), datetime.date(2021, 4, 29), datetime.date(2021, 4, 30), datetime.date(2021, 5, 1), datetime.date(2021, 5, 2)]], [[datetime.date(2021, 4, 26), datetime.date(2021, 4, 27), datetime.date(2021, 4, 28), datetime.date(2021, 4, 29), datetime.date(2021, 4, 30), datetime.date(2021, 5, 1), datetime.date(2021, 5, 2)], [datetime.date(2021, 5, 3), datetime.date(2021, 5, 4), datetime.date(2021, 5, 5), datetime.date(2021, 5, 6), datetime.date(2021, 5, 7), datetime.date(2021, 5, 8), datetime.date(2021, 5, 9)], [datetime.date(2021, 5, 10), datetime.date(2021, 5, 11), datetime.date(2021, 5, 12), datetime.date(2021, 5, 13), datetime.date(2021, 5, 14), datetime.date(2021, 5, 15), datetime.date(2021, 5, 16)], [datetime.date(2021, 5, 17), datetime.date(2021, 5, 18), datetime.date(2021, 5, 19), datetime.date(2021, 5, 20), datetime.date(2021, 5, 21), datetime.date(2021, 5, 22), datetime.date(2021, 5, 23)], [datetime.date(2021, 5, 24), datetime.date(2021, 5, 25), datetime.date(2021, 5, 26), datetime.date(2021, 5, 27), datetime.date(2021, 5, 28), datetime.date(2021, 5, 29), datetime.date(2021, 5, 30)], [datetime.date(2021, 5, 31), datetime.date(2021, 6, 1), datetime.date(2021, 6, 2), datetime.date(2021, 6, 3), datetime.date(2021, 6, 4), datetime.date(2021, 6, 5), datetime.date(2021, 6, 6)]], [[datetime.date(2021, 5, 31), datetime.date(2021, 6, 1), datetime.date(2021, 6, 2), datetime.date(2021, 6, 3), datetime.date(2021, 6, 4), datetime.date(2021, 6, 5), datetime.date(2021, 6, 6)], [datetime.date(2021, 6, 7), datetime.date(2021, 6, 8), datetime.date(2021, 6, 9), datetime.date(2021, 6, 10), datetime.date(2021, 6, 11), datetime.date(2021, 6, 12), datetime.date(2021, 6, 13)], [datetime.date(2021, 6, 14), datetime.date(2021, 6, 15), datetime.date(2021, 6, 16), datetime.date(2021, 6, 17), datetime.date(2021, 6, 18), datetime.date(2021, 6, 19), datetime.date(2021, 6, 20)], [datetime.date(2021, 6, 21), datetime.date(2021, 6, 22), datetime.date(2021, 6, 23), datetime.date(2021, 6, 24), datetime.date(2021, 6, 25), datetime.date(2021, 6, 26), datetime.date(2021, 6, 27)], [datetime.date(2021, 6, 28), datetime.date(2021, 6, 29), datetime.date(2021, 6, 30), datetime.date(2021, 7, 1), datetime.date(2021, 7, 2), datetime.date(2021, 7, 3), datetime.date(2021, 7, 4)]]], [[[datetime.date(2021, 6, 28), datetime.date(2021, 6, 29), datetime.date(2021, 6, 30), datetime.date(2021, 7, 1), datetime.date(2021, 7, 2), datetime.date(2021, 7, 3), datetime.date(2021, 7, 4)], [datetime.date(2021, 7, 5), datetime.date(2021, 7, 6), datetime.date(2021, 7, 7), datetime.date(2021, 7, 8), datetime.date(2021, 7, 9), datetime.date(2021, 7, 10), datetime.date(2021, 7, 11)], [datetime.date(2021, 7, 12), datetime.date(2021, 7, 13), datetime.date(2021, 7, 14), datetime.date(2021, 7, 15), datetime.date(2021, 7, 16), datetime.date(2021, 7, 17), datetime.date(2021, 7, 18)], [datetime.date(2021, 7, 19), datetime.date(2021, 7, 20), datetime.date(2021, 7, 21), datetime.date(2021, 7, 22), datetime.date(2021, 7, 23), datetime.date(2021, 7, 24), datetime.date(2021, 7, 25)], [datetime.date(2021, 7, 26), datetime.date(2021, 7, 27), datetime.date(2021, 7, 28), datetime.date(2021, 7, 29), datetime.date(2021, 7, 30), datetime.date(2021, 7, 31), datetime.date(2021, 8, 1)]], [[datetime.date(2021, 7, 26), datetime.date(2021, 7, 27), datetime.date(2021, 7, 28), datetime.date(2021, 7, 29), datetime.date(2021, 7, 30), datetime.date(2021, 7, 31), datetime.date(2021, 8, 1)], [datetime.date(2021, 8, 2), datetime.date(2021, 8, 3), datetime.date(2021, 8, 4), datetime.date(2021, 8, 5), datetime.date(2021, 8, 6), datetime.date(2021, 8, 7), datetime.date(2021, 8, 8)], [datetime.date(2021, 8, 9), datetime.date(2021, 8, 10), datetime.date(2021, 8, 11), datetime.date(2021, 8, 12), datetime.date(2021, 8, 13), datetime.date(2021, 8, 14), datetime.date(2021, 8, 15)], [datetime.date(2021, 8, 16), datetime.date(2021, 8, 17), datetime.date(2021, 8, 18), datetime.date(2021, 8, 19), datetime.date(2021, 8, 20), datetime.date(2021, 8, 21), datetime.date(2021, 8, 22)], [datetime.date(2021, 8, 23), datetime.date(2021, 8, 24), datetime.date(2021, 8, 25), datetime.date(2021, 8, 26), datetime.date(2021, 8, 27), datetime.date(2021, 8, 28), datetime.date(2021, 8, 29)], [datetime.date(2021, 8, 30), datetime.date(2021, 8, 31), datetime.date(2021, 9, 1), datetime.date(2021, 9, 2), datetime.date(2021, 9, 3), datetime.date(2021, 9, 4), datetime.date(2021, 9, 5)]], [[datetime.date(2021, 8, 30), datetime.date(2021, 8, 31), datetime.date(2021, 9, 1), datetime.date(2021, 9, 2), datetime.date(2021, 9, 3), datetime.date(2021, 9, 4), datetime.date(2021, 9, 5)], [datetime.date(2021, 9, 6), datetime.date(2021, 9, 7), datetime.date(2021, 9, 8), datetime.date(2021, 9, 9), datetime.date(2021, 9, 10), datetime.date(2021, 9, 11), datetime.date(2021, 9, 12)], [datetime.date(2021, 9, 13), datetime.date(2021, 9, 14), datetime.date(2021, 9, 15), datetime.date(2021, 9, 16), datetime.date(2021, 9, 17), datetime.date(2021, 9, 18), datetime.date(2021, 9, 19)], [datetime.date(2021, 9, 20), datetime.date(2021, 9, 21), datetime.date(2021, 9, 22), datetime.date(2021, 9, 23), datetime.date(2021, 9, 24), datetime.date(2021, 9, 25), datetime.date(2021, 9, 26)], [datetime.date(2021, 9, 27), datetime.date(2021, 9, 28), datetime.date(2021, 9, 29), datetime.date(2021, 9, 30), datetime.date(2021, 10, 1), datetime.date(2021, 10, 2), datetime.date(2021, 10, 3)]]], [[[datetime.date(2021, 9, 27), datetime.date(2021, 9, 28), datetime.date(2021, 9, 29), datetime.date(2021, 9, 30), datetime.date(2021, 10, 1), datetime.date(2021, 10, 2), datetime.date(2021, 10, 3)], [datetime.date(2021, 10, 4), datetime.date(2021, 10, 5), datetime.date(2021, 10, 6), datetime.date(2021, 10, 7), datetime.date(2021, 10, 8), datetime.date(2021, 10, 9), datetime.date(2021, 10, 10)], [datetime.date(2021, 10, 11), datetime.date(2021, 10, 12), datetime.date(2021, 10, 13), datetime.date(2021, 10, 14), datetime.date(2021, 10, 15), datetime.date(2021, 10, 16), datetime.date(2021, 10, 17)], [datetime.date(2021, 10, 18), datetime.date(2021, 10, 19), datetime.date(2021, 10, 20), datetime.date(2021, 10, 21), datetime.date(2021, 10, 22), datetime.date(2021, 10, 23), datetime.date(2021, 10, 24)], [datetime.date(2021, 10, 25), datetime.date(2021, 10, 26), datetime.date(2021, 10, 27), datetime.date(2021, 10, 28), datetime.date(2021, 10, 29), datetime.date(2021, 10, 30), datetime.date(2021, 10, 31)]], [[datetime.date(2021, 11, 1), datetime.date(2021, 11, 2), datetime.date(2021, 11, 3), datetime.date(2021, 11, 4), datetime.date(2021, 11, 5), datetime.date(2021, 11, 6), datetime.date(2021, 11, 7)], [datetime.date(2021, 11, 8), datetime.date(2021, 11, 9), datetime.date(2021, 11, 10), datetime.date(2021, 11, 11), datetime.date(2021, 11, 12), datetime.date(2021, 11, 13), datetime.date(2021, 11, 14)], [datetime.date(2021, 11, 15), datetime.date(2021, 11, 16), datetime.date(2021, 11, 17), datetime.date(2021, 11, 18), datetime.date(2021, 11, 19), datetime.date(2021, 11, 20), datetime.date(2021, 11, 21)], [datetime.date(2021, 11, 22), datetime.date(2021, 11, 23), datetime.date(2021, 11, 24), datetime.date(2021, 11, 25), datetime.date(2021, 11, 26), datetime.date(2021, 11, 27), datetime.date(2021, 11, 28)], [datetime.date(2021, 11, 29), datetime.date(2021, 11, 30), datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), datetime.date(2021, 12, 3), datetime.date(2021, 12, 4), datetime.date(2021, 12, 5)]], [[datetime.date(2021, 11, 29), datetime.date(2021, 11, 30), datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), datetime.date(2021, 12, 3), datetime.date(2021, 12, 4), datetime.date(2021, 12, 5)], [datetime.date(2021, 12, 6), datetime.date(2021, 12, 7), datetime.date(2021, 12, 8), datetime.date(2021, 12, 9), datetime.date(2021, 12, 10), datetime.date(2021, 12, 11), datetime.date(2021, 12, 12)], [datetime.date(2021, 12, 13), datetime.date(2021, 12, 14), datetime.date(2021, 12, 15), datetime.date(2021, 12, 16), datetime.date(2021, 12, 17), datetime.date(2021, 12, 18), datetime.date(2021, 12, 19)], [datetime.date(2021, 12, 20), datetime.date(2021, 12, 21), datetime.date(2021, 12, 22), datetime.date(2021, 12, 23), datetime.date(2021, 12, 24), datetime.date(2021, 12, 25), datetime.date(2021, 12, 26)], [datetime.date(2021, 12, 27), datetime.date(2021, 12, 28), datetime.date(2021, 12, 29), datetime.date(2021, 12, 30), datetime.date(2021, 12, 31), datetime.date(2022, 1, 1), datetime.date(2022, 1, 2)]]]]
>>> import datetime
>>> x=datetime.MINYEAR
>>> x
1
>>> x=datetime.timedelta(5)
>>> from datetime import datetime
>>> y=datetime.now()
>>> x+y
datetime.datetime(2021, 5, 8, 11, 44, 29, 197077)
>>> y.day
3
>>> z=x+y
>>> z.day
8
>>> z.year
2021
>>> z.month
5
>>> z.microsecond
197077
>>> z.second
29
>>> from datetime import date
>>> x=date.today()
>>> x
datetime.date(2021, 5, 3)
>>> import datetime
>>> x=datetime.date(2020,5,6)
>>> x
datetime.date(2020, 5, 6)
>>> import time
>>> x=time.time()
>>> x
1620023159.495695
>>> a=time.localtime(time,time())
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a=time.localtime(time,time())
TypeError: 'module' object is not callable
>>> a=time.localtime(time.time())
>>> a
time.struct_time(tm_year=2021, tm_mon=5, tm_mday=3, tm_hour=11, tm_min=57, tm_sec=14, tm_wday=0, tm_yday=123, tm_isdst=0)
>>> import calendar
>>> a=a.year
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a=a.year
AttributeError: 'time.struct_time' object has no attribute 'year'
>>> import calendar
>>> x=calendar.calendar(2020)
>>> x
'                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'
>>> x.upper
<built-in method upper of str object at 0x0000024F9A2C15C0>
>>> calendar.leapdays(2020,2021)
1
>>> calendar.leapdays(2020,2024)
1
>>> import calendar
>>> class sample():
	a=calendar.TextCalendar(0)
	print(a)

	
<calendar.TextCalendar object at 0x0000024F9A1F9D60>
>>> 
>>> import calendar
>>> a=calendar.HTMLCalendar
>>> a
<class 'calendar.HTMLCalendar'>
>>> for i in calendar.month_name:
	print(i)

	

January
February
March
April
May
June
July
August
September
October
November
December
>>> for i in calendar.month_abbr:
	print(i)

	

Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
>>> import calendar
>>> mydata={}
>>> x=calendar.TextCalendar(0)
>>> x
<calendar.TextCalendar object at 0x0000024F9A1F9E80>
>>> x.formatmonth(2020,4)
'     April 2020\nMo Tu We Th Fr Sa Su\n       1  2  3  4  5\n 6  7  8  9 10 11 12\n13 14 15 16 17 18 19\n20 21 22 23 24 25 26\n27 28 29 30\n'
>>> for i in calendar.month_abbr:
	print(i)

	

Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
>>> len(i)
3
>>> x.formatyear(2020)
'                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'
>>> mydata[i]=x.formatyear(2020)
>>> print(mydata)
{'Dec': '                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'}
>>> import calendar
>>> a=calendar.calendar(2020)
>>> a
'                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'
>>> calendar.monthcalendar(2020,4)
[[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 0, 0, 0]]
>>> calendar.day_abbr
<calendar._localized_day object at 0x0000024F9A1F9070>
>>> c=calendar.day_abbr
>>> c
<calendar._localized_day object at 0x0000024F9A1F9070>
>>> for i in range(0,3):
	print(i)
    if(i==3):
	    
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(0,3):
	print(i) if(i==3):
		
SyntaxError: invalid syntax
>>> for i in range(0,3):
	print(i)
	if(i==3):
	 break

	
0
1
2
>>> for i in range(0,3):
	if(i==3):
	 break
	print(i)

	
0
1
2
>>> for i in range(1,3):
	if(i==3):
	 break
	print(i)

	
1
2
>>> for i in range(0,3):
	print(i)
	if(i==3):
	 break

	
0
1
2
>>> for i in range(1,3):
	print(i)
	if(i==3):
	 break

	
1
2
>>> 