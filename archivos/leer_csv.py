import csv
with open("archivos\\datos.csv", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)