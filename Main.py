from Customer import Customer
from Agent import Agent
from Database import Database, generate_account_number

db = Database()
db.load_data()

print("Number of customers:", len(db.customers))
print("Number of agents:", len(db.agents))

def create_customer_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    pin = input("Set PIN: ")

    customer = Customer(first_name, last_name, email, pin, generate_account_number())
    print("Created customer with account number:", customer._account_number)
    db.add_customer(customer)
    db.save_data()

def create_agent_account():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    pin = input("Set PIN: ")

    agent = Agent(first_name, last_name, email, pin)
    db.add_agent(agent)
    db.save_data()

def login_as_agent(agent):
    agent_pin = input("Enter agent PIN: ")
    if agent.login(input("Enter email: "), agent_pin):
        while True:
            print("\nWelcome Agent, please input your choice.")
            print("1. Transfer Funds to customer account")
            print("2. Reset customer PIN")
            print("3. Delete customer account")
            print("4. Reset account PIN")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                customer_account = input("Enter customer account number: ")
                amount = float(input("Enter amount: "))
                customer_pin = input("Enter customer PIN: ")
                agent.transfer_funds_to_customer(customer_account, amount, customer_pin, db)
            elif choice == 2:
                customer_account = input("Enter customer account number: ")
                new_pin = input("Enter new PIN: ")
                agent.reset_customer_pin(customer_account, new_pin, db)
            elif choice == 3:
                customer_account = input("Enter customer account number: ")
                agent.delete_customer_account(customer_account, db)
            elif choice == 4:
                email = input("Enter your email: ")
                old_password = input("Enter old password: ")
                new_pin = input("Enter new PIN: ")
                agent.reset_account_pin(email, old_password, new_pin, db)
            elif choice == 5:
                print("Goodbye! Contact EngrJohntegabankcustomerservices for more info.\n")
                break
            else:
                print("Invalid choice.")

def login_as_customer(customer):
    if customer.login(input("Enter email: "), input("Enter PIN: ")):
        while True:
            print("\n1. View account info")
            print("2. Transfer funds")
            print("3. Reset password")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                customer.view_account_info()
            elif choice == 2:
                recipient_account = input("Enter recipient account: ")
                amount = float(input("Enter amount: "))
                pin = input("Enter PIN: ")
                customer.transfer_funds(recipient_account, amount, pin, db)
            elif choice == 3:
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                customer.reset_pin(old_pin, new_pin)
            elif choice == 4:
                print("Goodbye! Contact EngrJohntegabankcustomerservices for more info.\n")
                break
            else:
                print("Invalid choice.")

def main():
    while True:
        print("Welcome to EngrJohntegaBank App")
        print("1. Create Customer Account")
        print("2. Create Agent Account")
        print("3. Login as Customer")
        print("4. Login as Agent")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_customer_account()
        elif choice == 2:
            create_agent_account()
        elif choice == 3:
            account_number = input("Enter account number: ")
            print("Entered account number:", account_number)
            customer = db.find_customer_by_account_number(account_number)
            if customer:
                login_as_customer(customer)
            else:
                print("Invalid account number or account not found.")
        elif choice == 4:
            email = input("Enter email: ")
            agent = db.find_agent_by_email(email)
            if agent:
                login_as_agent(agent)
            else:
                print("Invalid email or account not found.")
        elif choice == 5:
            print("Goodbye! Contact EngrJohntegabankcustomerservices for more info.\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
