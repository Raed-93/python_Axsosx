import uuid

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.product_id = str(uuid.uuid4())  
        
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change / 100
        else:
            self.price -= self.price * percent_change / 100
        return self
            
    def print_info(self):
        print(f"ID: {self.product_id}, Product: {self.name}, Price: {self.price}, Category: {self.category}")
        return self
