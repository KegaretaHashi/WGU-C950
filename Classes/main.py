import csv
import truck
import package

from hashTable import hashtable
from datetime import timedelta

packagetable = hashtable()

with open("SupportingDocument/WGUPS Package File.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # Skip header row
    for row in reader:
        id =  int(row[0])
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
    #print(distances)

with open("SupportingDocument/addresslegend.csv") as file:
    reader = csv.reader(file, delimiter=',')
    address_legend = list(reader)

def translate_address(address):
    for row in address_legend:
        if address in row[2]:
            return int(row[0])

def get_distance(address1, address2):
    distance = distances[address1][address2]
    if distance == '':
        distance = distances[address2][address1]

    return float(distance)

def deliver_packages(truck, start_time):
    while truck.get_packages():
        current_location = truck.current_location
        truck.current_time = start_time
        min_distance = float('inf')
        next_package_id = None
        next_package = None
        for package_id in truck.get_packages():
            p = packagetable.get(package_id)
            if p.status == 'At The Hub' or p.status == 'In Transit':
                distance = get_distance(
                    translate_address(current_location),
                    translate_address(p.address)
                )
                if distance < min_distance:
                    min_distance = distance
                    next_package_id = package_id
                    next_package = p
        if next_package:
            truck.distance_traveled += min_distance
            truck.current_location = next_package.address
            # Calculate delivery time
            travel_time = timedelta(hours=min_distance / truck.speed)
            truck.current_time += travel_time
            next_package.update_status('Delivered')
            if hasattr(next_package, 'delivery_time'):
                next_package.delivery_time = truck.current_time
            else:
                setattr(next_package, 'delivery_time', truck.current_time)
            truck.packages.remove(next_package_id)
            print(f"Delivered package {next_package.ID} to {next_package.address} at {next_package.delivery_time} and {next_package.status}. Distance traveled: {truck.distance_traveled} miles.")
        else:
            break

truck1 = truck.Truck(1, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])
truck2 = truck.Truck(2, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
truck3 = truck.Truck(3, [17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28])

class Main:
    deliver_packages(truck1, timedelta(hours=8))
    deliver_packages(truck2, timedelta(hours=9))
    deliver_packages(truck3, timedelta(hours=10))

    print("Western Governors University Parcel Service (WGUPS)")
    print("Package Delivery Summary:")
    print("Total distance traveled be all trucks:", round((truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled), 2))