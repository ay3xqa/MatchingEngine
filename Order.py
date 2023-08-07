class Order:
    def __init__(self, orderType, price, quantity):
        self.orderType = orderType
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f'(T: {self.orderType}, P: {abs(self.price)}, Q: {self.quantity})'
    def __lt__(self, other):
        return self.price < other.price