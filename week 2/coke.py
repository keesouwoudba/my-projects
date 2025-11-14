money_paid = 0
cola_price = 50
valid_coins = [5, 10, 25] 

while money_paid < cola_price:
    
    amount_due = cola_price - money_paid
    print(f"Amount Due: {amount_due} cents") 
    
    try:
        money_inserted = int(input("Insert coin (5, 10, or 25): "))
    except ValueError:
        print("Invalid input. Please insert a valid coin value.")
        continue

    if money_inserted not in valid_coins:
        print(f"{money_inserted} cents is not an accepted denomination. Coin rejected.")
        continue
    else:
        money_paid += money_inserted


change = money_paid - cola_price

print("---")
print("Transaction successful!")
if change > 0:
    print(f"Your change is: {change} cents. Please take your cola!")
else:
    print("No change owed. Please take your cola!")

