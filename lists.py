#To Create list by taking input from user
'''l=list(map(int,input().split()))
print(l)'''

#To insert element at specific index of list
'''l=list(map(int,input().split()))
l.insert(2,80)
print(l)'''



#To merge two lists into single list
'''l1=[10,20,30,40,50]
l2=[60,70]
l1.extend(l2)
print(l1)'''

#to remove specific element from a list
'''l=[10,20,30,40,50]
l.remove(50)
print(l)'''


#   To remove an element using index from list
'''l=[10,20,30,40,50,60]
l.remove(l[0])
print(l)'''


#index of given element in the list
'''l=[10,20,30,40,50,60]
key=30
for i in l:
    if key==i:
        print(l.index(key))'''


#To count number of occurrences from the list
'''l=[10,20,30,30,40,50,30]
key=30
c=0
for i in l:
    if key==i:
        c+=1
print(c)'''


#To print sum of first and last elements from the list
'''[l=[10,20,30,40,50,60]
print(l[0]+l[-1])'''



#To calculate sum of list elements upto given index
'''l=[10,20,30,40,50]
sum=0
for i in range(0,len(l)):
    sum+=l[i]
print(sum)'''


#To Calculate Average of Odd numbers in the list
'''l=[2,3,5,7,11,13,15,17,19,21]
sum=0
for i in range(0,len(l)):
    if l[i]%2==1:
        sum+=l[i]
print(sum)'''


#To print all prime numbers present in the list
'''l=[10,11,12,13,14,15,16,17,18]
import math
for i in l:
    fc=0
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            fc+=1
    if fc==0:
        print(i)'''


#To print next prime number for each element in the list
'''l=[10,11,13,18,21,26]
c=0
import math
for i in l:
    p=i+1
    while True:
        fc=0
        for j in range(2,int(math.sqrt(p)+1)):
            if p%j==0:
                fc+=1
        if fc==0:
            print(p)
            break
        p+=1'''


#To print  the list in the reverse order
'''l=[10,20,30,40,50,60]
for i in range(len(l)-1,-1,-1):
    print(l[i])'''


#To find sum of any two elements is equal to key value
'''l=[10,2,18,14,6,12]
target=20
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(l[i],l[j])'''

#largest number in the list
'''l=[11,12,13,14,22,34,45]
max=-(10^6)
for i in range(0,len(l)):
    if l[i]>max:
        max=l[i]
print(max)'''

#second largest number in the list
'''l=[10,20,30,45,39,62]
max1=max2=-(10^6)
for i in range(0,len(l)):
    if l[i]>max1:
        max1=l[i]
for j in range(0,len(l)):
    if l[j]>max2 and l[j]<max1:
        max2=l[i]
print(max2)'''

#third largest number in the list
'''l=[12,23,34,57,76,82]
max1=-10^6
for i in range(0,len(l)):
    if l[i]>max1:
        max1=l[i]
max2=-10^6
for j in range(0,len(l)):
    if l[j]>max2  and l[j]<max1:
        max2=l[j]
max3=-10^6
for k in range(0,len(l)):
    if l[k]>max3 and l[k]<max2 and l[k]<max1:
        max3=l[k]
print(max1,max2,max3)'''


#To Sort list without using any built-in sorting functions
'''l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)'''

#To find Nth largest element in a list
'''l=list(map(int,input().split()))
n=int(input())
l.sort()
print(l[-n])'''


#to print smallest missing elements in list
'''l=[6,10,15,14,82]
m=min(l)
c=0
while c<4:
    if m not in l:
        print(m)
        c+=1
    m+=1'''


#To perform linear Search on a list
'''l=[2,4,5,20,43,20,48,20]
l.sort()
print(l)
key=20
for i in range(0,len(l)):
    if key==l[i]:
        print(i)'''




#To print Binary Search on a sorted list
'''l=list(map(int,input().split()))
key=int(input())
s=0
e=len(l)-1
while s<=e:
    mid=s+e//2
    if key==l[mid]:
        print(key)
        break
    elif l[mid]>key:
        e=mid-1
    else:
        s=mid+1
if s>e:
    print("not found")'''


#To return all index positions of a searched element in a list
'''l=list(map(int,input().split()))
key=int(input())
for i in range(0,len(l)):
    if key==l[i]:
        print(i)'''

# To check the list is sorted or not
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
        if l[i]>l[i+1]:
            print(" Not Sorted list")
            break
else:
    print("Sorted")'''



#To print LCM of all Numbers in the list
'''l=list(map(int,input().split()))
m=max(l)
mul=m
while True:
        for i in range(0,len(l)):
                if not mul%l[i]==0:
                        mul+=m
                        break
        else:
                print(mul)
                break'''


#to find GCD in the given list
'''l=list(map(int,input().split()))
m=min(l)
fa=m
while True:
        for i in range(0,len(l)):
                if not l[i]%fa==0:
                        fa+=m
                        break
        else:
                print(fa)
                break'''


#To find factorial of each element in the list
'''l=[3,7,6,9]
for i in range(0,len(l)):
        fact=1
        for j in range(1,i+1):
                fact=fact*l[j]
        print(fact)'''


#frequency
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
        c=0
        for j in range(0,len(l)):
                if l[i]==l[j]:
                        c+=1
        print(l[i],c)'''

#to calculate backward frequency of elements in a list
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
        c=0
        for j in range(0,i+1):
                if l[i]==l[j]:
                        c+=1
        print(l[i],c)'''

#to print frequency of each element without repetition
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
        oc,bc=0,0
        for j in range(0,len(l)):
                if l[i]==l[j]:
                        oc+=1
        for j in range(0,i+1):
                if l[i]==l[j]:
                        bc+=1
        if bc==1:
                print(l[i],oc)'''


#to find most frequently repeated element in a list
'''l=list(map(int,input().split()))
maxc,maxele=0,0
for i in range(0,len(l)):
    oc=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            oc+=1
    if oc>maxc:
        maxc=oc
        maxele=l[i]
print(maxele)'''


#To find Unique element in a list
''''=list(map(int,input().split()))
for i in range(0,len(l)):
    c=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            c+=1
    if c==1:
        print(l[i])'''


#To  find the least unique element in a list
'''l=list(map(int,input().split()))
luniq=10^6
for i in range(0,len(l)):
    oc=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            oc+=1
    if oc==1 and l[i]<luniq:
        luniq=l[i]
print(luniq)'''



# To print greater  than 1 element in the list
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
    oc,bc=0,0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            oc+=1
    if oc>1:
        for j in range(0,i+1):
            if l[i]==l[j]:
                bc+=1
        if bc==1:
            print(l[i])'''

# To rotate a list in clockwise direction
'''l=list(map(int,input().split()))
for i in  range(0,len(l)):
    t=l.pop(0)
    l.append(t)
    print(l)'''

#To print all rotations of a list
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
    t=l.pop()
    l.insert(0,t)
    print(l)'''

#To rotate a list by k positions(anti clock)
'''l=list(map(int,input().split()))
k=int(input())
for i in range(0,k):
    t=l[len(l)-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0]=t
print(l)'''


#To find sublists of given list
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(i,j+1):
            print(l[k],end=" ")
        print()'''


#Sublists along with sum which is equal to key
'''l=list(map(int,input().split()))
key=int(input())
for i in range(0,len(l)):
    for j in range(i,len(l)):
        sum=0
        res=[]
        for k in range(i,j+1):
            res.append(l[k])
            sum=sum+l[k]
        if sum==key:
            print(res)'''

#write a program to convert a list  of digits into a number
'''l=list(map(int,input().split()))
num=0
for i in l:
    num=num*10+i
print(num)'''


#write a program to convert a number into a list of digits
'''num=int(input())
while num!=0:
    r=num%10
    num=num//10
    print(r,end=" ")'''

#Write a program to reverse a list  and also reverse each element in the list
'''l=list(map(int,input().split()))
for i in l[::-1]:
    print(str(i)[::-1],end=" ")'''


'''import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
        return True
n=int(input())
i=n
c=0
f=0
while i>0:
    r=i%10
    i=i//10
    c+=1
n=i
while c>0:
    r=i%10
    i=i//10
    i=int(str(r)+str(i))
    if is_prime(i)==False:
        f=1
    c-=1
if f==0:
    print("pointer prime")'''


'''l1=[10,20,10,30,30,30,10,30,40]
l2=[30,10,40,10,10,10,30,50]
l1.sort()
l2.sort()
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            print(l1[i])'''




