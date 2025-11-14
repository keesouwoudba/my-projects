def main():
    plate = input("what's plate: ")
    if is_valid(plate):
        print("Valid!")
    else:
        print("Invalid!!")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        print("too long or too short")
        return False
    if not s[:2].isalpha():
        print("first 2 characters are not letters")
        return False
    if not s.isalnum():
        print("does contain inappropriate characters")
        return False
    first_digit_index = -1
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break
    if first_digit_index == -1:
        return True
    if s[first_digit_index] == "0":
        print("first digit is zero")
        return False
    if not s[first_digit_index:].isdigit():
        print("contains letters after numbers")
        return False
    return True

if __name__ == "__main__":
    main()