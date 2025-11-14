fruits = { 
    "Apple" : 130 ,
     "Avocado" : 50 ,
     "Banana" : 110 ,
     "Grapefruit" : 60 ,
     "Grapes" : 90 ,
     "Lemon" : 15 
 }
def main():

    x = fruits[get_name()]
    
    for i in range(x):
        print(f"the amount of calories is {x}" )

def get_name():
    name = input("what's fruit name? ")
    name = name.capitalize()
    return name

main()