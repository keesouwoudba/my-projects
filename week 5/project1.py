import random
import emoji


def main():
    myfunction_type = get_function()
    mylevel = get_level()
    mynumber_of_problems = get_num()
    get_problems_and_solve(myfunction_type, mylevel, mynumber_of_problems)


def get_function():
    possible_functions = ["+", "-", "*", "/"]
    
    while True:
        try:
            user_input = input("choose type from +, -, / and *:")
            if user_input not in possible_functions:
                raise ValueError
            else:
                return user_input
        except (ValueError, TypeError):
            print(emoji.emojize(f":cross_mark: choose approptiate function from +, -, / and *"))
            continue

def get_level():
    levels = [1, 2, 3, 4]
    while True:
        try:
            user_input = int(input("choose level(1 to 4) :"))
            if user_input not in levels:
                raise ValueError
            else:
                return user_input
        except (ValueError, TypeError):
            print("choose appropriate level")
            continue

def get_num():
    while True:
        try:
            user_input = int(input("choose the number of problems: "))
            if not 0 < user_input < 100 :
                raise ValueError
            else:
                return user_input
        except (ValueError, TypeError):
            print("choose appropriate number")
            continue


def get_problems_and_solve(functiontype, level, number_of_problems):
    variables_dict = generate_random_pairs_to_solve(level, functiontype, number_of_problems)
    try:
        for i in range(1, (number_of_problems+1)):
                x = variables_dict[0][f"x{i}"]
                y = variables_dict[1][f"y{i}"]
                show_the_problem(x, y, functiontype)
                z = 1
                while True:
                    try:
                        user_answer = int(input("answer: "))
                        result = iscorrect(x, y, functiontype, user_answer)
                        if result == True:
                            print(emoji.emojize("congrats :1st_place_medal:, correct :fire:"))
                            break
                        elif z >= 3:
                            help_the_user(x, y, functiontype)
                        else:
                            z += 1
                            print(emoji.emojize("incorrect :cross_mark:"))
                    except (ValueError, TypeError):
                        print(emoji.emojize(":cross_mark: no cheating, man!"))
                        z+=1

    except:
        print("error happened in the stage of get_problems_and_solve, end the programm and try again")

def generate_random_pairs_to_solve(level, functiontype, number_of_problems):
    try:
        if level == 1: max = 10   
        elif level == 2: max = 50   
        elif level == 3: max = 100  
        elif level == 4: max = 200
            

        if functiontype == "/" or functiontype == "-":       
            xvariables_dict = {}
            yvariables_dict = {}
            for i in range(1, (number_of_problems+1)):
                try:
                    while True:
                        x = random.randint(0, max)
                        y = random.randint(0, max)
                        if y == 0 or x<y or x%y != 0:
                            continue
                        else:
                            break
                    xvariables_dict[f"x{i}"] = x 
                    yvariables_dict[f"y{i}"] = y
                except:
                    continue
        elif functiontype == "*" or functiontype == "+":
            xvariables_dict = {}
            yvariables_dict = {}
            for i in range(1, (number_of_problems+1)):
                try:
                    while True:
                        x = random.randint(0, max)
                        y = random.randint(0, max)
                        xvariables_dict[f"x{i}"] = x 
                        yvariables_dict[f"y{i}"] = y
                        break
                except:
                    continue
        variables_dict = [xvariables_dict, yvariables_dict]      
        return variables_dict
    except:
        print("error in get random pairs")

def show_the_problem(x, y, functiontype):
    if functiontype == "+":
        print(f"{x}+{y}")
    elif functiontype == "-":
        print(f"{x}-{y}")
    elif functiontype == "/":
        print(f"{x}/{y}")
    elif functiontype == "*":
        print(f"{x}*{y}")
    else:
        print("sorry man, error is in the show the problem(), try again")

def iscorrect(x, y, functiontype, user_answer):
    correct = None
    if functiontype == "+":
        correct = x+y 
    elif functiontype == "-":
        correct = x-y 
    elif functiontype == "/":
        correct = x/y 
    elif functiontype == "*":
        correct = x*y 
    else:
        print("sorry man, error is in the iscorrect stage")
        return False
    
    
    return (user_answer == correct)

def help_the_user(x, y, functiontype):
    if functiontype == "+":
        correct = x+y 
    elif functiontype == "-":
        correct = x-y 
    elif functiontype == "/":
        correct = x/y 
    elif functiontype == "*":
        correct = x*y 
    else:
        print("sorry man, error is in the help the user stage")

    print(f"the correct answer is: {correct}")


main()

