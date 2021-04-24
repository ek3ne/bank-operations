#What are we doing?
#basic login authentification program


import random

def init():
    #this is to initialiaze the program, remember to run 'init()' at bottom of code
    print('Welcome to Python Bank')
    haveAccount=int(input('1. Login\n2. Create New Account\n'))
    if haveAccount==1:       
        login()           
    elif haveAccount==2:
        register()
    else:
        print('Invalid Option')

        init()

    



def login():
    #this is login
    print('***** LOGIN *****')
    enterAccountNum=input('Enter your Account Number\n')
    enterPassword=input('Enter your Password\n')

    bankOperation()



def register():
    #this is to register new account
    print('***** REGISTER *****')
    email=input('Enter your email address\n')
    firstName=input('Enter your First Name\n')
    lastName=input('Enter your Last Name\n')
    password=input('Create a Secure Password\n')
    
    genAccountNum()




def genAccountNum():
    #this is to get acccount number
    print('Your new account number is')
    print(random.randrange(1111111111, 9999999999))

    login()




def bankOperation():
    whatToDo=int(input('What would you like to do?\n 1. Withdrawal\n 2. Deposit\n 3. Check Balance\n'))
    if whatToDo==1:
        withdraw()
    elif whatToDo==2:
        deposit()
    elif whatToDo==3:
        checkBal()
    else:
        print('Invalid Option Selected')
        bankOperation()



        
def withdraw():
    print('this is to withdraw')
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance

def deposit():
    print('this is to deposit')
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance
    
def checkBal():
    print('this is to check balance')




        
def logout():
    login()





def exit():
    exit()





init()
