# C Assignment 2 Converted to Python

option = 0
PinNum = 0
pin = []

def PIN(PinNum):
	print "Enter your 4 digit PIN one digit at a time\n"

	while (PinNum < 4) :
        PinNum = PinNum + 1
        num = input()
    	pin.append(num)
    print "New pin is", pin

while option != 5:

    print "Please select any one of the following:\n\n"
    print "1. Enter code\n"
    print "2. Encrypt code and verify if correct\n"
    print "3. Decrypt code\n"
    print "4. Display the number of times the code was entered (i) Successfully (ii) Incorrectly\n"
    print "5. Exit Program\n"
    option = input(' ')
    
    if option == 1 :
    	PIN(PinNum);
	    # call function PIN
	    # PIN (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
        
    elif option == 2:
    	print "ggg"
        # call function ENCRYPT
        #ENCRYPT (code_p, correctly_entered, INcorrectly_entered, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    
    elif option == 3 :
    	print "ggg"

        # call function DECRYPT
        # DECRYPT (code_p, EncryptBeforeDecrypt, EncryptingTwice, EnterPinFirst);
    
    if option == 4 :
    	print "ggg"

        # call function COUNT
        # COUNT (correctly_entered, INcorrectly_entered, EnterPinFirst);

    else :
    	option = 5
    	print "ggg"

    	# exit program