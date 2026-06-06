'''
condition statement
--------------------
if,nested if,elif

num=6
if num%2==0:
    print(num)
if else
-----------------
num=5
if num%2==0:
    print("even")
else:
    print("odd")

if else
num=int(input("enter a number:"))
if num%2!=0:
    print(f"{num}is a even number")
else:
    print(f"{num}is a odd number")

eg:
age_= 20
if age_>=20:
    print("your eligible for vote")
else:
    print("your not eligible for vote {18-age}")

eg:
year_=2025
if (year_%4==0 and year_%100==0):
    print(f"{year_}is a leap year")
else:
    print(f"{year}is not a leap year")

eg:
vowel_="a"
if vowel_ in "AEIOUaeiou":
    print(f"{vowel_}is a vowel")
else:
    print(f"{vowel_}is not a vowel")

eg:
num=1
if num>=0:
    print(f"{num}is a positive number ")
else:
    print(f"{num}is a negative number ")
eg:
marks=int(input("enter your marks:"))
stu_name=input("enter your name:")
if marks>=45:
    print(f"{stu_name} your passed")
else:
    print(f"{stu_name} your failed")

eg:
num=80
if( num%3==0 or num%5==0):
    print(f"{num}is divisible by 3 and 5")
else:
    print(f"{num}is not divisible 3 or 5")


          







    
