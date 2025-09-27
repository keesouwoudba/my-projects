items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00, 
    "French Fries" : 9.00,
    "Rice" : 5.00, 
    "Ketchup" : 1.00,
    "Nuggets" : 5.00
}
z = 0
total = float(0.00)
while True:
    try:   
        if z == 0 :
            ordered_item = input("What do you want to order? ")
            ordered_item = ordered_item.title()
            z += 1 
        elif z >= 1:
            ordered_item = input("what else do you want to order?")
            ordered_item = ordered_item.title()
        
        if ordered_item == "Nothing" or ordered_item == "":
            break   

        temp_var_for_price = float(items[ordered_item])
        print(f"you ordered: {ordered_item} , price: {temp_var_for_price}")
        total += temp_var_for_price
        print(f"your total is {total}")
    except KeyError:
        print("no such item exists in our menu")
        pass
    

print(f"Total: {total:.2f}")


