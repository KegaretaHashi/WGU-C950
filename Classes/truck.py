class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.packages = []
        self.current_location = "Hub"
        self.distance_traveled = 0.0
        self.start_time = None
        self.end_time = None
        self.speed = 18 
        self.address = None

    def load_package(self, package):
        self.packages.append(package)

    def unload_package(self, package):
        if package in self.packages:
            self.packages.remove(package)

    def get_packages(self):
        return self.packages