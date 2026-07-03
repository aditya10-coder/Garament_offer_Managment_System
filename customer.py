class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
    
    def display(self):
        print("\nCustomer Details")
        print("------------------")
        print(f"ID   :  {self.customer_id}")
        print(f"name :  {self.name}")
        