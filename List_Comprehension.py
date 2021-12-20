
# List Comprehension

p = [100,200,300,400,500]
q = [value * value for value in p]

for value in p:
	q.append(value)
else:
	print(q)

x = [100,200,10,20,30,45,34,24,35,19,17,15]
y = [value for value in x if value % 2 == 0]
z = []
print(y)

for value in x:
	if value % 2 != 0:
		z.append(value)
else:
	print(z)

print(dir(help(list)))

words = ['abc', 'abcd','abcde','abcasdasddef','abadasdcdef','abc', 'abasdascd','abcde','abcdeasdsaf','abadasdcdef']

word_number = [len(value) for value in words]
print(word_number)

a = [ (value1, value2) for value1 in range(1,5) for value2 in range(100,103) ]
print(a)

l = [[1,2,3],[3,4,9],[3,9,5]]
m = []
for value in l:
	print(value)

for value in l:
	for item in value:
		m.append(item)
print(m)

m = [[1,2,3],[3,4,9],[3,9,5]]
n = [item for value in m for item in value]
print(n)

u = [100,103,104,108,110,120,114,119]
v = ["EVEN" if value % 2 ==0 else "ODD" for value in u]
print(v)

