# Recursive Functions

# Power Square
n = 2
def power(num):
	if num == 1:
		print(num)
	else:
		return num * num
result = power(n)
print(result)

# Cubic
m = 2
def power(num):
	if num == 1:
		print(num)
	else:
		return num * num * num
result = power(m)
print(result)

# Factorial

def factorial(value):
	if value == 1:
		return 1
	else:
		return value * factorial(value-1)

num = 5
result = factorial(5)
print(result)


def binary_search(l,key):
	mid = len(l) // 2

	if l[mid] == key:
		return True
	elif key < l[mid]:
		return binary_search(l[:mid],key)
	else:
		return binary_search(l[mid+1:],key)

l = [100,200,300,400,500,600,700,800,900]
key = 300

score = binary_search(l,key)
print(score)