Set&Dictionaries.py

Set - {}

includes a data type for sets
Curly braces or the set() function can be used to create sets.


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} 
print(basket)  # show that duplicates have been removed


'orange' in basket    # fast membership testing
'crabgrass' in basket
true or false (boolaun)

Demonstrate sets operations on unique letters from two words


a = set('abracadabra')
b = set('alacazam')

a       # unique letters in a 
a - b   #  letters in a but not in b
a | b   # letters in a or b or both
a & b   # letters in both a and b 
a ^ b   # letters in a or b but not both


a = {x for x in 'abracadabra' if x not in 'abc'}
a



fruits = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'}
print("cherry" in fruits)


fruits.add("cucumber")
fruits
fruits.update("grape") x
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits




Dictionaries

#Another useful data type built into python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel


-----------------------

del tel['sape']
tel['irv'] = 4137
tel

list(tel)	# Change the list

sorted(student)	#Alphabet sorting

'MgOo' in student

'MaMa' not in student



-----------------------

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

(x: x**2 for x in (2, 4, 6))

for x in 2, 4, 6:
	print(x, ':' ,x**2)

2 : 4
4: 15
6 : 36


for x in 2, 4, 6:
	print(x,':',x**2)


--------------------------


When looping through Dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape': 4355}
for x,y in knights.items():
	print(x,y)


for x,y in enumerate(['tic', 'tac', 'toe']):
	print(x,y)


-----------------------


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

#sum

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
result = ['1','2','3']
for q, a in zip(questions, answers, result):
	print('What is your {0}? It is {1}.It is {2}'.format(q, a, 1))


-------------------------------

print('{0} and {1} , {2} and {3}'.format('spam', 'egg', 'color', 'food'))

