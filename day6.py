'''type conversions'''
a=789
b=str(a)
print(type(b))
c=float(a)
print(type(c))
#----------------------
s=345
m=float(s)
print(type(m))
#----------------------
an="567"
am=tuple(an)
print(type(am))
#----------------------
f1=583.34
f2=int(f1)
print(type(f2))
#----------------------
'''num=int(input("enter a number "))
print(num)

string=input("enter a text")
print(string)
#----------------------'''
'''list1=list(map(int,input("enter numbers:").split()))
print(list1)
#--------------------------
any=list(map(str,input("enter a list:").split()))
print(any)
#------------------------'''
an=tuple(map(int,input("enter numbers:").split()))
print(an)
