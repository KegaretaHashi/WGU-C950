from datetime import timedelta


class package:
    # Initializes a package object
    def __init__(self, ID, address, city, state, zip_code, deadline, weight, status='At The Hub'):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = timedelta(hours=0)
        self.departure_time = timedelta(hours=0)
        self.truck_id = None

    # Returns a string description of the package object
    def __str__(self):
        return (f"Package ID: {self.ID}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zip Code: {self.zip_code}, Delivery Deadline: {self.deadline}, Weight: {self.weight} kgs, "
                f"Delivery Status: {self.status}, Delivery Time: {self.delivery_time}, Truck ID: {self.truck_id}")
    
    # Updates the status of the package
    def update_status(self, status):
        self.status = status

    # Updates the delivery time of the package
    def update_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    # Returns the current status of the package
    def get_status(self):
        return self.status
    
    # Returns status of the package at a given time
    def get_time_status(self, time):
        if (self.ID == 6 or self.ID == 25 or self.ID == 28 or self.ID == 32) and time < timedelta(hours=9, minutes=5):
            return "Delayed"
        elif self.delivery_time < time:
            return "Delivered"
        elif self.delivery_time > time and self.departure_time < time:
            return "En Route"
        else:
            return "At The Hub"