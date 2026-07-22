'''#a = 15
#b = 5
#print(a + b)

#arithmatic operators

# Addition
a = 15
b = 5
print(a + b)  # Output: 20

# Subtraction
print(a - b)  # Output: 10

# Multiplication
print(a * b)  # Output: 75

# Division
print(a / b)  # Output: 3.0

# Modulus
print(a % b)  # Output: 0

# Exponentiation
print(a ** b)  # Output: 759375

'''
 #Assignment Operators
'''
a = 10
 
a += 5 
print(a)

a-= 2
print(a)

a*= 3
print(a)'''

#comparison operators
'''
a = 10
b = 5

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False
'''

# Logical Operators
'''a = 10
b = 20

print(a < b and b > a)
print(a < b or b < a)
print(not(a < b))
'''

# Membership Operators
'''
name = "python"

print("p" in name)
print("z"not in name)'''
      
 # Types of Type Casting
 #Implicit Type Casting

'''a = 10
b = 5.5

c = a + b

print(c)  # Output: 15.5
print(type(c))'''


# MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.__name = name        # Private attribute
        self.__price = price      # Private attribute

    # Getter methods
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


# Order class
class Order:
    TAX_RATE = 0.05  # 5% tax

    def __init__(self):
        self.__items = []  # Private list to store menu items

    # Method to add menu item to the order
    def add_item(self, menu_item):
        self.__items.append(menu_item)
        print(f"{menu_item.get_name()} added to order.")

    # Method to compute total bill including tax
    def compute_total(self):
        subtotal = sum(item.get_price() for item in self.__items)
        tax = subtotal * Order.TAX_RATE
        total = subtotal + tax
        return subtotal, tax, total

    # Method to display the bill
    def print_bill(self):
        print("\n--- Order Bill ---")
        for item in self.__items:
            print(f"{item.get_name():20} ${item.get_price():.2f}")
        subtotal, tax, total = self.compute_total()
        print(f"{'Subtotal':20} ${subtotal:.2f}")
        print(f"{'Tax (5%)':20} ${tax:.2f}")
        print(f"{'Total':20} ${total:.2f}")
        print("------------------\n")


# Example usage
# Create menu items
burger = MenuItem("Burger", 8.50)
pizza = MenuItem("Pizza", 12.00)
coffee = MenuItem("Coffee", 3.50)

# Create an order
order1 = Order()
order1.add_item(burger)
order1.add_item(pizza)
order1.add_item(coffee)

# Print the bill
order1.print_bill()