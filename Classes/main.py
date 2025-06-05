import csv
import truck
import package

from hashTable import hashtable
# Initialize the hash table for packages
packagetable = hashtable()

with open("SupportingDocument/WGUPS Package File.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # Skip header row
    for row in reader:
        package_id =  row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        new_package = package.package(package_id, address, city, state, zip_code,deadline, float(weight))
        packagetable.insert(new_package.ID, new_package)
        print(f"Package {new_package.ID} loaded into the package table.")

class Main:
    print("Welcome to the WGUPS Package Management System")
    for i in range(1, 41):
        print(f"Package {i}: {packagetable.get(str(i))}")