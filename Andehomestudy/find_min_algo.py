def find_min(A):
	if len(A) == 0:
		return 'nil'
	else:
		min_ = A[0]
		for i in A:
			if i < min_:
				min_ = i

		return min_

print find_min([45,647,9986,23,65,32,4])
print find_min([])