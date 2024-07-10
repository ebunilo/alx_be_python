class Product:
    """Define a Product class with attributes like name, price, and quantity. 
    Implement a method to calculate the total value of products in stock."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity


# Test the Product class
product = Product("Laptop", 999.99, 10)
print(f"Total value of {product.name} in stock: ${product.total_value():.2f}")
