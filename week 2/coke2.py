money_paid = 0
cola_price = 50
valid_coins = [5,10,25,50]
while money_paid < cola_price:
    money_inserted = int(input("insert coin: "))
    if money_inserted not in valid_coins:
        print("no such coin exist, your coin is rejected")
        continue
    else:
        money_paid += money_inserted
        print(f"you paid:{money_paid}")
change = money_paid - cola_price
print(f"your change is: {change}, please take your cola!")

