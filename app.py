import streamlit as st
st.title(" Phantom Cafe Rooftop Experience ")
st.write(" Welcome to Phantom Cafe !")

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
st.header(" Menu")

for item, price in menu.items():
    st.write(
        item.replace("_"," "),
        f"Rs {price}"
    )
selected_item = st.selectbox(
    "Choose your food",
    list(menu.keys())
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=1
)

if "cart" not in st.session_state:
    st.session_state.cart = []

if st.button("Add to Cart"):

    for i in range(quantity):
        st.session_state.cart.append(selected_item)

    st.success("Item Added!")

    st.header(" Your Order")

total = 0

for food in st.session_state.cart:
    st.write(
        food.replace("_"," "),
        "- Rs",
        menu[food]
    )

    total += menu[food]
st.subheader(f"Total Bill : Rs {total}")