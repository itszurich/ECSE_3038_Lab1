def temperature_check(temp,tempchar):
	if (tempchar=="c"| tempchar=="C"):
		if (temp<35):
			print("youre hypothermic")
		elif(temp>=35 & temp<38):
			print ("youre normal")
		else:
			print("youre hyperthermic")
	if(tempchar=='f'| tempchar=='F'):
		if (temp<95):
			print("youre hypothermic")
		elif (temp>=96 & temp<100):
			print("youre normal")
		else:
			print("youre hyperthermic")

temperature_check(32,'F')