
# Iteration & Generators
def score(num):
	for value in num:
		print(value)

l = [10,20,30,40,50,60]

score(l)

def demo():
	first_number  = 0
	second_number = 1
	yield second_number
	while(True):
		next_number = first_number + second_number
		yield next_number
		first_number,second_number = second_number,next_number

result = demo()
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for value in range(10):
	print(next(result))

def getValue(p):
	for item in p:
		yield item

p = [10,20,30,40,50]

q = getValue(p)
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))

u = [10,20,30,40,50]
v = (value * value for value in u)
print(v)
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))