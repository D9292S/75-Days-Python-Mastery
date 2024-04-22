import json
import hashlib
class BankAccount:
    VALID_ACCOUNT_TYPES = ["Savings Account", "Current Account"]

    def __init__(self, client_id, first_name, last_name, account_no, crn_number, password, branch, Savings_Account = 0, Current_Account= 0):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.account_no = account_no
        self.crn_number = crn_number
        self.password = password
        self.branch = branch
        self.Savings_Account = Savings_Account
        self.Current_Account = Current_Account
        self.clients = self._load_bank_data()

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def balance(self, client_id):
        client = self.clients.get(str(client_id), {})
        return client.get("Savings Account", 0) , client.get("Current Account", 0)
    
    def _get_client(self):
        return self.clients.get(str(self.client_id), {})
    
    def open_account(self):
        if str(self.client_id) in self.clients:
            raise ValueError("An account with this client_id already exists.")
        self.clients[str(self.client_id)] = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Account Number": self.account_no,
            "CRN Number": self.crn_number,
            "Password": self.password,
            "Branch": self.branch,
            "Savings Account": self.Savings_Account,
            "Current Account": self.Current_Account
        }
        self._save_bank_data()

    def deposit(self, client_id, amount, account_type):
        if account_type not in self.VALID_ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type. Expected one of {self.VALID_ACCOUNT_TYPES}")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if account_type == "Savings Account":
            self.clients[str(client_id)]["Savings Account"] += amount
        else:
            self.clients[str(client_id)]["Current Account"] += amount
        self._save_bank_data()

    def _load_bank_data(self):
        try:
            with open("mainbank.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_bank_data(self):
        with open("mainbank.json", "w") as f:
            json.dump(self.clients, f, indent=4)

class Transaction:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def deposit(self, amount, account_type):
        self.bank_account.deposit(amount, account_type)

    def withdraw(self, amount, account_type):
        if self.bank_account.clients[str(self.bank_account.client_id)][account_type] < amount:
            raise ValueError("Insufficient balance.")
        self.bank_account.clients[str(self.bank_account.client_id)][account_type] -= amount
        self.bank_account._save_bank_data()

class BankManager:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def open_account(self):
        self.bank_account.open_account()

    def close_account(self):
        del self.bank_account.clients[str(self.bank_account.client_id)]
        self.bank_account._save_bank_data()
