import csv
from datetime import timedelta
import truck
import package
from hashTable import hashtable

# File paths
PACKAGE_FILE = "SupportingDocument/WGUPS Package File.csv"
DISTANCE_FILE = "SupportingDocument/WGUPS Distance Table.csv"
ADDRESS_LEGEND_FILE = "SupportingDocument/addresslegend.csv"

# Load package data into hash table
packagetable = hashtable()
with open(PACKAGE_FILE) as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        pkg = package.package(
            int(row[0]), row[1], row[2], row[3], row[4], row[5], float(row[6])
        )
        packagetable.insert(pkg.ID, pkg)

# Load distances and address legend
with open(DISTANCE_FILE) as file:
    distances = list(csv.reader(file))

with open(ADDRESS_LEGEND_FILE) as file:
    address_legend = list(csv.reader(file))

def translate_address(address):
    """Convert an address string to its index using the address legend."""
    for row in address_legend:
        if address == row[2]:
            return int(row[0])
    return None

def get_distance(idx1, idx2):
    """Get the distance between two address indices."""
    d = distances[idx1][idx2]
    if not d:
        d = distances[idx2][idx1]
    return float(d)

def deliver_packages(truck_obj, start_time):
    """Deliver all packages on the truck using a greedy nearest-neighbor approach."""
    truck_obj.current_time = start_time

    while truck_obj.get_packages():
        current_idx = translate_address(truck_obj.current_location)
        closest_pkg = None
        min_distance = float('inf')

        for pkg_id in truck_obj.get_packages():
            pkg = packagetable.get(pkg_id)
            if pkg.status not in ('At The Hub', 'In Transit'):
                continue
            pkg_idx = translate_address(pkg.address)
            distance = get_distance(current_idx, pkg_idx)
            if distance < min_distance:
                min_distance = distance
                closest_pkg = pkg

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
            break

if __name__ == "__main__":
    truck1 = truck.Truck(1, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])
    deliver_packages(truck1, timedelta(hours=8))
