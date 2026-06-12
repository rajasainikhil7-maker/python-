'''
assert:
----------> this is debugging statements And text whether a condition is true

num=10
assert num > 15
print("True")

functions:
----------------
------> a function is a block of code which only execute when it is called
------>you can pass data, known as parameters into a function
------>to avoid repeated lines in code
ways to pass arguments:
1. required arguments - a required arguments are the parameters that must be given when calling a function
eg:
num=9
def even(num):
    if num%2==0:
        print(f"{num} even")
    else:
        print(f"{num} odd")
even(num)
even(109)
even(107)

2.default arguments:by default values is defined at parameters even through it will take from arguments
eg:
def even(name="teja",age=89,sal=10):
    print(name)
    print(age)
    print(sal)
even("garikapati",89,75000)

3.keyword arguments:we can send arguments with key value syntax by this , order of arguments does not matter
def even(name,age,sal):
    print(name)
    print(age)
    print(sal)
even("garikapati",89,75000)

4. variable length arguments :adding a (*) before the parameters name in the function , recieve a tuple of arguments and can access item with indexes 
def even(*name):
    print(name)
even("karthik","x","jetlee")

quo-prime numbers
eg:'''
def prime_num(num):
    c = 0
    for i in range (2,num+1):
        if num%i==0:
            c+=1
    if c==2:
        print(f"{num} is a prime)")
    else:
        print(f"{num} is not a prime")

prime_num(97)
    
