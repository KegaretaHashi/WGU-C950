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
    reader = csv.reader(file, delimiter=',')
    distances = list(reader)

with open("SupportingDocument/addresslegend.csv") as file:
    reader = csv.reader(file, delimiter=',')
    address_legend = list(reader)

def translate_address(address):
    for row in address_legend:
        if address in row[2]:
            return int(row[0])

def get_distance(address1, address2):
    distance = 0.0
    for row in distances:
        if row[0] == address1:
            distances[row[1]] = float(row[2])
        elif row[0] == address2:
            distances[row[1]] = float(row[2])
    return distance


def deliver_packages(truck):
    for package_id in truck.get_packages():
        next_address = float('inf')
        next_package = None
        package = packagetable.get(package_id)
        if package.status == 'At The Hub' or package.status == 'In Transit':
            if get_distance(translate_address(truck.address), translate_address(package.address)) <= next_address:
                next_address = get_distance(translate_address(truck.address), translate_address(package.address))
                next_package = package
            package.update_status('Delivered')
            truck.unload_package(package)
            truck.current_location = package.address    
            truck.distance_traveled += next_address
            truck.address = package.address
            print(f"Truck {truck.truck_id} delivered package {package.ID} to {package.address}.")

class Main:
    print(packagetable.get(str(1)).status())
    
    
    packagetable.get(str(3)).update_status('Delivered')
    print(packagetable.get(str(3)))