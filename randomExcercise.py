import random
#generates random numbers between 1 and 100 until it hits 100. 
test = 0
while test < 100:
	test = int(random.randint(1, 100))
	print(str(test))
	if test == 100:
		print("it worked!!!")
