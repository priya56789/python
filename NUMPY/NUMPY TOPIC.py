'''import numpy as np
#import pandas as pd

print("Numpy")
list_a=list((map(int,input().split())))

a=np.array(list_a)
print(a)
print()

b=np.zeros((2,2))
print(b)
print()

z=np.ones((2,2),dtype=bool)
print(z)
print()

c=np.full((2,2),2)
print(c)
print()


d=np.eye(4)
print(d)
print()


e=np.arange(0,10,2)
print(e)
print()

f=np.arange(6)
print(f)
print()

g=np.linspace(0,1,4)
#This generates numbers in between 0 and 1 as given size or evenly separated values
print(g)
print()

h=np.random.rand(2,2)
print(h)
print()

i=np.random.randint(1,10,(2,2))
print(i)
print()


print(a.shape,a.ndim,a.dtype,a.size)
print()

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print()


#0 serial number lo 1st index values as o/p
print(arr[0,1])
print()


#return values according to column given
print(arr[:,2])
print()


x=np.arange(6)
print(x.reshape(2,3))
print(x.flatten())


#METHODS
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)
print()
print(np.dot(a,b))
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))

arr=np.array([[1,2,30],[4,8,6]])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))#index number of minimum value
print(np.argmax(arr))#index number of maximum value



arr=np.array([[1,2],[3,4]])
print(arr+10)
print()

arr=np.array([1,2,3,4,5])
print(arr[arr>3])
print()

a=np.array([1,2])
b=np.array([4,5])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

print(np.split(np.array([1,2,3,4]),2))

#print(np.split(np.array([1,2,3,4]),2))

mat=np.array([[1,2],[3,4]])
print(np.linalg.inv(mat))
print(np.linalg.det(mat))
print(np.linalg.eig(mat))'''
















