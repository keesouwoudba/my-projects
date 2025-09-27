def main():
    f = get_percent()

    percent = round(f * 100)
    
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")



def get_percent(): 
    while True:
        try:
            # 1. Запрашиваем ввод и разделяем
            z = input("What's a fraction (X/Y): ")
            
            # Разделение по "/" (может вызвать ValueError, если нет "/")
            x_str, y_str = z.split("/") 
            #convert to integer format
            x = int(x_str)
            y = int(y_str)
            #check 0div
            if y == 0:
                print("division by zero")
                continue
            #chech fraction
            if x > y:
                print("incorrect fraction")
                continue
            #check positive
            if x < 0 or y < 0:
                print("all numbers must be positive")
                continue
            #now we can move forward and divide, as if some kind of error happened it would have started again
            f = x / y
            return f   
            #check whether x is less than y
            #check whether division is not by 0
            #check whether these are positive integers
        except (ValueError, ZeroDivisionError):
                print("try again")
                pass

main()




