import random 
import emoji

def get_random_number():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                raise ValueError
            random_number = random.randint(1, n)
            return random_number
        except (ValueError, TypeError):
            continue

def guess_number(random_number):
    while True:
        try:
            guess_num = int(input("guess: "))
            if guess_num > random_number:
                print("too big")
            elif guess_num < random_number:
                print("too small")
            else:
                print(emoji.emojize(f"Congrats! :1st_place_medal:, you have guessed correct :fire:"))
                break
        except (ValueError, TypeError):
            continue

limmit = get_random_number()

guess_number(limmit)
