import heapq
import operator
from Order import Order
class Engine():
    def __init__(self) -> None:
        self.buyOrders = [] #maxHeap
        self.sellOrders = [] #minHeap
        return
    
    #add a sell/buy order to the trading book and return a trade if it matches
    #TC: O(n*logm) where n is the quantity and m is the size of the heap because popping from heap is logm 
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
    #delete a sell/buy order at that price
    #O(n): n is the size of the heap search to find right element to delete, swap with front and pop, then reheapify 
    def deleteOrder(self, orderType, price):
        mapping = {"BUY": self.buyOrders, "SELL": self.sellOrders}
        heap = mapping[orderType]
        res = None
        for idx, order in enumerate(heap):
            if abs(order.price) == price:
                heap[0], heap[idx] = heap[idx], heap[0] 
                res = heapq.heappop(heap)
                heapq.heapify(heap)
                break
        if res:
            return res
        return "N/A"
    
    #get total volume at a specified price and ordertype
    #iterate through heap and sum the quantitys for that price
    #O(n) where n is size of heap
    def getVolume(self, orderType, price):
        mapping = {"BUY": self.buyOrders, "SELL": self.sellOrders}
        heap = mapping[orderType]
        totalVolume = 0
        for order in heap:
            if abs(order.price) == price:
                totalVolume+=order.quantity
        return f"Volume: {totalVolume} @ Price: {price}"
    
    def printTradebook(self):
        print("------------------------------------------")
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
e.printTransactions(e.submitOrder("BUY", 6, 350))
e.printTradebook()
e.printTransactions(e.submitOrder("SELL", 4, 250))
e.printTradebook()
e.printTransactions(e.submitOrder("SELL", 9, 50))
e.printTradebook()
print("Deleted: "+str(e.deleteOrder("SELL", 9)))
e.printTradebook()
print(e.getVolume("BUY", 6))
# e.submitOrder("SELL", 3, 100)