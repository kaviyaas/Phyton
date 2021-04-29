Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 12<23
True
>>> 10<45
True
>>> 12<2
False
>>> 12<5
False
>>> 12>56
False
>>> 45>12
True
>>> 23>15
True
>>> 12<=3
False
>>> 34<=21
False
>>> 12<=67
True
>>> 23<=78
True
>>> 
>>> 67<=56
False
>>> 67>=56
True
>>> 67>=45
True
>>> 1001>=1000
True
>>> 456>=678
False
>>> 7890>=4560
True
>>> x,y=456,672
>>> X>=y
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    X>=y
NameError: name 'X' is not defined
>>> x>=y
False
>>> x<=y
True
>>> X>y
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    X>y
NameError: name 'X' is not defined
>>> x>y
False
>>> x<y
True
>>> x!=y
True
>>> x==y
False
>>> 500==500
True
>>> 500!=591
True
>>> x,y=23,45
>>> x<y
True
>>> x>y
False
>>> x<=y
True
>>> x>=y
False
>>> x==y
False
>>> x!=y
True
>>> x+=1
>>> x
24
>>> x-=2
>>> x
22
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> "quit"

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help()keyword
SyntaxError: invalid syntax
>>> help>keyword
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    help>keyword
NameError: name 'keyword' is not defined
>>> help>keywords
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    help>keywords
NameError: name 'keywords' is not defined
>>> help>Keywords
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    help>Keywords
NameError: name 'Keywords' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

