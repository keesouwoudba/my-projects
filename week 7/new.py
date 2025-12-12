import csv

name = input("whats your name: ")
home = input("where is your home: ")

with open("names.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})