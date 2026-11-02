from collections import deque


class Queue:
    def __init__(self):
        self.orders = deque()

    def add_order(self, order):
        self.orders.append(order)

    def next_order(self):
        if len(self.orders) == 0:
            print("Queue is empty")
        else:
            print(f"Next order: {self.orders[0]}")

    def prepare_order(self):
        if len(self.orders) == 0:
            print("Queue is empty")
        else:
            print(f"Prepared: {self.orders.popleft()}")

    def show_orders(self):
        if len(self.orders) == 0:
            print("Queue is empty")
        else:
            print("Remaining orders:")
            for order in self.orders:
                print(order)


queue = Queue()

queue.add_order("Order 101")
queue.add_order("Order 102")
queue.add_order("Order 103")
queue.add_order("Order 104")
queue.add_order("Order 105")

queue.next_order()

queue.prepare_order()
queue.prepare_order()

queue.show_orders()

queue.prepare_order()
queue.prepare_order()
queue.prepare_order()
queue.prepare_order()