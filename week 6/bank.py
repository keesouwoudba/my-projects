def main():
    userinput = input("Greeting: ").lower()
    print(f"you got: ${greeting(userinput)}")
    



def greeting(userinput):
    if "hello" in userinput[0:5]:
        return 0
    elif userinput[0] == "h":
        return 20
    else:
        return 100
    
if __name__ == "__main__":
    main()


