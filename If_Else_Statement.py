If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))



Python Conditions


Equals						-> x == y
Not Equals					-> x != y
Less than					-> x < y
less than or equal to		-> x <= y
Greater than				-> x > y
Greater than or equal to 	-> x >= y
Boolean OR 					-> x or y, x | y
Boolean AND					-> x and y, x & y
Boolean Not					-> not x



#IF statement

x = 70
y = 60

if x > y:
	print("x is greater than y")



x = 10
if x == 0:
	print("x is zero")
elif x != 0:
	print("x is equal to zero")
elif x < 20:
	print("x is 20")
elif x == 10:
	print("x is 10")
else:
	print("x is nothing") 


x = 70
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("Default")



x = 60
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("Default")



x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x ")


if x < y: print("y is greater than x")


x = 50
y = 150
print(x) if x > y else print(y)

#And is logical operator

x = 50
y = 40
z = 100
if  x > y and z > y or x > z:
	print("All Conditions are True")
else:
	print("one coondition is True")

if x > y and y > z or z > x:


x = 50
y = 40
z = 100
if  x > y or z > y:
	print("one of the conditions is True")
elif x > y and z > y:
	print("All conditions are True")
else:
	print("nothing else")


x = 50
if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
		if x > 40 and x < 50 or x == 50:
			print("x is above 40 or equal to 50")
		else:
			print("x is normal")
	else:
		print("No,x is not greater than 20")
else:
	print("x is 50")


x = 15
if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
		if x > 40 and x < 50 or x == 50:
			print("x is above 40 or equal to 50")
		else:
			print("x is normal")
	else:
		print("No,x is not greater than 20")
else:
	print("x is smaller than 10")


x = int(input("Please enter an integer:"))

if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else: 
	print('More')


int(input("Exmanination Result : "))
100 - 90	- A
90 - 70		- B 
70 - 60		- C 
60 - 40		- D 
40 - 0		- Fail