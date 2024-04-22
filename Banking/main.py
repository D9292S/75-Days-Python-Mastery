import random
from banking import BankAccount
import time 
from tqdm import tqdm
import os

from getpass import getpass 

os.chdir("D:\\75 Days Python Mastery\\Banking")


def welcome_screen():
    print()
    print("*** Welcome to DS Bank ***")
    print()
    print("NOTE: Dear user, we do not ask for your personal information such as ATM PIN, Card No, CVV, etc.")
    print("Kindly do not share it with anyone")
    print()
    print("To Continue, press 1, To exit press any other key.")

def netbanking_portal():
    print()
    print("--------------------------------------------------------------------------------------")
    print("| ****** Welcome To DS Netbanking Portal, Kindly Enter your Unique Customer Id ***** |")
    print("--------------------------------------------------------------------------------------")
    print()


def banking_services_menu():
    print("+-----------------------------------------+")
    print("|             DS Bank Services            |")
    print("+-----------------------------------------+")
    print("| 1. Banking Services                     |")
    print("| 2. Card Services                        |")
    print("| 3. Loan Services                        |")
    print("| 4. Customer Services                    |")
    print("| Any Other Key to Exit                   |")
    print("+-----------------------------------------+")
    print()

def banking_services(bank_account, client_id):
    choice = input("Enter your choice: ")
    print()
    while True:
        if choice == '1':
            print("+----------------------------------------+")
            print("|          Banking Services Menu         |")
            print("+----------------------------------------+")
            print("| 1. Check Balance                       |")
            print("| 2. Deposit Money                       |")
            print("| 3. Withdraw Money                      |")
            print("| 4. Transfer Money                      |")
            print("| Pres Any Other Key to Exit             |")
            print("+----------------------------------------+")
            print()

            choice = input("Enter your choice: ")
            print()

            if choice == '1':
                savings, current = bank_account.balance(client_id)
                print("+--------------------------------------------+")
                print(f"| Your Savings Account Balance is: {savings} |")
                print(f"| Your Current Account Balance is: {current} |")
                print("+--------------------------------------------+")

            elif choice == '2':
                print("Please Choose the type of Account you want to deposit money into..")
                print()
                print("Press 1 for Savings Account")
                print("Press 2 for Current Account")
                print()
                choice = input("Enter your choice: ")
                print()
                if choice == '1':
                    amount = int(input("Enter the amount to be deposited: "))
                    bank_account.deposit(client_id, amount, "Savings Account")
                    print(f"Amount of ${amount} deposited successfully in Savings Account")
                else:
                    amount = int(input("Enter the amount to be deposited: "))
                    bank_account.deposit(client_id, amount, "Current Account")
                    print(f"Amount of ${amount} deposited successfully in Current Account")

            elif choice == '3':
                amount = int(input("Enter the amount to be withdrawn: "))
                account_type = input("Enter the account type (Savings Account/Current Account): ")
                bank_account.withdraw(amount, account_type)
                print("Amount Withdrawn Successfully")

            elif choice == '4':
                amount = int(input("Enter the amount to be transferred: "))
                account_type = input("Enter the account type (Savings Account/Current Account): ")
                bank_account.transfer(amount, account_type)
                print("Amount Transferred Successfully")

            else:
                print("Thank You for using DS Bank")
                break


def login(client_id, bank_account):
    clients = bank_account._load_bank_data()
    for i in range(3, 0, -1):
        password = getpass("Enter your Password: ")
        if password != clients[str(client_id)]["Password"]:
            print(f"Invalid Password, Please Try Again: Attempts Left {i-1}")
            if i == 1:
                print("You have entered the wrong password multiple times, Kindly try again after 24 hours later.")
                exit(0)
        else:
            break
        

def register():
    print("You are not a registered user, Kindly Register Yourself")
    print()
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    account_number = random.randint(10000000000000, 999999999909999)
    crn_number = random.randint(100000, 999999)
    client_id = first_name[:4] + str(random.randint(100000, 999999))
    password = first_name[:2].upper() + last_name[:2].lower() + '@' + str(random.randint(100000, 999999))
    branch = "Codex Discord"
    bank_account = BankAccount(client_id, first_name, last_name, account_number, crn_number, password, branch)
    bank_account.open_account()
    print()
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
    print("Congratulations, We have successfully opened an account for you!")
    print("Please Note Down your Account Details for Future Reference..........")
    print()
    print("****************************************************")
    print("*                                                  *")
    print("*                Account Details                   *")
    print("*                                                  *")
    print("****************************************************")
    print("* Client Id: ", client_id, " "*(35-len(client_id)), "*")
    print("* First Name: ", first_name, " "*(34-len(first_name)), "*")
    print("* Last Name: ", last_name, " "*(35-len(last_name)), "*")
    print("* Account Number: ", account_number, " "*(30-len(str(account_number))), "*")
    print("* CRN Number: ", crn_number, " "*(34-len(str(crn_number))), "*")
    print("* Password: ", password, " "*(36-len(password)), "*")
    print("* Branch: ", branch, " "*(38-len(branch)), "*")
    print("*                                                  *")
    print("****************************************************")
    print()
    print("Thank You for choosing DS Bank")
    print("Thank You for using DS Netbanking Portal, Have a Nice Day!")



def main():
    welcome_screen()
    ch = input("Enter your choice: ")
    if ch == '1':
        netbanking_portal()
        client_id = input("Enter your Unique Customer Id, If you don't have one, press any key to Register: ")
        print()
        bank_account = BankAccount(client_id, "", "", "", "", "", "", "", "")
        if client_id in bank_account._load_bank_data():
            login(client_id, bank_account)
            print()
            print(f"** Login Successful, Welcome user {client_id} **")
            print()
            banking_services_menu()
            banking_services(bank_account, client_id)

        else:
            register()
    else:
        print("Thank You for using DS Bank")

if __name__ == "__main__":
    main()






