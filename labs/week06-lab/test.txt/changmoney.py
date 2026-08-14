def changmoney(value,currency) :
    if currency == "USD":
        money = value * 3300
        print(f"{value} THB = {money}THB")
        

        
    elif currency == "THB":
        money = value / 33
        print(f"{value} USD = {money} THB")
        
        

changmoney(100,"THB")
changmoney(100,"USD")


