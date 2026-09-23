import csv

cislo = 0
cases = {}

for i in range(1,10):
    cases[i] = 0

fr = open('data.csv')
csv_reader = csv.reader(fr, delimiter=',')
for row in csv_reader:
    if str(row[5]) == "NA" and type(row[5]) != int:
        row[5] = 0
    else:
        cislo = int(str(row[5])[0])
        cases[cislo] += 1

print(cases)