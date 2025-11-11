class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
           
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name:")
item1.item_price = float(input("Enter the item price:"))
item1.item_quantity = int(input("Enter the item quantity:"))
    
print("Item 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name:")
item2.item_price = float(input("Enter the item price:"))
item2.item_quantity = int(input("Enter the item quantity:"))
    
print("Total Cost:")
item1.print_item_cost()
item2.print_item_cost()
    
total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${total:.2f}")
