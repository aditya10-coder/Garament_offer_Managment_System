from customer import Customer
from offer import GaramentOffer
from file_manager import FileManager

def main():
    print("=" * 35)
    print("GARMENT OFFER MANAGEMENT SYSTEM ")
    print("=" * 35)

    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")

    customer = Customer(customer_id, name)

    offer = GaramentOffer()
    offer.get_purchase()

    print("\n-----RESULT-----")

    print(F"Purchase Price : Rs.{offer.purchase_price}")
    print(f"Free Price     : Rs.{offer.total_free_price()}")
    
    if offer.check_offer():
        print("Offer Applied")
    else:
        print("Offer Not Allowed")

    FileManager.save_history(customer, offer)
    print("\nPurchase Saved Successfully")

    print("\nHistory")

    FileManager.view_history()

if __name__ == "__main__":
    main()
