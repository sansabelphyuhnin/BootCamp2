# Create FileInputOutput into Python Code
# save as Open.py in FileInputOutput


# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

# Open & Read File

# f = open('test.txt', 'r')	# R - Read
# print(f.name)
# f.close()


# with open('test.txt', 'a') as f:

# 	f.write('This is line number '+"\n")

# 	print(f,end='')


with open('test.txt', 'r') as f:

	# f_next = f.readline()
	# print(f_next,end='')

# This answer is for Line1 but 
# there will not be the two line for Line1 
# cuz overerite from the programming of the below one.

	# for f_next in f:
	# 	print(f_next,end='')

# 	f_next = f.readline()
# 	print(f_next,end=' ')

# 	f_next = f.readline()
# 	print(f_next,end=' ')

# 	f_next = f.readline()
# 	print(f_next,end=' ')

# .read() can be the word count 

	f_next = f.read(60)
	print(f_next,end=' ')

# 	f_next = f.read(100)

# 	while 100 > 0:
# 		print(f_text,end=' ')