# Author: Cherokee Wilson 
# Student ID: 001459252

import csv
from datetime import timedelta
import truck
import package
from hashTable import hashtable

PACKAGE_FILE = "SupportingDocument/WGUPS Package File.csv"
DISTANCE_FILE = "SupportingDocument/WGUPS Distance Table.csv"
ADDRESS_LEGEND_FILE = "SupportingDocument/addresslegend.csv"

# Create Hashtable and load package data into it
packagetable = hashtable()
with open(PACKAGE_FILE) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        pkg = package.package(
            int(row[0]), row[1], row[2], row[3], row[4], row[5], float(row[6])
        )
        packagetable.insert(pkg.ID, pkg)

# Load distances into a list
with open(DISTANCE_FILE) as file:
    distances = list(csv.reader(file))

# Load address legend into a list
with open(ADDRESS_LEGEND_FILE) as file:
    address_legend = list(csv.reader(file))

# Translate address string to address ID
def translate_address(address):
    for row in address_legend:
        if address == row[2]:
            return int(row[0])
    return None

# Gets the distance between two addresses
def get_distance(address1, address2):
    d = distances[address1][address2]
    if not d:
        d = distances[address2][address1]
    return float(d)

# Delivers all packages in specified truck using the nearest neighbor algorithm
def deliver_packages(truck_obj, start_time):
    # Set truck start time
    truck_obj.current_time = start_time

    # Set status of all packages in the truck to 'In Transit'
    for package_id in truck_obj.get_packages():
            package = packagetable.get(package_id)
            package.update_status('In Transit')

    # Loop through packages in truck until all packages are delivered
    while truck_obj.get_packages():
        current_address = translate_address(truck_obj.current_location)
        closest_pkg = None
        min_distance = float('inf')
        
        # Iterates through packages in the truck to find the closest undelivered package
        # based on the trucks current location
        for package_id in truck_obj.get_packages():
            package = packagetable.get(package_id)
            if package.status not in ('In Transit'):
                continue
            package_address = translate_address(package.address)
            distance = get_distance(current_address, package_address)
            if distance < min_distance:
                min_distance = distance
                closest_pkg = package

        # If a undelivered package is found, update truck and package status
        # and move the truck to the package's address
        if closest_pkg:
            truck_obj.distance_traveled += min_distance
            truck_obj.current_location = closest_pkg.address
            travel_time = timedelta(hours=min_distance / truck_obj.speed)
            truck_obj.current_time += travel_time
            closest_pkg.update_status('Delivered')
            closest_pkg.delivery_time = truck_obj.current_time
            truck_obj.packages.remove(closest_pkg.ID)
            print(
                f"Delivered package {closest_pkg.ID} to {closest_pkg.address} at {closest_pkg.delivery_time} "
                f"({closest_pkg.status}). Distance traveled: {truck_obj.distance_traveled:.2f} miles."
            )
        else:
            # Break the loop if no undelivered packages are found
            break

# Create and load trucks with packages
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

