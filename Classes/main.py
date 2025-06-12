import csv
import truck
import package

from hashTable import hashtable

packagetable = hashtable()

with open("SupportingDocument/WGUPS Package File.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # Skip header row
    for row in reader:
        id =  row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        new_package = package.package(id, address, city, state, zip_code,deadline, float(weight))
        packagetable.insert(new_package.ID, new_package)

with open("SupportingDocument/WGUPS Distance Table.csv") as file:
    distance_reader = csv.reader(file, delimiter=',')


class Main:
    print("Welcome to the WGUPS Package Management System")
    for i in range(1, 41):
        print(f"Package {i}: {packagetable.get(str(i))}")