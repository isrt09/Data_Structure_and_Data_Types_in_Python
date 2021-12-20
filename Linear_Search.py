def linear_search(l, key):
	for value in l:
		if key == value:
			return True
	else:
		return False

l = [100,200,300,400,500]
key = 400

result = linear_search(l, key)
print(result)

l = [10,20,30,40,50]
l.append(70)
print(l)

def value_reverse(value):
	if type(value) == list or type(value) == str:
		score = value[::-1]
		return score
	else:
		tmp = str(value)
		score = tmp[::-1]
		return score

l = [100,200,300,400,500]
result = value_reverse(l)
print(l)
print(result)