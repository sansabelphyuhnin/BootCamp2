def say_hello():
	print('Hello World')


say_hello()

# >>> def say_hello():
# ...     print("Hello World")
# ...
# >>>
# >>> def cal():
# ...     x = 1
# ...     y = 2
# ...     z = x + y
# ...     print(z)
# ...
# >>> cal()
# 3


#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maxium')
	elif a == b:
		print(a, 'is equal to',b)
	else:
		print(b, 'is maxium')

print_max(5,8)
print_max(10,10)

print_max(3,4)

x = 8
y = 11

print_max(x,y)

# Local Variables

def func(x):
	print('x is',x)
	x = 2
	print('Change local x to',x)

x = 50
func(x)
print('x is still', x)

x = 30
def func(x):
	x = 2

def funx(x):
	x = 10


func(x)
funx(x)
x
func(x) + funx(x)

#Global statement

def func():
	global x

	print('x is', x)
	x = 2
	print('Change global x to',x)

# x = 50
# func()
# print('')



def say(message, times=1):
	print(message * times)

say('Hello')
say('World', s)
say('Good Bye')

# Keyword argument

def func(a, b=s, c=10):
	print('a is',a,'and b is',b, 'and c is',c)

func(3,8)
func(24, c=26)
func(c=29,a=39)


# VarArgs permeters
# function_VerArgs.py

def total(a=5, *numbers, **phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)
	
	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)
total(10,123, 1121, 32, 5, 45,Jack=1123,Inge=1459,Joe=2830)
# Return statement


def maxium(x,y):
	if x > y:
		return x
	elif x == y;
		return 'The numbers are equal'
	else:
		return y


print(maxium(3,8))

print(maxium(20,10))

# docString(Documentation strings)


def print_max(x,y):
	'''Prints the maximum of two numbers
	The two values must be integer
	'''


	x = int(x)
	y = int(y)

	if x > y:
		print(x,'is maxium')

	elif x < y:
		print(y,'is maxium')
	else:
		print(x,'&',y,'is equal')

print_max(5,9)

print(print_max.__doc__)


def paper():
	'''1. There will be situtations where your 
	program has to interact with the user.
	For example, you would want to take input
	from the user and then print some results
	back. We can achieve  this using input()
	function and print function respectively.'''
	
	'''2. There will be situtations where your 
	program has to interact with the user.
	For example, you would want to take input
	from the user and then print some results
	back. We can achieve  this using input()
	function and print function respectively.'''

print(paper.__doc__)