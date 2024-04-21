import json

class BankAccount:
    def __init__(self, client_id, first_name, last_name, account_no, crn_number, password, branch):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.account_no = account_no
        self.crn_number = crn_number
        self.password = password
        self.branch = branch

    def balance(self):
        self.open_account()
        clients = self.get_bank_data()
        savings = clients[str(self.client_id)]["Savings Account"]
        current = clients[str(self.client_id)]["Current Account"]
        return savings, current
    
    def open_account(self):
        clients = self.get_bank_data()
        if str(self.client_id) not in clients:
            clients[str(self.client_id)] = {
                "First Name": self.first_name,
                "Last Name": self.last_name,
                "Account Number": self.account_no,
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
        with open('mainbank.json', 'r') as f:
            clients = json.load(f)

        return clients