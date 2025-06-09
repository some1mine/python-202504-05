import numpy as np 
a = [1,2,3,4,5,6,7,8,9,10]
b = [x*2 for x in a]
c = a+b 
print(a)
print(b)
print(c)

a1 = np.array(a)
b1 = 2 * a1
c1 = a1 + b1  
print(a1)
print(b1)
print(c1)