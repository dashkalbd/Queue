from collections import deque


class Queue:
    def __init__(self):
        self.documents = deque()

    def add_document(self, title, author):
        self.documents.append({"title": title, "author": author})

    def next_document(self):
        if len(self.documents) == 0:
            print("Queue is empty")
        else:
            document = self.documents[0]
            print(f"Next to print: {document['title']} ({document['author']})")

    def print_document(self):
        if len(self.documents) == 0:
            print("Queue is empty")
        else:
            document = self.documents.popleft()
            print(f"Printed: {document['title']} ({document['author']})")

    def count(self):
        print(f"Documents waiting: {len(self.documents)}")


queue = Queue()

queue.add_document("Essay", "Olena")
queue.add_document("Report", "Andrii")
queue.add_document("Homework", "Maria")
queue.add_document("Presentation", "Ivan")

queue.count()
queue.next_document()

queue.print_document()
queue.count()

queue.print_document()
queue.count()

queue.print_document()
queue.print_document()
queue.count()

queue.print_document()