Tuple.py

Tuple - ()

t = 12345, 54321, 'hello!'
t[0]

x = list(t)
x[0] = 1000
t = tuple(x)
t
(1000, 54321, 'hello!')


#tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

#tuples are immutable:
t[0] = 88888

#but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v



fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#change tuple values

x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "mango"
x = tuple(y)
x