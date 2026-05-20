'''sets'''
any={1,2,3,3,4}
print(any)

'''union'''
set1={1,2,3,3,4,5,6}
set2={33,34,45,56}
print(set1|set2)
print(set1.union(set2))

'''intersection'''
num1={2,3,3,4,4,5,6}
num2={7,6,3,10,8,2}
print(num1&num2)
print(num1.intersection(num2))

'''difference'''
am={7,8,9,9,10,11}
an={6,8,11}
print(am-an)
print(am.difference(an))

'''add'''
arr={1,2,3,4,5,6,}
arr.add(35)
print(arr)

'''update'''
arr={1,2,3,4,5,6,6,7}
arr.update({35,36,37,38})
print(arr)

'''remove'''
arr={1,2,3,4,5,6,6,7}
arr.remove(6)
print(arr)
