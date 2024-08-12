from product import Product
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