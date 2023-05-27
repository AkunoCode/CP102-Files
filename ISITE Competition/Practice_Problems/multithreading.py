import threading
import time
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

class Food_Ordering_System:
    def __init__(self):
        self.food_orders = Queue()
        self.menu = ['pizza','samosa','pasta','biryani','burger']
    
    def place_order(self):
        for item in self.menu:
            print(f"Order in: {item}")
            self.food_orders.enqueue(item)
            time.sleep(0.5)
    
    def serve_order(self):
        time.sleep(1)
        while self.food_orders.is_empty() is False:
            order = self.food_orders.dequeue()
            print(f"Order out: {order}")
            time.sleep(2)
    
    def process_order(self):
        t1 = threading.Thread(target=self.place_order)
        t2 = threading.Thread(target=self.serve_order)
        t1.start()
        t2.start()

food_ordering_system = Food_Ordering_System()
food_ordering_system.process_order()

