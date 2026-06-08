'''
elif statement
--------------------
eg:
stu_marks=73
if stu_marks >=90:
    print("A+")
elif stu_marks >=80:
    print("A")
elif stu_marks >=70:
    print("B+")
elif stu_marks >=60:
    print("B")
elif stu_marks >=50:
    print("c+")
elif stu_marks >=35:
    print("pass")
else:
    print("fail")

eg:
a=80
b=670
c=890
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)

nested if
----------------------

SBI_bank ={"ATM PIN": "6655"}
pin =input("enter 4 digit ATM PIN:")
if len(pin)==4:
    if pin in SBI_bank["ATM PIN"]:
        print("welcome to SBI bank")
    else:
        print("invalid pin")
else:
        print("enter 4 digit pin")


for loop
--------------------

x="python"
y=[1,2,3,4]
z=[5,6,7,8]
for i in x :
    print(i)


for i in range(0,10):
    print(i)
    if i ==3:
        break

for i in range (1,11):
    if i==6:
        continue
    print(i)

'''
i=1
while i<=5:
    print(i)
    i=i+1


            
