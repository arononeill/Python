# C Assignment 2 Converted to Python

option = 0
correctly_entered = 0
Incorrectly_entered = 0   
EnterPinFirst = 0  
EncryptFirst = 0 
EncryptTwice = 0 
DecryptTwice = 0 
pin = [0, 0, 0, 0]

def PIN():
    "Enters the user's pin"
    print ("Enter your 4 digit PIN one digit at a time\n")
    PinNum = 0
    EncryptTwice = 0
    DecryptTwice = 0

    while PinNum < 4:
        num = input()

        if num >= 0 and num < 10:
            pin[PinNum] = num
            PinNum += 1

        else:
            print ("\nPlease Enter one digit at a time\n")
            PinNum = 0

    print ("New pin is", pin)
    EnterPinFirst = 1

    return EnterPinFirst

def ENCRYPT(EnterPinFirst):
    "Encrypts the user's pin"
    global EncryptFirst
    if EnterPinFirst == 1:
        global EncryptTwice
        if EncryptTwice == 0:
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

            print ("The pin you encrypted pin is ", pin)
            EncryptFirst = 1
            EncryptTwice = 1
            COMPARE();

        else:
            print ("\n\t*** Sorry you cannot encrypt the same pin twice ***\n")

    else:
        print ("\n\t*** Please Enter a pin First ***\n")

    return EncryptFirst

def COMPARE():
    access_code = [4, 5, 2, 3]
    flag = True
    PinNum = 0
    global correctly_entered
    global Incorrectly_entered

    while PinNum < 4:
        if pin[PinNum] != access_code[PinNum]:
            flag = False
        PinNum += 1

    if (flag):
        print ("\nPin Entered Correctly\n")
        correctly_entered += 1

    else:
        print ("\nPin Entered Incorrectly\n")
        Incorrectly_entered += 1


def DECRYPT(EnterPinFirst, EncryptFirst):

    if EnterPinFirst == 1:
        if EncryptFirst == 1:
            global DecryptTwice
            if DecryptTwice == 0:
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

                print ("Your newly decrypted pin is ", pin)
                DecryptTwice = 1

            else:
                print ("\n\t*** Sorry you cannot decrypt the same pin twice ***\n")

        else:
            print ("\n\t***Please Encrypt your pin first ***\n")

    else:
        print ("\n\t*** Please Enter a pin First ***\n")        

def COUNT(EnterPinFirst):

    if EnterPinFirst == 1:
        print ("\nNumber of times entered correctly : ", correctly_entered)
        print ("\nNumber of times entered incorrectly : ", Incorrectly_entered)

    else:
        print ("\n\t*** Please Enter a pin First ***\n")  

while option != 5:

    print ("Please select any one of the following:\n\n")
    print ("1. Enter code\n")
    print ("2. Encrypt code and verify if correct\n")
    print ("3. Decrypt code\n")
    print ("4. Display the number of times the code was entered (i) Successfully (ii) Incorrectly\n")
    print ("5. Exit Program\n")
    option = input(' ')
    
    if option == 1 :
    	EnterPinFirst = PIN();
	    # call function PIN
	    # PIN (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);   
    elif option == 2:
        EncryptFirst = ENCRYPT(EnterPinFirst); 
        # call function ENCRYPT
        #ENCRYPT (code_p, correctly_entered, INcorrectly_entered, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    elif option == 3 :
    	DECRYPT(EnterPinFirst, EncryptFirst);

        # call function DECRYPT
        # DECRYPT (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    elif option == 4 :
    	COUNT(EnterPinFirst);

        # call function COUNT
        # COUNT (correctly_entered, INcorrectly_entered, EnterPinFirst);
    else :
    	print ("Thank you for using this service")
        # exit program