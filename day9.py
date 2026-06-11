'''
----------

num=int(input())
for i in range(1,11):
    print(num,"*",i,"=",num*i)

so=input("enter a word:")
empty_str=""
for j in so:
    empty_str=j+empty_str
if empty_str==so:
    print("Is a palindrome")
else:
    print("NOT a palindrome")

num=int(input("enter a number:"))
n=num
s=0
length_ =len(str(num))
while n>0:
    mod=n%10
    s+=mod**length_
    n//=10
if num==s:
    print("amstrong")
else:
    print("not a amstrong")


num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("is a prime")
else:
    print("is not a prime")


star_=5
for g in range(1,star_+1):
    for j in range(1,g+1):
        print("*",end="")
    print()


star_=5
count=0
for g in range(1,star_+1):
    for j in range(1,g+1):
        count+=1
        print(count,end="")
    print()


num=5
for i in range(1,num+1):
    print(""*(num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
