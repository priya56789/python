#To find length of string
'''s="hii priyanka"
st=len(s)
print(st)
s=input()
print(len(s))'''

#to display ASCII value of given string
'''s=input()
for i in s:
    print(ord(i))'''

#To convert a string into uppercase
'''s="I love you"
st=s.upper()
print(st)'''

#To convert string into Lowercase
'''s="MOM AND DAD"
st=s.lower()
print(st)'''

#To replace all places of string with hyphens
'''s="Hii I am going to Vizag"
print(s.replace(" ","-"))'''


#To check whether a string contains only digits
'''s=input()
print(s.isdigit())'''


#To check whether a string contains only alphabets using isalpha()
'''s=input()
print(s.isalpha())'''


#To check whether a string is alphanumeric using isalnum()
'''s=input()
print(s.isalnum())'''


#To validate an Aadhar number based on its length and digit rules
'''s=input()
if len(s)==12:
    print("Valid")
else:
    print("not valid")'''



#To validate a PAN Card using its format rules
#s=input()




# To validate a Gmail ID
'''gmail=input()
if gmail.endswith(".com") and gmail.lower():
    print("satisfied:",gmail)
else:
    print("incorrect gmail")'''



#To validate a password based on length,uppercase,lowercase,digit
'''ch=input()
if ch>="A" and ch<="Z":
    print(ch,"is an uppercase letter")
elif ch>="a" and ch<="z":
    print(ch,"is an lowercase letter")
elif ch>=0 and ch<=9:
    print(ch,"is a digit")
else:
    print(ch,"is a character")'''


s="123456"
s1=s[0:3]
s2=s[3:7]
print(s1+s2)
for i  in range(len(s),0,-1):
    print(i,end="")
print()
s1=s[2:0:-1]
s2=s[7:2:-1]
print(s1)
print(s2)
