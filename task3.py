from collections import deque


class Queue:
    def __init__(self):
        self.clients = deque()

    def add_client(self, ticket, issue):
        self.clients.append({"ticket": ticket, "issue": issue})
        print(f"Added: ticket {ticket} ({issue})")

    def call_next(self):
        if len(self.clients) == 0:
            print("All clients have been served")
        else:
            client = self.clients.popleft()
            print(f"Now serving: ticket {client['ticket']} ({client['issue']})")

    def count(self):
        print(f"Clients waiting: {len(self.clients)}")

    def next_ticket(self):
        if len(self.clients) == 0:
            print("All clients have been served")
        else:
            client = self.clients[0]
            print(f"Next ticket: {client['ticket']}")


queue = Queue()

queue.add_client("A001", "Phone screen broken")
queue.add_client("A002", "Laptop won't turn on")
queue.add_client("A003", "Software installation")
queue.add_client("A004", "Battery replacement")

queue.count()
queue.next_ticket()

queue.call_next()
queue.count()
queue.next_ticket()

queue.call_next()
queue.call_next()
queue.call_next()
queue.count()

queue.call_next()
queue.next_ticket()