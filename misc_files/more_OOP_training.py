class Item():
    def calculate_total_price(self, x, y): # This is creating a method
        return x * y


item1 = Item() # Creating an instance of a class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item() # Creating an instance of a class
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item1.calculate_total_price(item2.price, item2.quantity))
