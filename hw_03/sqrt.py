
def mysqrt(number):
    #newguess=Oldguess+(new/oldguess))/2
    guess=1
    while (guess!= number**(1/2)):
        guess=(guess+number/guess)/2

        print (guess)
    return str(guess)+" this is the square root of "+ str(number)
#print(mysqrt(16))
print(mysqrt(5))
#for i in range (3):
#    print(mysqrt(i))