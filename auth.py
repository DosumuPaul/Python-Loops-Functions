import random

database = {}  #dictionary

def init():

    is_valid_option = False
    print("Welcome to BankPHP!")

    while is_valid_option == False:

        have_account = int(input("Do you have an account?: 1 (yes) 2 (No) \n"))

        if have_account == 1:
            is_valid_option = True
            login()
        elif have_account == 2:
            is_valid_option = True
            print(register())
        else:
            print("You have selected an invalid option")    


def login():
    
    print("***** Login *****")

    is_login_successful = False

    while is_login_successful == False:

        account_number_from_user = int(input("What is your account number? \n"))
        password = input("What is your password \n")

        for account_number, user_details in database.items():
            if account_number == account_number_from_user:
                if user_details[3] == password:
                    is_login_successful = True
                    
        print("Invalid account or password")            

        #def bank_operations(user_details):

def register():

    print("Create an Account!")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("***Account Creation Successfull!***")
    print("== === ===== ===== ==")
    print("Your account number is %d" %account_number)
    print("Make sure you keep it safe")
    print("== === ===== ===== ==")

    login()
    
def bank_operations(user):
    print("Welcome %s %s" %(user[0], user[1] ) )
    
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (5) Exit (4) Logout \n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_option()
    elif selected_option == 3:
        complaint_option
    elif selected_option == 5:
        exit        
    elif selected_option == 4:
        logout()
    else:
        print("Invalid option selected")  
        bank_operations(user)      

def withdrawal_option():
    print("withdrawal")

def deposit_operation():
    print("Deposit Operations")

def complaint_option():
    print("Complaint_operation")         

def generate_account_number():

    print("Generating Account Number")
    return random.randrange(1111111111,9999999999)

def logout():
    login()    


#### ACTUAL BANKING SYSTEM ###
#rint(generate_account_number())
init()

      