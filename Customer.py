from AbstractClass import BankAccount
    
class Customer(BankAccount):
    def __init__(self, first_name, last_name, email, pin, _account_number, _balance=0.0):
        super().__init__(first_name, last_name, email, pin)
        self._account_number = _account_number
        self._balance = _balance

    def login(self, email, pin):
        if email == self.email and pin == self.pin:
            print("Login successful. Welcome back, customer {}!".format(self.first_name))
            return True
        else:
            print("Invalid credentials. Login failed.")
            return False

    def reset_password(self, old_password, new_password):
        if old_password == self.pin:
            self.pin = new_password
            print("Password reset successfully.")
        else:
            print("Invalid old password. Password reset failed.")
            
    def reset_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN reset successful.")
        else:
            print("Invalid old PIN. PIN reset failed.")
            
    def view_account_info(self):
        print("Account Information:")
        print("Name:", self.first_name, self.last_name)
        print("Email:", self.email)
        print("Account Number:", self._account_number)
        print("Balance: N", self._balance)

    def transfer_funds(self, recipient_account, amount, pin,db):
        if not self.login(self.email, pin):
            print("Invalid PIN. Transfer failed.")
            return

        if amount <= 0:
            print("Invalid amount. Transfer failed.")
            return
        
        if self._balance < amount:
            print("Insufficient balance. Transfer failed.")
            return

        self._balance -= amount
        recipient = db.find_customer_by_account_number(recipient_account)
        recipient.receive_funds(amount)
        db.save_data()
        print("Transferring {} to recipient account: {}".format(amount, recipient_account))
        print("New balance:", self._balance)

    def receive_funds(self, amount):
        self._balance += amount
        print("Received {} from agent. New balance: {}".format(amount, self._balance))
