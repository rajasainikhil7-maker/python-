any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2])
print(any[2][3])
print(any[4][1])


any=[1,2,3,4]
any.append(7)
print(any)
any.append([20,30,60])
print(any)
any.append(10)
print(any)

arr=[2345,56,456,56,9]
arr.extend("python")
print(arr)
arr.extend([1,2,3,4])
print(arr)

any=[1,2,3,"python"]
any.pop(3)
print(any)

arr=[1,2,3,4,5]
arr.remove(3)
print(arr)
