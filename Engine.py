import heapq
import operator
from Order import Order
class Engine():
    def __init__(self) -> None:
        self.buyOrders = [] #maxHeap
        self.sellOrders = [] #minHeap
        return
    
    #add a sell/buy order to the trading book and return a trade if it matches
    def submitOrder(self, orderType, price, quantity):
        mapping = {"BUY": self.sellOrders, "SELL": self.buyOrders}
        operations = {"BUY": operator.le, "SELL": operator.ge}
        leftover = {"BUY": self.buyOrders, "SELL": self.sellOrders}
        leftoverHeap = leftover[orderType]
        heap = mapping[orderType]
        res = []
        while quantity and heap and operations[orderType](abs(heap[0].price),price):
            currentOrder = heap[0]
            if currentOrder.quantity <= quantity:
                if orderType == "BUY":
                    transaction = Order(currentOrder.orderType, min(currentOrder.price, price), currentOrder.quantity)
                else:
                    transaction = Order(currentOrder.orderType, min(-currentOrder.price, price), currentOrder.quantity)
                res.append(transaction)
                quantity-=currentOrder.quantity
                heapq.heappop(heap)
            else:
                if orderType == "BUY":
                    transaction = Order(currentOrder.orderType, min(currentOrder.price, price), quantity)
                else:
                    transaction = Order(currentOrder.orderType, min(-currentOrder.price, price), quantity)
                res.append(transaction)
                currentOrder.quantity-=quantity
                quantity = 0
        if quantity:
            if orderType == "SELL":
                leftoverOrder = Order(orderType, price, quantity)
            else:
                leftoverOrder = Order(orderType, -price, quantity)
            heapq.heappush(leftoverHeap, leftoverOrder)
        return res
    
    #assume is valid to delete
    #delete a sell/buy order at that price given quantity
    def deleteOrder(self, orderType, price, quantity):
        
        return 
    
    #get total volume at a specified price and ordertype
    def getVolume(self, orderType, price):
        return
    
    #return min and max of orders for a specified order type
    def getRange(self, orderType):
        return
    
    def printTradebook(self):
        print("---BUYS AVAILABLE---")
        for buy in self.buyOrders:
            print(buy)
        print("---SELLS AVAILABLE---")
        for sell in self.sellOrders:
            print(sell)
        print("------------------------------------------")
    
    def printTransactions(self, transactions):
        print("---Transactions---")
        for buy in transactions:
            print(buy)

# t = []
# x = Order("BUY", 5, 100)
# print(x)
# heapq.heappush(t, Order("BUY", 5, 100))
# heapq.heappush(t, Order("BUY", 4, 100))
# heapq.heappush(t, Order("BUY", 1, 100))
# heapq.heappush(t, Order("BUY", 1, 1))


e = Engine()

e.printTransactions(e.submitOrder("BUY", 3, 150))
e.printTradebook()
e.printTransactions(e.submitOrder("BUY", 6, 200))
e.printTradebook()
e.printTransactions(e.submitOrder("SELL", 4, 50))
e.printTradebook()
# e.submitOrder("SELL", 3, 100)