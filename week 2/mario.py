def main():
    print_cube_with(get_number_row(), get_number_collumn())

def print_cube_with(row, collumn):
    #for each row in square
    for i in range(row):
        print("#" * collumn, end="")
        print()
        
def get_number_row():
    v = int(input("which size of the rows of the cube? "))
    return v
def get_number_collumn():
    n = int(input("what's the collumn size? "))
    return n


main()

