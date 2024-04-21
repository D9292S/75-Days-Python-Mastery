import random
from banking import BankAccount
import time 
from tqdm import tqdm
import os

os.chdir("D:\\75 Days Python Mastery\\Banking")
print("*** Welcome to DS Bank ***")
print()
print("NOTE: Dear user, we do not ask for your personal information such as ATM PIN, Card No, CVV, etc.")
print("Kindly do not share it with anyone")
print()
print("To Continue, press 1. To exit, press any other key.")
print()
ch = input("Enter your choice: ")
if ch == '1':
    print("**** Welcome To DS Netbanking Portal, Kindly Enter your Unique Customer Id *****")
    print()
    client_id = input("Enter your Unique Customer Id, If you don't have one, press any key to Register: ")
    print()

    bank_account = BankAccount(client_id, "", "", "", "", "", "")
    if client_id in bank_account.get_bank_data():
        password = input("Enter your Password: ")
        bank_account = BankAccount(client_id, "", "", "", "", password, "")
        if password != bank_account.get_bank_data()[str(client_id)]["Password"]:
            print("Invalid Password, Please Try Again")
            exit()

        else:
            print()
            print(f"Welcome Back **{client_id}**!")
            print("Press 1. Check Balance")
            print("Press 2. Deposit Money")
            print("Press 3. Withdraw Money")
            print("Press 4. Transfer Money")
            print("Press Any Other Key to Exit")
            print()

            choice = int(input("Enter your choice: "))
            print()

            if choice == 1:
                print("Your Account Balance is: ", bank_account.balance())
            elif choice == 2:
                amount = int(input("Enter the amount to be deposited: "))
                bank_account.deposit(amount)
                print("Amount Deposited Successfully")
            elif choice == 3:
                amount = int(input("Enter the amount to be withdrawn: "))
                bank_account.withdraw(amount)
                print("Amount Withdrawn Successfully")
            elif choice == 4:
                recipient_id = input("Enter the recipient's Customer Id: ")
                amount = int(input("Enter the amount to be transferred: "))
                bank_account.transfer(recipient_id, amount)
                print("Amount Transferred Successfully")
            else:
                print("Thank You for using DS Netbanking Portal")
    



    else:
        print("You are not a registered user, Kindly Register Yourself")
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        account_number = random.randint(10000000000000, 999999999909999)
        crn_number = random.randint(100000, 999999)
        client_id = first_name[:4] + str(random.randint(100000, 999999))
        password = first_name[:2].upper() + last_name[:2].lower() + '@' + str(random.randint(100000, 999999))
        branch = "Codex Discord"
        bank_account = BankAccount(client_id, first_name, last_name, account_number, crn_number, password, branch)
        bank_account.open_account()
        print("Please Wait while we open an account for you...")
        print()
        time.sleep(5)
        print("We are connecting to our server, Kindly wait for a moment....")
        print('Connecting', end='')

        for i in tqdm(range(100)):
            time.sleep(0.1)

        print()
        print()
        time.sleep(3)
        print("Congratulations, We have successfully opened an account for you")
        print("Please Note Down your Account Details for Future Reference")
        print()
        print("Client Id: ", client_id)
        print("First Name: ", first_name)
        print("Last Name: ", last_name)
        print("Account Number: ", account_number)
        print("CRN Number: ", crn_number)
        print("Password: ", password)
        print("Branch: ", branch)
        print()
        print("Thank You for choosing DS Bank")
        print("Thank You for using DS Netbanking Portal")
else:
    print("Thank You for using DS Netbanking Portal")


