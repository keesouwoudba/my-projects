def main():
    while True:
        try:
            z = input("What's a fraction (X/Y): ")
            z = get_percent(z)
            break
        except (ValueError, ZeroDivisionError, TypeError):
            continue
    print(f"{gauge(z)}")



def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return (f"{percent}%")



def get_percent(z): 
        try:
            p = 0
            for char in z:
                if char == "/":
                    p+=1
            if p > 1:
                raise ValueError
            x_str, y_str = z.split("/") 
            x = int(x_str)
            y = int(y_str)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                #print("incorrect fraction")
                raise ValueError
            if x < 0 or y < 0:
                #print("all numbers must be positive")
                raise ValueError 
            f = x / y
            percent = round(f * 100)
            return percent
        except (ZeroDivisionError, ValueError):
            raise


if __name__ == "__main__":
    main()




