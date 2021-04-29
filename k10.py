Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0 and 0
0
>>> 0 and 1
0
>>> 1 and 0
0
>>> 1 and 1
1
>>> 0&0
0
>>> 0&1
0
>>> 1&0
0
>>> 1&1
1
>>> false&false
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    false&false
NameError: name 'false' is not defined
>>> False&False
False
>>> False&True
False
>>> True&False
False
>>> True&True
True
>>> False and False
False
>>> True and False
False
>>> True and True
True
>>> 0|0
0
>>> 0|1
1
>>> 1|0
1
>>> 1|1
1
>>> 0 or 0
0
>>> 0 or 1
1
>>> 1 or 0
1
>>> 1 or 1
1
>>> False | False
False
>>> True | True
True
>>> True | False
True
>>> False | True
True
>>> not True
False
>>> not not not False
True
>>> not not not not false
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    not not not not false
NameError: name 'false' is not defined
>>> not not not not False
False
>>> not not not not not true
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    not not not not not true
NameError: name 'true' is not defined
>>> not not not not not False
True
>>> 0 xor 0
SyntaxError: invalid syntax
>>> 0 ^ 0
0
>>> 0 ^ 1
1
>>> 1 ^ 0
1
>>> 1 ^ 1
0
>>> False ^ False
False
>>> False ^ True
True
>>> True ^ True
False
>>> True ^ False
True
>>> 0 Ex- or 0
SyntaxError: invalid syntax
>>> 0 and 0
0
>>> 1 and 1
1
>>> 0 and 1
0
>>> 1 and 0
0
>>> 1 or 0
1
>>> 0 or 1
1
>>> 1 or 0
1
>>> 1 or 1
1
>>> 1 ^^ 1
SyntaxError: invalid syntax
>>> 1^1
0
>>> True ^ True
False
>>> False ^ False
False
>>> False ^ true
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    False ^ true
NameError: name 'true' is not defined
>>> 
>>> False ^ True
True
>>> True ^ False
True
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

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> ~ True
-2
>>> ~ ~ True
1
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

help> ~

help> not
Boolean operations
******************

   or_test  ::= and_test | or_test "or" and_test
   and_test ::= not_test | and_test "and" not_test
   not_test ::= comparison | "not" not_test

In the context of Boolean operations, and also when expressions are
used by control flow statements, the following values are interpreted
as false: "False", "None", numeric zero of all types, and empty
strings and containers (including strings, tuples, lists,
dictionaries, sets and frozensets).  All other values are interpreted
as true.  User-defined objects can customize their truth value by
providing a "__bool__()" method.

The operator "not" yields "True" if its argument is false, "False"
otherwise.

The expression "x and y" first evaluates *x*; if *x* is false, its
value is returned; otherwise, *y* is evaluated and the resulting value
is returned.

The expression "x or y" first evaluates *x*; if *x* is true, its value
is returned; otherwise, *y* is evaluated and the resulting value is
returned.

Note that neither "and" nor "or" restrict the value and type they
return to "False" and "True", but rather return the last evaluated
argument.  This is sometimes useful, e.g., if "s" is a string that
should be replaced by a default value if it is empty, the expression
"s or 'foo'" yields the desired value.  Because "not" has to create a
new value, it returns a boolean value regardless of the type of its
argument (for example, "not 'foo'" produces "False" rather than "''".)

Related help topics: EXPRESSIONS, TRUTHVALUE

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> *x*
SyntaxError: invalid syntax
>>> ~~0
0
>>> ~1
-2
>>> not 1
False
>>> not 0
True
>>> not not true
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    not not true
NameError: name 'true' is not defined
>>> not not True
True
>>> not not not true
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    not not not true
NameError: name 'true' is not defined
>>> not not not True
False
>>> 1 and 0
0
>>> 1 and 1
1
>>> 1 and 0
0
>>> 0 and 1
0
>>> 0 or 1
1
>>> 1 or 1
1
>>> 1 or 0
1
>>> 1 or 1
1
>>> 0 or 0
0
>>> 0 ^ 0
0
>>> 1 ^ 0
1
>>> 0 ^ 1
1
>>> 1 ^ 1
0
>>> 0!
SyntaxError: invalid syntax
>>> 0 and 0 and 0
0
>>> 0 or 0 or 0
0
>>> 0 and 0 and 0 or 0
0
>>> 0 or 1 and 1 or 1
1
>>> 0 ^ 1 & 1 | 0
1
>>> a=23
>>> type(a)
<class 'int'>
>>> id(a)
2901060709360
>>> x=34
>>> y=67
>>> temp=""
>>> temp=X
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    temp=X
NameError: name 'X' is not defined
>>> temp=x
>>> x=y
>>> y=temp
>>> x
67
>>> y
34
>>> x,y=y,x
>>> x
34
>>> y
67
>>> a="sliceing"
>>> len(a)
8
>>> a[1]
'l'
>>> a[7]
'g'
>>> a[0:8]
'sliceing'
>>> a[5:8]
'ing'
>>> a[::]
'sliceing'
>>> a[::-2]
'gicl'
>>> x=input("the age of the person")
the age of the person45
>>> x
'45'
>>> x=int(input("the age relaxation"))
the age relaxation2
>>> x
2
>>> x=int(input("""the age1
the age2"""))
the age1
the age245
>>> x
45
>>> x=56
>>> y=45
>>> x<y
False
>>> x>y
True
>>> x>=y
True
>>> x<=y
False
>>> x!=y
True
>>> x==y
False
>>> x+=2
>>> x
58
>>> txt="the universe is{:,} years old"
>>> print(txt.format(1300000000000))
the universe is1,300,000,000,000 years old
>>> xTrue
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    xTrue
NameError: name 'xTrue' is not defined
>>> 1 and 0
0
>>> true and false
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    true and false
NameError: name 'true' is not defined
>>> True and False
False
>>> 1&1
1
>>> 0|0
0
>>> 0|1
1
>>> 1 or 1
1
>>> True or False
True
>>> not not not false
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    not not not false
NameError: name 'false' is not defined
>>> not not not False
True
>>> not not true
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    not not true
NameError: name 'true' is not defined
>>> not not True
True
>>> 0^0
0
>>> 0^1
1
>>> True^ True
False
>>> True^False
True
>>> False^False
False
>>> 1^1
0
>>> not not True
True
>>> 1 and 1
1
>>> 0 or 1
1
>>> 0|0
0
>>> 0|1
1
>>> 1^1
0
>>> 1|0
1
>>> 1^0
1
>>> 1
1
>>> not not not False
True
>>> not not True
True
>>> not False
True
>>> 1 or 0
1
>>> 0 or 0
0
>>> 0 or 1
1
>>> 1 or 1
1
>>> 1|0
1
>>> 1|1
1
>>> True and True
True
>>> True or False
True
>>> False or False
False
>>> x=int(input("enter the number1"))
enter the number123
>>> y=int(input("enter the number2"))
enter the number243
>>> x+y
66
>>> x-y
-20
>>> x="""the input is given in
the specification for
usage of users"""
>>> x
'the input is given in\nthe specification for\nusage of users'
>>> y="the input is given"
>>> x+y
'the input is given in\nthe specification for\nusage of usersthe input is given'
>>> x=56
>>> y=67
>>> x,y=y,x
>>> x,y
(67, 56)
>>> x=567,y=789
SyntaxError: cannot assign to literal
>>> x,y=567,789
>>> x<y
True
>>> x>y
False
>>> x<=
SyntaxError: invalid syntax
>>> x<=y
True
>>> x>=y
False
>>> x!=y
True
>>> x==y
False
>>> x<=y
True
>>> x+=2
>>> x
569
>>> 56/67
0.835820895522388
>>> 56//67
0
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

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> CLASSES

help> ELLIPSIS
The Ellipsis Object
*******************

This object is commonly used by slicing (see Slicings).  It supports
no special operations.  There is exactly one ellipsis object, named
"Ellipsis" (a built-in name).  "type(Ellipsis)()" produces the
"Ellipsis" singleton.

It is written as "Ellipsis" or "...".

Related help topics: SLICINGS

help> UNARY
Unary arithmetic and bitwise operations
***************************************

All unary arithmetic and bitwise operations have the same priority:

   u_expr ::= power | "-" u_expr | "+" u_expr | "~" u_expr

The unary "-" (minus) operator yields the negation of its numeric
argument.

The unary "+" (plus) operator yields its numeric argument unchanged.

The unary "~" (invert) operator yields the bitwise inversion of its
integer argument.  The bitwise inversion of "x" is defined as
"-(x+1)".  It only applies to integral numbers.

In all three cases, if the argument does not have the proper type, a
"TypeError" exception is raised.

Related help topics: EXPRESSIONS

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> x=complex(input())
7i+4j
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    x=complex(input())
ValueError: complex() arg is a malformed string
>>> x=complex(input())
3j
>>> x
3j
>>> x=int(input())
8%3
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    x=int(input())
ValueError: invalid literal for int() with base 10: '8%3'
>>> 8%3
2
>>> float=8%3
>>> 
>>> float
2
>>> num=3
>>> if num>0
SyntaxError: invalid syntax
>>> if num>0:
	print(num,"is a positive number")

	
3 is a positive number
>>> x=int(input("enter the number:"))
enter the number:78
>>> if num>0
SyntaxError: invalid syntax
>>> if num>0:
	print("num is a positive number")

	
num is a positive number
>>> num=45
>>> if num>=0
SyntaxError: invalid syntax
>>> if num>=0:
	print("positive number")

	
positive number
>>> if num<=0:
	print("positive number")
	else
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> else :
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if num<=0:
	print("positive number")

	
>>> else num>=0:
	
SyntaxError: invalid syntax
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

help> LOOPING

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

help> else
The "if" statement
******************

The "if" statement is used for conditional execution:

   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section Boolean operations
for the definition of true and false); then that suite is executed
(and no other part of the "if" statement is executed or evaluated).
If all expressions are false, the suite of the "else" clause, if
present, is executed.

Related help topics: while, for

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> else:
	
SyntaxError: invalid syntax
>>> "else"
'else'
>>> print("negative number")
negative number
>>> if num=0
SyntaxError: invalid syntax
>>> if num=0:
	
SyntaxError: invalid syntax
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

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> if num==0:
	print("zero")
	else if num>0:
		
SyntaxError: invalid syntax
>>> elif
SyntaxError: invalid syntax
>>> elif num>0:
	
SyntaxError: invalid syntax
>>> n=12
>>> sum=0
>>> i=1
>>> while i<=n
SyntaxError: invalid syntax
>>> while i<=n:
	sum=sum+i
	i=i+1

	
>>> print("the sum is",sum)
the sum is 78
>>> counter =0
>>> while counter<3
SyntaxError: invalid syntax
>>> while counter<3:
	print("inside loop")
	counter=counter+1

	
inside loop
inside loop
inside loop
>>> else
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> print("and truth table")
and truth table
>>> False and True|0 0r 1
SyntaxError: invalid syntax
>>> NAND(False,False)
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    NAND(False,False)
NameError: name 'NAND' is not defined
>>> False NAND False
SyntaxError: invalid syntax
>>> It selects exactly one of the suites by evaluating the expressions one
SyntaxError: invalid syntax
>>> 
>>> 
>>> 0 and 1
0
>>> 0 and 0
0
>>> True and True
True
>>> True or True
True
>>> True ^ True
False
>>> True ^ False | True
True
>>> True ^ False | False and True ^ True
False
>>> 0&1^1|1
1
>>> x,y=0,1
>>> x|y^y&x^x
1
>>> x>y
False
>>> x<=y
True
>>> x>=y
False
>>> x!=y
True
>>> x==y
False
>>> 1 is 1
True
>>> 1 is 0
False
>>> rare is rare
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    rare is rare
NameError: name 'rare' is not defined
>>> gt in acgtta
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    gt in acgtta
NameError: name 'gt' is not defined
>>> "rare" is "rare"
True
>>> "gt" in "acgtta"
True
>>> a ==b
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    a ==b
NameError: name 'b' is not defined
>>> a==34
False
>>> b=""
>>> b==a
False
>>> a
'sliceing'
>>> anteaters<ant
Traceback (most recent call last):
  File "<pyshell#301>", line 1, in <module>
    anteaters<ant
NameError: name 'anteaters' is not defined
>>> False
False
>>> a="anteater"
>>> b="ant"
>>> len(a)
8
>>> len(b)
3
>>> len(a)<len(b)
False
>>> a<b
False
>>> a[0]=a[1]
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    a[0]=a[1]
TypeError: 'str' object does not support item assignment
>>> a>b
True
>>> a+b
'anteaterant'
>>> a,b="anteater","ant"
>>> a>b
True
>>> a,b="ads,efg"
Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    a,b="ads,efg"
ValueError: too many values to unpack (expected 2)
>>> a="ads","efg"
>>> a,b="ads","efg"
>>> a==b
False
>>> a<b
True
>>> a>b
False
>>> 
>>> 
>>> a,b=0,1
>>> if (a&b=True)
SyntaxError: invalid syntax
>>> if (a&b=True):
	
SyntaxError: invalid syntax
>>> a&b
0
>>> a|b
1
>>> a^b
1
>>> a|b
1
>>> a||b
SyntaxError: invalid syntax
>>> a|b
1
>>> 0&1|1&0^1^0|0
>>> 
>>> 
>>>
