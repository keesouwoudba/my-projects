import sys
import csv
 
if len(sys.argv) != 3:
    sys.exit("too few or many args")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith("csv"):
    sys.exit("the files are not csv extension")

read_path = sys.argv[1]
write_path = sys.argv[2]


final = []
try:
    with open(read_path, "r") as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            house = row["house"]
            lname, fname = (row["name"]).split(",")
            final.append({"last name" : lname, "first name" : fname, "house" : house })
        
    with open(write_path, "w", newline="") as writefile:
        writer = csv.DictWriter(writefile, fieldnames=["last name", "first name", "house"])
        writer.writeheader()
        for eachrow in final:
            writer.writerow(eachrow)


except Exception as e:
    sys.exit(f"error {e} occurred")

        




