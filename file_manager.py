class FileManager:
    FILE_NAME = "purchase_history.txt"

    @classmethod
    def save_history(cls, customer, offer):

        with open(cls.FILE_NAME, "a") as file:
            
            file.write(
                f"{customer.customer_id},{customer.name},{offer.purchase_price},{offer.total_free_price()}\n"
            )

    @classmethod
    def view_history(cls):

        try:
            with open(cls.FILE_NAME, "r") as file:
                 
                 print("\nPurchase History")
                 print("----------------")

                 for line in file:
                     print(line.strip())

        except FileNotFoundError:
            print("No purchase histroy found")