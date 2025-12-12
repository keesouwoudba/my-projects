import tabulate
import sys
import csv


if len(sys.argv) != 2:
    sys.exit("too few or many command line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("the file does not end with .csv")
path = sys.argv[1]

table = []
try:
    with open(path, "r" ) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="latex"))

except FileNotFoundError:
    sys.exit("file was not found")
