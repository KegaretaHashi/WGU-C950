class package:
    def __init__(self, ID, address, city, state, zip_code, weight, delivery_status='Pending'):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.delivery_status = delivery_status

    def __str__(self):
        return (f"Package ID: {self.ID}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zip Code: {self.zip_code}, Weight: {self.weight} lbs, "
                f"Delivery Status: {self.delivery_status}")
    
    def update_delivery_status(self, status):
        self.delivery_status = status