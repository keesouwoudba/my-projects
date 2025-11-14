import requests
import json
import emoji

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=4a6a0b6de3c7f26926ba9b1efb6609a0bf69446bc440a2d98e4e0b43b8b98216")
    o = response.json()
    price = o["data"]["priceUsd"]
    price = float(price)
except Exception as e:
    print(f"error as {e}")


while True:
    try:
        allowedmodes = [1, 2]
        mode = int(input("choose mode(1) BTC->$ or 2) $->BTC) "))
        if mode not in allowedmodes:
            raise ValueError
        break
    except (ValueError, TypeError):
        print("incorrect mode chosen")


if mode == 1:
    while True:
        try:
            user_input = float(input("how many BTC do you want to buy(float e.g. 5.0)"))
            break
        except (ValueError, TypeError):
            print("incorrect format entered, try again")
    total_price = (price * user_input)
    print(emoji.emojize(f"the total price is: {total_price:,.4f}:thumbs_up:"))

elif mode == 2:
    while True:
        try:
            user_input = float(input("how much money do you have? "))
            break
        except (ValueError, TypeError):
            print("incorrect format, try again")
    total_BTC = user_input / price
    
    print(emoji.emojize(f"total BTC you can buy is: {total_BTC}:thumbs_up:"))


else:
    print("there must have been a mistake, try again")
                   