class Product_Catalog:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity
    
product1 = Product_Catalog("apple", 5, 10)   
product2 = Product_Catalog("banana", 2, 10)
    
print (f"product: {product1.name}, total value: {product1.total_value()}") 
print (f"product: {product2.name}, total value: {product2.total_value()}") 

