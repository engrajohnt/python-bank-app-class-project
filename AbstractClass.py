from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, first_name, last_name, email, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pin = pin

    @abstractmethod
    def login(self, email, pin):
        pass

    @abstractmethod
    def reset_password(self, old_password, new_password):
        pass

    @abstractmethod
    def view_account_info(self):
        pass
    
    @abstractmethod
    def transfer_funds(self, recipient_account, amount, pin):
        pass
