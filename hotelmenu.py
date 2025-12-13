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
print("🌆 Welcome to Phantom Cafe – Rooftop Experience 🌆")

print("\n--- Breakfast ---")
print("English_Breakfast Rs550\nPancake_with_Honey Rs320\nFrench_Toast Rs300\nOmelette_Plain Rs220\nOmelette_Cheese Rs280\nAloo_Paratha Rs300\nGranola_Yogurt Rs350")

print("\n--- Lunch / Dinner ---")
print("Veg_Momo Rs260\nChicken_Momo Rs320\nVeg_Chowmein Rs280\nChicken_Chowmein Rs340\nVeg_Pizza Rs650\nChicken_Pizza Rs750\nVeg_Pasta Rs520\n Chicken_Pasta Rs620 | Dal_Bhat_Set Rs480")

print("\n--- Snacks ---")
print("French_Fries Rs260\nGrilled_Sandwich Rs350\nVeg_Burger Rs420\nChicken_Burger Rs480\nChicken_Wings Rs520\nNachos Rs450")

print("\n--- Drinks ---")
print("Masala_Tea Rs90\nMilk_Tea Rs100\nBlack_Coffee Rs160\nCappuccino Rs220\nLatte Rs240\nCold_Coffee Rs280\nFresh_Lemon_Soda Rs220\nOrange_Juice Rs260")
order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu [item_1]
    print("Your item {item_1} has been added to your order")

else:
    print(f"Ordered item [item_1] currently unavailable. Please order something esle we can serve you")

another_order = input("Do you want to add another item in your order list? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total += menu [item_2]
        print(f"item {item_2} has been added to your order list")
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of items to pay is {order_total}  ")
