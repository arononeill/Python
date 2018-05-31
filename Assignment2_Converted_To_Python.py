# C Assignment 2 Converted to Python

option = 0
correctly_entered = 0
Incorrectly_entered = 0

pin = []

def PIN():
    "Enters the user's pin"
    print "Enter your 4 digit PIN one digit at a time\n"
    PinNum = 0

    while PinNum < 4:
        PinNum += 1
        num = input()
        pin.append(num)

    print "New pin is", pin

def ENCRYPT():
    "Encrypts the user's pin"
    # Algorithm to encrypt the user's pin
    temp = pin[0]
    pin[0] = pin[2]
    pin[2] = temp

    temp = pin[1]
    pin[1] = pin[3]
    pin[3] = temp

    PinNum = 0
    while PinNum < 4:
        pin[PinNum] += 1

        if pin[PinNum] == 10:
            pin[PinNum] = 0

        PinNum += 1

    print "The pin you encrypted pin is ", pin
    COMPARE();

def COMPARE():
    access_code = [4, 5, 2, 3]
    flag = True
    PinNum = 0

    while PinNum < 4:
        if pin[PinNum] != access_code[PinNum]:
            flag = False
        PinNum += 1


    if (flag):
        print "Pin Entered Correctly"
        correctly_entered += 1

    else:
        print "Pin Entered Incorrectly"
        Incorrectly_entered += 1


def DECRYPT():

    temp = pin[3]
    pin[3] = pin[1]
    pin[1] = temp

    temp = pin[0]
    pin[0] = pin[2]
    pin[2] = temp

    PinNum = 0
    while PinNum < 4:
        pin[PinNum] -= 1

        if pin[PinNum] == -1:
            pin[PinNum] = 9

        PinNum += 1

    print "Your newly decrypted pin is ", pin 

def COUNT():
    print "\nNumber of times entered correctly : "
    print "\nNumber of times entered incorrectly : "

while option != 5:

    print "Please select any one of the following:\n\n"
    print "1. Enter code\n"
    print "2. Encrypt code and verify if correct\n"
    print "3. Decrypt code\n"
    print "4. Display the number of times the code was entered (i) Successfully (ii) Incorrectly\n"
    print "5. Exit Program\n"
    option = input(' ')
    
    if option == 1 :
    	PIN();
	    # call function PIN
	    # PIN (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);   
    elif option == 2:
        ENCRYPT(); 
        # call function ENCRYPT
        #ENCRYPT (code_p, correctly_entered, INcorrectly_entered, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    elif option == 3 :
    	DECRYPT();

        # call function DECRYPT
        # DECRYPT (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    elif option == 4 :
    	COUNT();

        # call function COUNT
        # COUNT (correctly_entered, INcorrectly_entered, EnterPinFirst);
    else :
        option = 5
    	print "Thank you for using this service"
        # exit program