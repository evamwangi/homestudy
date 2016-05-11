i = 0
a = [2,3,4,5,6,8,7,64,2,34,6,77,89]
while i < len(a):
	print a[i]
	i = i + 3
print "the length of the list is:" 
print len(a)
print "============================="
print "appending to a list"
a.append(123)
print a
print "============================="
print "inserting an element"
a.insert(7,156)
print a
print "============================="
a.reverse()
print a
print "============================="
a.sort()
print a
a.remove(2)
print a
a.remove(6)
print a



	