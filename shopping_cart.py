# shopping_cart.py

import operator
import datetime
import tkinter

import os

Tax_Rate = float(os.getenv("sales_tax", default = "0.07"))


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

Company_name = "Samantha's Grocery"
Company_website = "www.SamanthaGrocery.com"
now = datetime.datetime.now()
Closing_message = "Thanks for shopping with us!"


# TODO: write some Python code here to produce the desired output

#Capture Products Being Purchased (ie. scan)

selected_ids = []

while True:
    selected_id = input("Please select / scan a valid product id or 'DONE':")
    if selected_id.upper() == "DONE":
        break
    else:
        selected_ids.append(selected_id)


selected_ids_count = len(selected_ids) 

print("------------------------------------------------")
print()
print(Company_name)
print(Company_website)
print()
print("------------------------------------------------")
print()
print("Time of Transaction: ", now.strftime('%Y-%m-%d %H:%M'))
print()
print("------------------------------------------------")
print()
print("Items Purchased: ")
print()

# Compile list of the products purchased and print
for selected_id in selected_ids:
  
    matching_products = [p for p in products if str(p["id"]) == selected_id]
    matching_product = matching_products[0]
    print(str(matching_product["name"]) +"---(" + str(to_usd(matching_product["price"])) + ")")

#print total number of products purchased (so customer can confirm)

print()
print("------------------------------------------------")
print()
print(f"Total Products Purchased: {selected_ids_count}")   

#Calculate subtotal

price= []

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == selected_id]
    matching_product = matching_products[0]
    price.append(matching_product["price"])

sub_total = (sum(price))

print("Item Subtotal: ", to_usd(sub_total))

#calculate Tax Rate

Tax = sub_total * Tax_Rate

print("Total Tax: ", to_usd(Tax))

#Calculate total

Total = sub_total + Tax

print("Total: ",to_usd(Total))

print()
print("------------------------------------------------")
print()
print(Closing_message)
print()
print("------------------------------------------------")





