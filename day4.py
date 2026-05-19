'''concatination'''
a=90
b=80
print(a+b)
any="python"
so="is a language"
print(any+so)
an=[1,2]
am=[3,4]
print(an+am)

'''count'''
so=(1,"python",[1,2],[3,4],"python")
print(so.count("python"))

'''index'''
some=(1,[1,2],(3,4),"python")
print(some.index("python"))

'''dictionary'''
teja_details={"name":"teja",1:2,(1,2):[3,4]}
print(type(teja_details))

'''keys'''
teja_details={"name":"teja",
              "age":45,
              "phno":"12345678",
              "pan":"rsn3tfhdeh"}
print(teja_details.keys())

'''items'''
teja_details={"name":"teja",
              "age":45,
              "phno":"12345678",
              "pan":"rsn3tfhdeh"}
print(teja_details.items())

'''update'''
teja_details={"name":"teja",
              "age":45,
              "phno":"12345678",
              "pan":"rsn3tfhdeh"}
teja_details.update({"adhar":23456789})
print(teja_details)
teja_details["asdfg"]=4578
print(teja_details)
teja_details.clear()
print(teja_details)

