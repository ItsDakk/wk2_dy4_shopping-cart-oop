# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program


## Backend ##
## Show, Add, Remove, Clear ##

cart = []

class Cart():

    def show_cart(self):
        print("Here is what is in your Cart so far: ")
        for item in cart:
            print(item)
        if not cart:
            print("Your Cart is empty")
        pass

    def add_item(self, item):
        cart.append(item)
        print(f"{item} has been added to your Cart")
        

    def remove_item(self, item):
        cart.remove(item)
        print(f"{item} has been removed to your Cart")
        
    def quit_shopping(self):
        print("Thank you for shopping at PYExpress! Here is a list of your items:")
        for item in cart:
            print(item)
        

## Front ##
## UI ##

class UI():

    def __init__(self, cart):
        self.cart = cart
        pass

    def execute_program(self):
            while True: 
                user_opt = input("What would you like to do? \n(Type in just one of these options [Show/Add/Remove/Quit])\n").strip() 
                if user_opt.lower().strip() == 'show':
                    self.cart.show_cart()
                elif user_opt.lower().strip() == 'add':
                    item = input("What would you like to add? ").strip()
                    self.cart.add_item(item)
                elif user_opt.lower() == 'remove':
                    item = input("What item would you like to remove? ").strip()
                    self.cart.remove_item(item)
                elif user_opt.lower() == 'quit':   
                    self.cart.quit_shopping()
                    

shopper1 = Cart()
ui = UI(shopper1)
ui.execute_program()
        
        
            
