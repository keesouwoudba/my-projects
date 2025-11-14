def main():
    user_input = input("what do you want to send: ")
    print(shorten(user_input))

def shorten(user_input):
    vowels = {"a", "o", "u", "i", "e", "A", "O", "U", "I", "E", "y", "Y" }
    word = ""
    for letter in user_input:
        if letter in vowels:
            letter = ""
        word += letter
    return word
if __name__ == "__main__":
    main()