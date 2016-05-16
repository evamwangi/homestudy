import time

def sum_of_n2(n):
	start = time.time()

	theSum = 0
	for i in range(1 , n+1):
		theSum += i
	end = time.time()

	return theSum , end-start

print sum_of_n2(1000)