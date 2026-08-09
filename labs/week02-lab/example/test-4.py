# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
subtotal = item_price * quantity

# TODO: Calculate discount amount
discount = subtotal *(discount_percent/100)
# TODO: Calculate price after discount
price = subtotal - discount
# TODO: Calculate tax amount
tax = price * (tax_percent/100)
# TODO: Calculate final total
finaltotal = price + tax
# TODO: Display itemized receipt

print("subtotal :", subtotal)
print("discout: ",discout)
print("price after discout :",price)
print("tax :",tax)
print("final total",finaltotal)

