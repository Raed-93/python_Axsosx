# main.py
from store import Store
from product import Product

# إنشاء متجر ومنتجات
store = Store("My Store")
product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Car", 10000, "Vehicle")

# إضافة المنتجات إلى المتجر
store.add_product(product1).add_product(product2)

# عرض معلومات المنتجات قبل البيع
print("Products before selling:")
for product in store.products:
    product.print_info()

# بيع منتج باستخدام معرفه الفريد
store.sell_product(product1.product_id)

# عرض معلومات المنتجات بعد البيع
print("\nProducts after selling:")
for product in store.products:
    product.print_info()
