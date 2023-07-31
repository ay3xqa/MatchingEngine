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
        while quantity and heap and operations[orderType](heap[0].price,price):
            currentOrder = heap[0]
            if currentOrder.quantity <= quantity:
                res.append(Order(currentOrder.orderType, min(currentOrder.price, price), currentOrder.quantity))
                quantity-=currentOrder.quantity
                heapq.heappop(heap)
            else:
                res.append(Order(currentOrder.orderType, min(currentOrder.price, price), quantity))
                currentOrder.quantity-=quantity
                quantity = 0
        if quantity:
            heapq.heappush(leftoverHeap, Order(orderType, price, quantity))
        # print("buys", self.buyOrders)
        # print("sells", self.sellOrders)
        # print("transactions----------------")
        # for q in res:
        #     print(q)
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
    

# t = []
# x = Order("BUY", 5, 100)
# print(x)
# heapq.heappush(t, Order("BUY", 5, 100))
# heapq.heappush(t, Order("BUY", 4, 100))
# heapq.heappush(t, Order("BUY", 1, 100))
# heapq.heappush(t, Order("BUY", 1, 1))


e = Engine()

e.submitOrder("BUY", 5, 150)
e.submitOrder("SELL", 4, 200)
e.submitOrder("BUY", 8, 50)
# e.submitOrder("SELL", 3, 100)