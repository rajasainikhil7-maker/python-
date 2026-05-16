'''
operators
-------------
arithmetic operator
'''
a=2
b=5
print(b+a)
print(b-a)
print(a*b)
print(b/a)

'''Assignment operator'''
c=a+b
d=b-a
e=a*b
print(c)
print(d)
print(e)

'''comparison operator'''
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=0)

'''identity operator'''
a1=15
b1=30
print(a1 is b1)
print(a1 is not b1)

'''membership operator'''
arr=[1,2,3,4,5,6]
print(b in arr)
print(a not in arr)

'''logical operator'''
if a==b and b!=a:
    print("true")
if a==b  or b!=a:
    print("true")

'''bitwise operator'''
print(a&b)
print(a|b)
print(a^b)
print(~a)

'''string'''
str1="welcome to the world"
print(str1.split())
print(str1.replace("world","city"))
print(len(str1))
print(str1[0:10])

