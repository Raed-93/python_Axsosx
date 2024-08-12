from store import Store
from product import Product

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





