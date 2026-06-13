'''
built-in functions
------------------------
1.print()
2.input()
3.len()
4.type()
5.max()
6.min()

m=[3,4,6,2]
m.sort()
print(m)

recursive functions:a recursive fun that calls itself to solve a problem by breaking it into small or simple sub problem
--------------------
eg:
def fac(num):
    if num == 1:
        return 1
    return num*fac(num-1)
print(fac(5))

return: this end a function execution and sends a value back to the code that called the function
-------------
eg:
def add(a,b):
    return a+b
res=add(4,5)
print(res)

lambda function: a lambda function is a small anonamus functions
----------> lambda can take n number of arguments, but only one expressions
syntax---->lambda arguments:expression
------------------
eg:  
so=lambda a,b,c:a+b+c+a
print(so(3,4,9))

