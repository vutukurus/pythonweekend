#deep copy..

a = [10,20,30,90,100]

b = [50,60,70]

a = b[:] #deep copy...different memory..


b[0] = 100


print a #50,60,70
print b #100,60,70