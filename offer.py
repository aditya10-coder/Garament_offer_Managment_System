class GaramentOffer:

    def __init__(self):
        self.purchase_price = 0
        self.free_prices = []

    def get_purchase(self):
        self.purchase_price = float(input("Enter purchase price: "))
        n= int(input("Enter Number of Free grament: "))

        self.free_prices.clear()
        
        for i in range(n):
            price = int(input(f"Enter price of Free Garment {i+1}: "))
            self.free_prices.append(price)

    def total_free_price(self):
        return sum(self.free_prices)
    
    def check_offer(self):
        total = self.total_free_price()

        if total <= self.purchase_price:
            return True
        return False
