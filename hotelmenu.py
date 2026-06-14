# define the menu of restaurant

menu = {

    # Breakfast
    'English_Breakfast': 550,
    'Pancake_with_Honey': 320,
    'French_Toast': 300,
    'Omelette_Plain': 220,
    'Omelette_Cheese': 280,
    'Aloo_Paratha': 300,
    'Granola_Yogurt': 350,

    # Lunch / Dinner
    'Veg_Momo': 260,
    'Chicken_Momo': 320,
    'Veg_Chowmein': 280,
    'Chicken_Chowmein': 340,
    'Veg_Pizza': 650,
    'Chicken_Pizza': 750,
    'Veg_Pasta': 520,
    'Chicken_Pasta': 620,
    'Dal_Bhat_Set': 480,

    # Snacks
    'French_Fries': 260,
    'Grilled_Sandwich': 350,
    'Veg_Burger': 420,
    'Chicken_Burger': 480,
    'Chicken_Wings': 520,
    'Nachos': 450,

    # Drinks
    'Masala_Tea': 90,
    'Milk_Tea': 100,
    'Black_Coffee': 160,
    'Cappuccino': 220,
    'Latte': 240,
    'Cold_Coffee': 280,
    'Fresh_Lemon_Soda': 220,
    'Orange_Juice': 260
}

# Greet
print(" -------------------- Welcome to Phantom Cafe Rooftop Experience -------------------- ")

print("\n -------------------- BREAKFAST -------------------- ")

print("English Breakfast      Rs550")
print("Pancake with Honey     Rs320")
print("French Toast           Rs300")
print("Omelette Plain         Rs220")
print("Omelette Cheese        Rs280")
print("Aloo Paratha           Rs300")
print("Granola Yogurt         Rs350")

print("\n --------------------  LUNCH / DINNER -------------------- ")
print("Veg Momo               Rs260")
print("Chicken Momo           Rs320")
print("Veg Chowmein           Rs280")
print("Chicken Chowmein       Rs340")
print("Veg Pizza              Rs650")
print("Chicken Pizza          Rs750")
print("Veg Pasta              Rs520")
print("Chicken Pasta          Rs620")
print("Dal Bhat Set           Rs480")

print("\n --------------------  SNACKS -------------------- ")
print("French Fries           Rs260")
print("Grilled Sandwich       Rs350")
print("Veg Burger             Rs420")
print("Chicken Burger         Rs480")
print("Chicken Wings          Rs520")
print("Nachos                 Rs450")

print("\n --------------------  DRINKS -------------------- ")
print("Masala Tea             Rs90")
print("Milk Tea               Rs100")
print("Black Coffee           Rs160")
print("Cappuccino             Rs220")
print("Latte                  Rs240")
print("Cold Coffee            Rs280")
print("Fresh Lemon Soda       Rs220")
print("Orange Juice           Rs260")


order_total = 0
ordered_items = []

while True:
    item = input("Enter the name of item you want to order = ")

    if item in menu:
        ordered_items.append(item)
        order_total += menu[item]
        print(f"{item} added to you order. Order will take 5/10 minutes to arrive")
    
    else:
        print("The item that you ordered is not available")

    another = input("Do you want to order another item? (Yes/NO)")

    if another.lower() == "no":
        break
print("\n ------------------------------- TOTAL BILL -------------------------------  ")

for food in ordered_items:
    print(f"{food} - Rs{menu[food]}")


print(f"\nTotal Amount = Rs{order_total}")





# item_1 = input("Enter the name of item you want to order = ")
# if item_1 in menu:
#     order_total += menu [item_1]
#     print("Your item {item_1} has been added to your order")

# else:
#     print(f"Ordered item [item_1] currently unavailable. Please order something esle we can serve you")

# another_order = input("Do you want to add another item in your order list? (Yes/No) ")
# if another_order == "Yes":
#     item_2 = input("Enter the name of the second item = ")
#     if item_2 in menu:
#         order_total += menu [item_2]
#         print(f"item {item_2} has been added to your order list")
#     else:
#         print(f"Ordered item {item_2} is not available!")
# print(f"The total amount of items to pay is {order_total}  ")
