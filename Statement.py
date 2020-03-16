int(input("Exmanination Result:"))
100 - 90	- A
90 - 70		- B 
70 - 60		- C 
60 - 40		- D 
40 - 0		- Fail

39
70
0
90
103
0.1

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



>>> x = int(input("Examination Result:"))
Examination Result:39
>>> if x > 90:
...     print("A")
... elif x > 70:
...     print("B")
... elif x > 60:
...     print("C")
... elif x > 40:
...     print("D")
... else:
...     print("Fail")
...
Fail