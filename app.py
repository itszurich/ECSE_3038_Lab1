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



		

