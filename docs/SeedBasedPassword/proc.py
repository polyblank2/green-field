#Procedural Password

import random
##user gives input, like Pizza...
##And a length, it's 19 by default

input_var = input("Enter a String you want the password to be based on [any string, try something simple]: ")
input_len = input("Enter a length you want the password to be [20 is recommended]: ")
input_rep = input("Enter a number of repetitions [must be a number]: ")

random.seed(input_var)
mystr = ''
for i in range(int(input_len)):
	mystr+=chr(random.randint(33,126))




if(int(input_rep) > 1):
	for rep in range(int(input_rep)):
		random.seed(mystr)
		mystr=''
		for i in range(int(input_len)):
			mystr+=chr(random.randint(33,126))
		#print(mystr)

print("FINAL")
print(mystr)


