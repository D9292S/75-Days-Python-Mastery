import json
from dataclasses import dataclass

@dataclass
class BankAccount:
    def __init__(self, client_id, first_name, last_name, account_number, crn_number, password, branch):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.crn_number = crn_number
        self.password = password
        self.branch = branch

    class BankingSystem:
        """
        A class representing a banking system.
        """

        def __init__(self, client_id, first_name, last_name, account_number, crn_number, password, branch):
            """
            Initialize a BankingSystem object.

            Parameters:
            - client_id (int): The client ID.
            - first_name (str): The first name of the client.
            - last_name (str): The last name of the client.
            - account_number (str): The account number of the client.
            - crn_number (str): The CRN (Customer Reference Number) of the client.
            - password (str): The password of the client.
            - branch (str): The branch of the client.
            """
            self.bank_account = BankAccount(client_id, first_name, last_name, account_number, crn_number, password, branch)
        
        @property
        def balance(self):
            """
            Get the balance of the client's savings and current accounts.

            Returns:
            - tuple: A tuple containing the savings and current account balances.
            """
            self.open_account()
            clients = self.get_bank_data()
            savings = clients[str(self.client_id)]["Savings Account"]
            current = clients[str(self.client_id)]["Current Account"]
            return savings, current

        def open_account(self):
            """
            Open a bank account for the client if it doesn't exist.

            Returns:
            - bool: True if the account was opened successfully, False otherwise.
            """
            clients = self.get_bank_data()
            if str(self.client_id) not in clients:
                clients[str(self.client_id)] = {
                    "First Name": self.first_name,
                    "Last Name": self.last_name,
                    "Account Number": self.account_number,
                    "CRN Number": self.crn_number,
                    "Password": self.password,
                    "Branch": self.branch,
                    "Savings Account": 0,
                    "Current Account": 0
                }
            
            with open("mainbank.json", "w") as f:
                json.dump(clients, f, indent=4)

            return True 
        
        def get_bank_data(self):
            """
            Get the bank data from the JSON file.

            Returns:
            - dict: A dictionary containing the bank data.
            """
            with open('mainbank.json', 'r') as f:
                clients = json.load(f)

            return clients
class Transaction:
    def __init__(self, sender_id, receiver_id, amount):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount

    def execute(self):
        sender = BankAccount.get_account_by_id(self.sender_id)
        receiver = BankAccount.get_account_by_id(self.receiver_id)

        if sender and receiver:
            sender_balance = sender.balance[0] + sender.balance[1]
            if sender_balance >= self.amount:
                sender.update_balance(-self.amount)
                receiver.update_balance(self.amount)
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def transfer(sender_id, receiver_id, amount):
        transaction = Transaction(sender_id, receiver_id, amount)
        return transaction.execute()


    @staticmethod
    def deposit(account_id, amount):
        account = BankAccount.get_account_by_id(account_id)
        if account:
            account.update_balance(amount)
            return True
        else:
            return False


    @staticmethod
    def withdraw(account_id, amount):
        account = BankAccount.get_account_by_id(account_id)
        if account:
            account_balance = account.balance[0] + account.balance[1]
            if account_balance >= amount:
                account.update_balance(-amount)
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def get_balance(account_id):
        account = BankAccount.get_account_by_id(account_id)
        if account:
            return account.balance
        else:
            return None


    @staticmethod
    def get_account_by_id(account_id):
        with open('mainbank.json', 'r') as f:
            clients = json.load(f)

        if str(account_id) in clients:
            account_data = clients[str(account_id)]
            return BankAccount(
                account_id,
                account_data["First Name"],
                account_data["Last Name"],
                account_data["Account Number"],
                account_data["CRN Number"],
                account_data["Password"],
                account_data["Branch"]
            )
        else:
            return None
