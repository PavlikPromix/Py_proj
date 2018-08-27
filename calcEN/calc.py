print ("Welcome to the Calc!")
print ("Input Help to take some help")
print ("ver 2.4.1")
while True:
	uin = input(":")
	if uin == "Help":
		print ("Input Add to add nums")
		print ("Input Multiply to multiply nums")
		print ("Input Divide to divide nums")
		print ("Input Subtract to subtract nums")
		print ("Enter Quit to quit from app")
	elif uin == "Add":
		a = float(input("Enter num : "))
		b = float(input("Enter another num : "))
		res = str(a + b)
		print ("Result : " + res)
	elif uin == "Multiply":
		a = float(input("Enter num : "))
		b = float(input("Enter another num : "))
		res = str(a * b)
		print ("Result : " + res)
	elif uin == "Divide":
		a = float(input("Enter num : "))
		b = float(input("Enter another num : "))
		res = str(a / b)
		print ("Result : " + res)
	elif uin == "Subtract":
		a = float(input("Enter num : "))
		b = float(input("Enter another num : "))
		res = str(a - b)
		print ("Result : " + res)
	elif uin == "Quit":
		break
	else:
		print ("Unknown input!")
