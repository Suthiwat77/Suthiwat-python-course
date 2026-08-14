product_price=[]

product_price1 = int(input("price 1 :"))
product_price2 = int(input("price 2 :"))
product_price3 = int(input("price 3 :"))
product_price4 = int(input("price 4 :"))
product_price5 = int(input("price 5 :"))
product_price6 = int(input("price 6 :"))

product_price.append(product_price1)
product_price.append(product_price2)
product_price.append(product_price3)
product_price.append(product_price4)
product_price.append(product_price5)
product_price.append(product_price6)

Total_budget=int(input("Total_budget :"))
x=Total_budget
canbuy_product=[]
print("============================")
for i in range(6):
    if Total_budget >= product_price[i]:
        print(f"buy item{i+1} price",product_price[i])
        Total_budget = Total_budget - product_price[i]
        canbuy_product.append(product_price[i])
        print("Money left over",Total_budget,"\n")
    else:
        print("cannot buy\n")
print("============================")
print("bought item :",canbuy_product)
print("total spent :",x-Total_budget)
print("remaining budget :",Total_budget)