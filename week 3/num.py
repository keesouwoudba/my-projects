def main():
    x = getint("whats x? ")
    print(f"x is {x}")

def getint(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            
main()