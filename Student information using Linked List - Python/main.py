class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"{data} not found in the list.")

    def display(self):
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
my_list = LinkedList()
my_list.insert_at_end(5)
my_list.insert_at_end(10)
my_list.insert_at_end(15)
my_list.display()  # Output: 5 10 15

my_list.delete(10)
my_list.display()  # Output: 5 15

my_list.delete(20)  # Output: 20 not found in the list.

