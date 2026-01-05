class ItemToPurchase:
    #initilizing default values. Steps 1-3
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        #adding item description for steps 4-6
        self.item_description = "none"
    
    def print_item_cost(self):
        #adding methods to class. part of steps 1-3
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        
class ShoppingCart:
     #initializing default values. Steps 4-6
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        #add an ItemToPurchase to cart_items list
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        #removes item from cart_items, if the item is not found in the cart then it returns a message
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        #modifies item's description, price, and/or quantity in cart_items. If the item wasn't found print a message
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
            if item_to_purchase.item_price != 0:
                item.item_price = item_to_purchase.item_price
            if item_to_purchase.item_quantity !=0:
                item.item_quantity = item_to_purchase.item_quantity
            return
        print("Item not found in cart. Nothing modified.")
        
    def get_num_items_in_cart(self):
        #Returns quanitiy of item in cart
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        #determines total cost of items in cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        #outputs total of items in cart. If there are no items in cart print a message
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item_total = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item_total:.2f}")
            print()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        #outputs items descriptions
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
    
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    #adding a menu where the user input will call a method to run for the shopping cart
    choice = ''

    while choice != 'q':
        print("Menu")
        print("a - Add item to the cart")
        print("r - Remove item from the cart")
        print("c - Change item quantity")
        print("i - Output item description")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        choice = input("Choose an option: ")
            
        if choice == 'a':
            # if choice 'a' add item
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name: " )
            item.item_description = input("Enter the item description: ")
            item.item_price = float(input("Enter the item price: "))
            item.item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(item)
            print()
                    
        elif choice == 'r':
            #if choice 'r' removem item
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter the item name: ")
            cart.remove_item(item_name)
            print()

        elif choice == 'c':
            #if choice 'c' change quantity
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase()
            item.item_name = item_name
            item.item_quantity = new_quantity
            cart.modify_item(item)
            print()
                                   
        elif choice == 'i':
            #if choice 'i' output description
            print("OUTPUT ITEM DESCRIPTION")
            cart.print_descriptions()
            print()
                
        elif choice == 'o':
            #if choice 'o' output cart
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            print()

        elif choice == 'q':
            #if choice 'q' quit loop
            break
        else:
            print("Invalid input. Try again.")

def main():
    #get information from user
    customer_name = input("Enter customer name: ")
    current_date = input("Enter today's date - format month day, year: ")
    print()
    print(f"Customer's name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    #create cart
    cart = ShoppingCart(customer_name, current_date)
    #display menu
    print_menu(cart)

if __name__ == "__main__":
        main()

        
        
