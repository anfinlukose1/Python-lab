import csv

with open("student.csv", "r", encoding="cp1252") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
