# Vending Machine Program

# Product list: Product ID -> (Name, Price)
goods = {
    1: ("Water", 2.5),
    2: ("Orange Juice", 4.0),
    3: ("Chips", 3.0),
    4: ("Chocolate", 5.5),
    5: ("Coffee", 6.0),
    6: ("Soft Drink", 2.5),
    7: ("Ice Cream", 4.5),
    8: ("Indomie", 1.5),
    9: ("Cream Cheese", 7.5),
   10: ("Barnacles", 9),
   11: ("Milk", 6),
   12: ("Yogurt", 2),
   13: ("Nestle", 5),
   14: ("Mars", 1.5),
   15: ("Tuna", 6),
   16: ("Ketchup", 7),
   17: ("Mayonnaise", 6),
   18: ("Burger", 10),
   19: ("Toast", 3.5),
   20: ("Samoli Bread", 1),
}

balance = 0.0

print("================================")
print("     Welcome to Vending Machine ")
print("================================")

# Display all goods
print("\nAvailable goods:")
for pid, (name, price) in goods.items():
    print(f"{pid}. {name} - {price} SAR")

try:
    # Step 1: Select product code first
    choice = int(input("\nSelect goods number: "))

    if choice not in goods:
        print("Invalid goods selection.")

    else:
        goods_name, goods_price = goods[choice]

        print(f"\nYou selected: {goods_name}")
        print(f"Price: {goods_price} SAR")

        # Step 2: Insert money after selecting product
        while balance < goods_price:
            try:
                money = float(input("Insert money (SAR): "))
                if money <= 0:
                    print("Please insert a valid amount.")
                else:
                    balance += money
                    print(f"Current balance: {balance} SAR")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Step 3: Dispense product
        balance -= goods_price
        print("\n----------------------------")
        print(f"Dispensing: {goods_name}")
        print(f"Remaining balance: {balance} SAR")
        print("Thank you for your purchase!")
        print("----------------------------")

except ValueError:
    print("Invalid input. Please enter a number.")

# Step 4: Return change
print("\nReturning change...")
print(f"Change returned: {balance} SAR")
print("Machine ready for next customer.")
