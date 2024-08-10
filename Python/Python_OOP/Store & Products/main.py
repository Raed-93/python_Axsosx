class Store:
    def __init__(self,name):
        self.name = name
        self.products = []
        
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        product = self.products.pop(id)
        product.print_info()
        return self
    
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_change=percent_increase, is_increased = True)
            return self
        
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_change=percent_discount, is_increased = False)
                return self
    
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change / 100
        else:
            self.price -= self.price * percent_change / 100
        return self
    
    def print_info(self):
        print(f"Product: {self.name}, Category: {self.category}, Price: ${self.price}")
        return self
    

store = Store("My Store")
product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Phone", 500, "Electronics")
product3 = Product("Shirt", 50, "Clothing")

store.add_product(product1).add_product(product2).add_product(product3)

print("Before inflation:")
for product in store.products:
    product.print_info()
    
store.inflation(10)  
print("\n After inflation:")
for product in store.products:
    product.print_info()
    
store.set_clearance("Electronics", 20)  
print("\n After the reduction:")
for product in store.products:
    product.print_info()
    
store.sell_product(1)  





