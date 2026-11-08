# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Jacob Lackey

# REFLECTION QUESTIONS

# 1. I would use .get() when a key might not exist because it allows the program to return a default value instead of crashing. I would use bracket notation when I know the key exists.
# 2. Exercise 8 reminds me of using SUMIF in Excel because it adds values. Python can be more useful for large datasets because it can automatically process and organize large amounts of information using loops.


# EXERCISE 1 - One customer
customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1500
}
print("\nEXERCISE 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2 - Update and add
print("\nEXERCISE 2")
customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)


# EXERCISE 3 - Safe lookup
print("\nEXERCISE 3")
email = customer.get("email", "no email on file")
print(email)
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 - Iterate
print("\nEXERCISE 4")
for key, value in customer.items():
    print(f"{key}: {value}")
# Without .items(), the loop only gives you the keys.
for key in customer:
    print(key)


# EXERCISE 5 - Lookup table
print("\nEXERCISE 5")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
discount = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
final_price = purchase_price * (1 - discount)
print("Tier:", customer["tier"])
print("Discount rate:", discount * 100, "%")
print("Final price: $", round(final_price, 2))


# EXERCISE 6 - List of dictionaries

print("\nEXERCISE 6")

customers = [
    {"name": "Alice", "tier": "bronze"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "gold"}
]

for customer_info in customers:
    discount_rate = tier_discounts.get(customer_info["tier"], 0)
    discount_amount = 300 * discount_rate

    print(
        customer_info["name"],
        customer_info["tier"],
        "Discount: $",
        round(discount_amount, 2)
    )


# EXERCISE 7 - Nested catalog

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print("LOW STOCK:", product)


# EXERCISE 8 - Sales by region

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(region + ":", sales_summary[region])