import numpy as np

print np.array([2,3,1,0]) 
print np.array( [ [2,3,1,0], [1,2,3,4] ]) 

print np.zeros((2, 3))
print np.ones((2, 3))

print np.arange(2, 10)
print np.arange(2, 10, dtype=np.float)  
print np.arange(2,5,0.2)

print np.random.random((2,3)) 

print np.linspace(1., 4., 6) 

print np.arange(9).reshape(3,3) 
a = np.arange(6).reshape(2,3) 
print a
print a[1,2]
print a[0,2]

b = np.arange(5)
print b
print b+2

c = np.arange(5)
print b+c

print b.shape
d = np.array( [ [2,3,1,0], [1,2,3,4] ]) 
print d.shape
print d 
e = d.transpose()
print e.shape













