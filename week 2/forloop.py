def main():
    print(convert(camel_input()))

def camel_input():
    i = input("what's camel input? ")
    return i

def convert(strings):
    word = ""
    word = word + strings[0]
    for char in strings[1:]:
        if char.isupper():
            word += "_" + char
        else:
            word += char

    word = word.upper()
    word = word.replace(" ", "_")
    return word



main()
