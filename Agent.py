from AbstractClass import BankAccount

class Agent(BankAccount):
    def login(self, email, pin):
        if email == self.email and pin == self.pin:
            print("Agent login successful. Welcome back, {}!".format(self.first_name))
            return True
        else:
            print("Invalid credentials. Agent login failed.")
            return False

    def reset_password(self, old_password, new_password):
        if old_password == self.pin:
            self.pin = new_password
            print("Agent password reset successful.")
        else:
            print("Invalid old password. Agent password reset failed.")

    def view_account_info(self):
        print("Account Information:")
        print("Name:", self.first_name, self.last_name)
        print("Email:", self.email)
        print("Account Number:", self._account_number)

    def transfer_funds(self, recipient_account, amount, pin):
        if pin != self.pin:
            print("Invalid PIN. Transfer failed.")
            return

        if amount <= 0:
            print("Invalid amount. Transfer failed.")
            return

        print("Transferring {} to recipient account: {}".format(amount, recipient_account))

    def transfer_funds_to_customer(self, customer_account, amount, pin, db):
        customer = db.find_customer_by_account_number(customer_account)
        if not customer:
            print("Customer account not found.")
            return

        if pin != customer.pin:
            print("Invalid PIN. Transfer failed.")
            return

        if amount <= 0:
            print("Invalid amount. Transfer failed.")
            return

        customer.receive_funds(amount)
        print("Transferring {} to customer account: {}".format(amount, customer_account))
        db.save_data()

    def reset_customer_pin(self, customer_account, new_pin, db):
        customer = db.find_customer_by_account_number(customer_account)
        if customer:
            customer.reset_pin(customer.pin, new_pin)
            db.save_data()
            print("Reset customer PIN for account: {} to new PIN: {}".format(customer_account, new_pin))
        else:
            print("Customer account not found.")

    def delete_customer_account(self, customer_account, db):
        customer = db.find_customer_by_account_number(customer_account)
        if customer:
            confirmation = input("Are you sure you want to delete the customer's account? (yes/no): ")
            if confirmation.lower() == "yes":
                db.remove_customer(customer._account_number)
                print("Deleted customer account: {}".format(customer_account))
            else:
                print("Account deletion canceled.")
        else:
            print("Customer account not found.")

    def reset_account_pin(self, email, old_password, new_pin, db):
        agent = db.find_agent_by_email(email)
        if agent and agent.pin == old_password:
            agent.pin = new_pin
            db.save_data()
            print("Agent PIN reset successful.")
        else:
            print("Invalid email or old password. Agent PIN reset failed.")
