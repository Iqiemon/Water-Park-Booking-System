import math
class Error(Exception):
    """Base class for other exceptions"""
    pass
class InvalidIC(Error):
	"""Raised when the input value is too small"""
	pass
class citizenError(Error):
	"""Raised when the input value is too small"""
	pass
name = str(input("Please enter your name: "))
for i in range(0,100):
			while True:
				try:
					ic = str(input("Please enter your IC number: "))
					if len(ic)<12 or len(ic)>12 :
						raise InvalidIC
				except InvalidIC:
					print("Please enter a valid IC Number!")
					continue
				break
			break
phone = str(input("Please enter your phone number: "))
for i in range(0,100):
			while True:
				try:
					nationality = str(input("Please enter your nationality (Citizen/Non-citizen): "))
					if nationality != "Citizen" and nationality != "Non-citizen":
						raise citizenError
				except citizenError:
					print("Please make sure you entered the same letter as in the choice!")
					continue
				break
			break

print("Welcome to Water Theme Park Package System",name,"!")
print("Please enter the following information:")
for i in range(0,100):
			while True:
				try:
					adult = int(input("Adult: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break

for i in range(0,100):
			while True:
				try:
					child = int(input("Child: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break
 
for i in range(0,100):
			while True:
				try:
					senior = int(input("Senior Citizen: "))
				except:
					print("Please enter numbers only!")
					continue
				break
			break
file1 = open("entrance Rate.txt", encoding="utf8")
# Reading from file
print(file1.read())
file1.close()
if nationality == "Citizen":
	totalAdult = adult*23
	totalChild = child*18
	totalSenior = senior*14
	totalAll = totalAdult + totalChild + totalSenior
	adultToString = str(adult)
	childToString = str(child)
	seniorToString = str(senior)
	totalToString = str(totalAll)
	print("Customer Information")
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Telephone Number: ",phone)
	print("Nationality: ",nationality)
	print("Number of Adults: ",adult)
	print("Number of Childs: ",child)
	print("Number of Senior Citizens: ",senior)
	print("The total payment is:RM",totalAll)
	f = open("Receipt.txt", "a")
	f.write('Customer Information:'+'\n')
	f.write('Name:'+name+'\n')
	f.write('IC Number:'+ic+'\n')
	f.write('Telephone Number:'+phone+'\n')
	f.write('Nationality:'+nationality+'\n')
	f.write('Number of Adults:'+adultToString+'\n')
	f.write('Number of Childs:'+childToString+'\n')
	f.write('Number of Senior Citizens:'+seniorToString+'\n')
	f.write('The total payment is:RM'+totalToString+'\n')
else:
	totalAdult = adult*33
	totalChild = child*28
	totalSenior = senior*24
	totalAll = totalAdult + totalChild + totalSenior
	adultToString = str(adult)
	childToString = str(child)
	seniorToString = str(senior)
	totalToString = str(totalAll)
	print("Customer Information")
	print("Name: ",name)
	print("IC Number: ",ic)
	print("Telephone Number: ",phone)
	print("Nationality: ",nationality)
	print("Number of Adults: ",adult)
	print("Number of Childs: ",child)
	print("Number of Senior Citizens: ",senior)
	print("The total payment is:RM",totalAll)
	f = open("Receipt.txt", "a")
	f.write('Customer Information:'+'\n')
	f.write('Name:'+name+'\n')
	f.write('IC Number:'+ic+'\n')
	f.write('Telephone Number:'+phone+'\n')
	f.write('Nationality:'+nationality+'\n')
	f.write('Number of Adults:'+adultToString+'\n')
	f.write('Number of Childs:'+childToString+'\n')
	f.write('Number of Senior Citizens:'+seniorToString+'\n')
	f.write('The total payment is:RM'+totalToString+'\n')