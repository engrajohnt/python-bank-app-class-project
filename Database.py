import random, json, string
from Customer import Customer
from Agent import Agent
random.seed(10)

def generate_account_number():
    characters = string.digits
    length = 10
    account_number = ''.join(random.choice(characters) for _ in range(length))
    return account_number

class Database:
    def __init__(self):
        self.customers = []
        self.agents = []
        self.customer_account_mapping = {}

    def add_customer(self, customer):
        self.customers.append(customer)
        self.customer_account_mapping[customer._account_number] = customer

    def find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def add_agent(self, agent):
        self.agents.append(agent)

    def find_customer_by_account_number(self, account_number):
        return self.customer_account_mapping.get(account_number, None)

    def remove_customer(self, account_number):
        if account_number in self.customer_account_mapping:
            customer = self.customer_account_mapping[account_number]
            self.customers.remove(customer)
            del self.customer_account_mapping[account_number]
            self.save_data()
            print("Customer removed: {}".format(customer.email))
        else:
            print("Customer account not found.")

    def find_agent_by_email(self, email):
        for agent in self.agents:
            if agent.email == email:
                return agent
        return None

    def save_data(self):
        data = {
            "customers": [customer.__dict__ for customer in self.customers],
            "agents": [agent.__dict__ for agent in self.agents]
        }
        with open('data.json', 'w') as file:
            json.dump(data, file,indent=4)

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                for customer_data in data["customers"]:
                    print("Loaded customer account number:",generate_account_number())
                    self.add_customer(Customer(**customer_data))

                for agent_data in data["agents"]:
                    self.add_agent(Agent(**agent_data))
        except FileNotFoundError:
            pass  # Handle the case where the data file does not exist
