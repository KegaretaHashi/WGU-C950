from datetime import timedelta


class Truck:
    # Initializes a Truck object 
    def __init__(self, truck_id, packages):
        self.truck_id = truck_id
        self.packages = packages
        self.current_location = "4001 South 700 East"
        self.current_time = timedelta(hours=0)
        self.distance_traveled = 0.0
        self.speed = 18 

    # Returns a string description of the Truck object
    def __str__(self):
        return f"Truck ID: {self.truck_id}, Current Location: {self.current_location}, Distance Traveled: {self.distance_traveled} miles, Speed: {self.speed} mph"

    # Loads a package into truch package list
    def load_package(self, package):
        self.packages.append(package)

    # Unloads a package from truck package list
    def unload_package(self, package):
        self.packages.remove(package)

    # Returns packages in the truck
    def get_packages(self):
        return self.packages