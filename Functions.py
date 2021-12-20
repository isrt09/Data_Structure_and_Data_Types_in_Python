import random

def gen_password(length=8):
	l = ['@','#','$','&']
	upper   = chr(random.randint(65,90))
	lower   = chr(random.randint(97,112))
	special = random.choice(l)
	digits  = random.randint(1000,9999)
	password= upper + lower + special + str(digits)
	l = random.sample(password, length)
	password = ("").join(l)
	return password

result = gen_password(7)
print(result)

# Keyword Argument
def validate(username,password):
	if username == "ABC" and password == "abc@123":
		print("Valid Password")
	else:
		print("InValid Password")


validate("abc123","ABC123")
validate("ABC","abc@123")
validate(username="ABC",password="abc@123")
help(print)
print(100,200)
print(100,200,sep=",",end=" ")
print("Hello Mazed")

# Propositional Argument
def greetings(name,value):
	print("Hello! "+ name +" Happy New Year "+ value)

greetings('Mazed', '2022')
greetings('Mizan', '2022')
greetings('Mafuz', '2022')


def value_reverse(value):
	reverse = value[::-1]
	return reverse

p = "Django Framework"
result = value_reverse(p)
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