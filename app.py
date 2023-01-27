#Write a function, parallel(), that, when called, outputs the outputs 
# the effective resistance of a network of 2 or more resistors 
# connected in parallel. The function should be able to accept 
# a list of numbers of any length.



def parallel(resistors):
    size=len(resistors)
    if (size>=2):
        sum=0
        paralsum=0
        for x in resistors:
            sum += (1/x)
        paralsum=(1/sum)
        print('%.2f' % paralsum,"ohms")
    else:
        print("not enough resistors")
    return 0



parallel([330,2200,1000])



		

def potential_divider(voltage,r):
    sum=0
    for x in r:
        sum += x
    for x in r:
        div=((x*voltage) / sum)
        print('%.2f'%div,"v")
resistors = [1010,1933,356]
potential_divider(6,resistors[:])

 
def temperature_check(temp,tempchar):
	if (tempchar=="c"|tempchar =="C"):
		if (temp<34):
			print("youre hypothermic")
		elif(temp>=36 & temp<38):
			print ("youre normal")
		else:
            print ("youre hyperthermic")
	if(tempchar=='f'| tempchar=='F'):
		if (temp<95):
			print("youre hypothermic")
		elif (temp>=96 & temp<100):
			print("youre normal")
		else:
			print("youre hyperthermic")

temperature_check(32,'F')