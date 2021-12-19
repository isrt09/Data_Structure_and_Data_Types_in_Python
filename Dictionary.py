# Update by Mazedur : 19.12.2021 

# Dictionary :
# mutatable
# unordered
# key unique
# key immutable int str tuple

s = ''
emp = {"id":10102121, "name":"John Smith", "desgination":"Software Engineeer", "salary":25000, "email" : "smith@msn.com"}
print(emp,type(emp))
print(emp['id'])

print("\n",s.center(130,"*"),"\n")

# add new item, update item value
emp['contact_no'] = 1711934200
emp['id'] = 11214521
print(emp)
print(emp.get('name')) # emp[1] not allowed for dictionary data structure
print(emp.get('Age','Not exits here ...'))

print(emp.setdefault('age'))
print(emp)
print(dir(dict))

print("\n",s.center(130,"*"),"\n")

pmp = {"id":10102121, "name":"John Smith", "desgination":"Software Engineeer", "salary":25000, "email" : "smith@msn.com"}
print(pmp,type(pmp))

for (index,value) in enumerate(pmp):
	print(index, value)

print("\n",s.center(130,"*"),"\n")

for index in pmp:
	print(index)

for key in pmp:
	print(key, pmp[key])

print("\n",s.center(130,"*"),"\n")

x = {}

for value in range(1,11):
	x[value] = value * value
else:
	print(x)

for value in range(1,11):
	x[value] = value * value
print(x)

employee = {"id":10102121, "name":"John Smith", "desgination":"Software Engineeer", "salary":25000, "email" : "smith@msn.com"}
print(employee,type(employee))

# Built In Methods
print(employee.keys())
print(employee.values())
print(employee.items())

for x in employee.items():
	print(x)
else:
	print(type(x))