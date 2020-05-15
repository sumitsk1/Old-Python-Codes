import sys

print("## Welcome to Paytm bank")

name=input("Please enter your Enter your Name ")
print("welcome to PayTm bank",name)

print("Swipe Your ATM card")
balance=100000
#user1=0000000000
#user2=1111111111
atm_pin=int(input("Enter your pin :"))
while(True):

    if atm_pin==9999:

        print("choose Your transaction")
        print("1. Balance Enquiry")
        print("2. Withdraw Money")
        print("3. Deposite Money")
        print("4. Money Transfer")
        print("5. Change Your Pin")
        print("6. Cancle")
        tran=int(input("Enter :"))
        if tran==1:
            print("Do you want slip")
            sleep=input(str("Type yes or NO"))
            if sleep=="yes" or "Yes":
                print("Your current balance is RS {}".format(balance))
            else:
                print("Thanks for using paytm bank")
        elif tran==2:
            print("so you want to withdraw your money")
            withdraw=int(input("Enter the amount"))
            if withdraw>0:
                print("Collect please collect your cash before leaving the ATM computer")
                print("RS = {}".format(withdraw))
                print("Current balance: {}".format(balance-withdraw))
            else:
                print("sorry , please try again")
        elif tran==3:
            print("so you want to deposite some money")
            deposite=int(input("Enter the amout to deposite : "))
            if deposite>0:
                print("Thanks for your Trust :")
                print("your updated balance : {}".format(balance+deposite))
            else:
                print("sorry , please try again :")

        elif tran==4:
            print("so you want to tranfer Money to other User ")
            user2=int(input("Enter the 10 digits account Number of other user"))
            if user2==1111111111:
                amount=int(input("Enter the amount to transfer to other user :"))
                if amount>0:
                    if (balance-amount) >=0:
                        print("Transfer successfull")
                        print("Updated balance {}".format(balance-amount))
                    else:
                        print("You dont have enough Money")
                else:
                    print("Please Try again")
            else:
                print("please enter the correct account number")
        elif tran==5:
            print("So you want to change Your paytm pin, Good :")
            pin=int(input("Enter current 4 digits pin "))
            if pin==9999:
                print("pin matched successfully :")
                new_pin=input("Enter 4 digits new pin :")
                if len(new_pin)==4:
                    print("your new pin {}".format(new_pin))
                else:
                    print("sorry , you have not entered the 4 digit pin \n please try again")
            else:
                print("sorry ,Wrong pin :")

        elif tran==6:
            print("thanks You :")
            sys.exit("bye bye")
        
        
       
    else:
        print("Enter the correct pin")
