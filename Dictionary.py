words_dict = {}
while True:
    word = input("what to add? ")
    try:
        if word == "STOPHERE": 
            break
        else:
            count_current = words_dict.get(word, 0) + 1
            words_dict[word] = count_current

    except EOFError:
        break

keyz = words_dict.keys()
sorted_keys = sorted(keyz)

for word in sorted_keys:
    counter = words_dict[word]
    print(f"{counter} {word.upper()}")
