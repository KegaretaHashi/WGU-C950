class package:
    def __init__(self, ID, address, city, state, zip_code, deadline, weight, status='At The Hub'):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return (f"Package ID: {self.ID}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zip Code: {self.zip_code}, Delivery Deadline: {self.deadline}, Weight: {self.weight} kgs, "
                f"Delivery Status: {self.status}")
    
    def update_status(self, status):
        self.status = status

    def get_status(self):
        return self.status