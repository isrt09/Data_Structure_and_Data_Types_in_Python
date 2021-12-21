# Map, Filter, and Lambda Functional Workflow

l = [10,20,30,40,50]

def sqr(value):
	return value ** 2

result = map(sqr,l)
print(result)

for value in l:
	print(value)

result = list(map(sqr,l))
print(result)

m = [sqr(value) for value in l]
print(m)


p = [100,200,300,400,500]
q = [10,20,30,40,50]

def add(x,y):
	return x + y

result = list(map(add,p,q))
print(result)

u = [100,115,120,125,130,140]
def check_num(value):
	if value % 2 == 0:
		return True
	else:
		return False

result = list(filter(check_num,u))
print(result)

result = list(map(check_num,u))
print(result)

v = [10,20,30,40,50]

result = list(map(lambda num: num * 2,v))
print(result)

def multiple(value):
	return value * value

# (lambda value: value * value, z)

z = [10,20,30,40,50]

result = list(map(multiple,z))
score = list(map(lambda value: value * value, z))
print(score)
print(result)

a = [10,13,15,18,20,23,25,24,26,30,32,15,36,38,40,39]
b = [ value for value in a if value % 2 == 0]
c = []

for value in a:
	if value % 2 == 0:
		c.append(value)


def even(value):
	if value % 2 == 0:
		return value

m1  = list(map(even,a))
m2  = list(map(lambda even:even % 2 == 0, a))
f1  = list(filter(even,a))
f2  = list(filter(lambda even:even % 2 == 0, a))

print(c)  # Traditional Method
print(b)  # List Comprehension
print(f1) # Filter Method
print(f2) # Lambda Method
print(m1) # Map Function
print(m2) # Map Function


d = {1:50, 2:40, 3:30,4:20,5:10}
e = sorted(d.items())
f = sorted(d.items(), key = lambda x: x[1] )
g = dict(sorted(d.items(), key = lambda x: x[1] ))
print(d)
print(e)
print(f)
print(g)