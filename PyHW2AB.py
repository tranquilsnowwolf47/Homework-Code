# Store name and based info centered, will be using a print statement
# Items (input), up to 5 items (not using a for loop, just seperate variables)




# Name
# Quantity
# Price
print("Please enter the 1st item:")
item1_name = input()
print(f"Please enter how many {item1_name}(s) you got:")
item1_quantity = int(input())
print(f"Please enter the price of {item1_name}:")
item1_price = float(input())
print()


# Name
# Quantity
# Price
print("Please enter the 2nd item:")
item2_name = input()
print(f"Please enter how many {item2_name}(s) you got:")
item2_quantity = int(input())
print(f"Please enter the price of {item2_name}:")
item2_price = float(input())
print()


# Name
# Quantity
# Price
print("Please enter the 3rd item:")
item3_name = input()
print(f"Please enter how many {item3_name}(s) you got:")
item3_quantity = int(input())
print(f"Please enter the price of {item3_name}:")
item3_price = float(input())
print()


# Name
# Quantity
# Price
print("Please enter the 4th item:")
item4_name = input()
print(f"Please enter how many {item4_name}(s) you got:")
item4_quantity = int(input())
print(f"Please enter the price of {item4_name}:")
item4_price = float(input())
print()


# Name
# Quantity
# Price
print("Please enter the 5th item: ")
item5_name = input()
print(f"Please enter how many of {item5_name}(s) you got: ")
item5_quantity = int(input())
print(f"Please enter the price of {item5_name}: ")
item5_price = float(input())




print("\t\t\t\t\tPublix")
print("\t\t\t\tTowne Square Shopping Center")
print("\t\t\t\t11950 W. Forest Hill Blvd")
print("\t\t\t\tWellington, FL 33414")
print()

print("Item summary:")
print(f"{item1_quantity} {item1_name}\t\t  {item1_price:.2f}")
print(f"{item2_quantity} {item2_name}\t\t\t   {item2_price:.2f}")
print(f"{item3_quantity} {item3_name}\t\t\t  {item3_price:.2f}")
print(f"{item4_name}\t\t\t {item4_quantity}  {item4_price:.2f}")
print(f"{item5_name}\t\t\t {item5_quantity}  {item5_price:.2f}")

print("Total summary:")
item1_subtotal = item1_price * item1_quantity
item2_subtotal = item2_price * item2_quantity
item3_subtotal = item3_price * item3_quantity
item4_subtotal = item4_price * item4_quantity
item5_subtotal = item5_price * item5_quantity



tax = .07
subtotal = item1_subtotal  + item2_subtotal + item3_subtotal + item4_subtotal + item5_subtotal

