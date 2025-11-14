import inflect
p = inflect.engine()

list_of_names = []




while True:
    try:
        userinput = input("name: ")
        if not userinput or not userinput.isalpha():
            raise ValueError
        
        if userinput.lower() == "break":
            break
        else:
            list_of_names.append(userinput)
    except (ValueError, IndexError, TypeError, NameError):
        print("error")
        continue

goodbye = "Adieau to: "
x = p.join(list_of_names)
print(goodbye + x) 