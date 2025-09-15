# Filename: PyHW2AB.py
# Date: 9/13/25
# Author: Aaron Bigby

# Store name and based info centered, will be using a print statement
# Items (input), up to 5 items  just seperate variables)



# Item 1
# Name
# Quantity
# Price
print("Please enter the 1st item:")
item1_name = input()
print(f"Please enter how many {item1_name}(s) you got:")
item1_quantity = int(input())
print(f"Please enter the price of {item1_name}:")
item1_price = float(input("$"))
print()


# Item 2
# Name
# Quantity
# Price
print("Please enter the 2nd item:")
item2_name = input()
print(f"Please enter how many {item2_name}(s) you got:")
item2_quantity = int(input())
print(f"Please enter the price of {item2_name}:")
item2_price = float(input("$"))
print()


# Item 3
# Name
# Quantity
# Price
print("Please enter the 3rd item:")
item3_name = input()
print(f"Please enter how many {item3_name}(s) you got:")
item3_quantity = int(input())
print(f"Please enter the price of {item3_name}:$")
item3_price = float(input("$"))
print()


# Item 4
# Name
# Quantity
# Price
print("Please enter the 4th item:")
item4_name = input()
print(f"Please enter how many {item4_name}(s) you got:")
item4_quantity = int(input())
print(f"Please enter the price of {item4_name}:")
item4_price = float(input("$"))
print()


# Item 5
# Name
# Quantity
# Price
print("Please enter the 5th item: ")
item5_name = input()
print(f"Please enter how many of {item5_name}(s) you got: ")
item5_quantity = int(input())
print(f"Please enter the price of {item5_name}: ")
item5_price = float(input("$"))


# Add on percentages
# Tax
print("\nPlease enter the tax:")
tax = float(input("%")) 

# Tip
print("\nPlease enter the tip:")
tip = float(input("%"))



print("\t\t\t\t\tPublix")
print("\t\t\t\tTowne Square Shopping Center")
print("\t\t\t\t11950 W. Forest Hill Blvd")
print("\t\t\t\tWellington, FL 33414")
print()
print()

# Item summary formatting
print(f"{item1_quantity} {item1_name}\t\t\t ${item1_price:.2f}")
print(f"{item2_quantity} {item2_name}\t\t\t ${item2_price:.2f}")
print(f"{item3_quantity} {item3_name}\t\t\t ${item3_price:.2f}")
print(f"{item4_quantity} {item4_name}\t\t\t ${item4_price:.2f}")
print(f"{item5_quantity} {item5_name}\t\t\t ${item5_price:.2f}")


# Subtotal calculations
item1_subtotal = item1_price * item1_quantity
item2_subtotal = item2_price * item2_quantity
item3_subtotal = item3_price * item3_quantity
item4_subtotal = item4_price * item4_quantity
item5_subtotal = item5_price * item5_quantity


# Calculations 
subtotal = item1_subtotal  + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal
tax_rate = subtotal * tax /100
tip_rate = subtotal * tip /100
net_total = subtotal + tax_rate + tip

print()
print()
print(f"\t\t\tSubtotal: ${subtotal:.2f}")
print(f"\t\t\tSales Tax: ${tax_rate:.2f}")
print(f"\t\t\tTip: ${tip:.2f}")
print(f"\n\t\t\tGrand Total: ${net_total:.2f}")

print("*********************************************************")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*                                                       *")
print("*********************************************************")



# Footer
print("\n\n\nThank you!")
print("9/13/2025 13:39")

