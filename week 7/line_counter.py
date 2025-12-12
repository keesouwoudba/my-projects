import sys


if len(sys.argv) !=2 or not sys.argv[1].endswith(".py"):
    sys.exit(1)

i = 0
path = sys.argv[1]

try:
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            i +=1


except FileNotFoundError:
    sys.exit(1)
            

print(f"the code has: {i} lines")