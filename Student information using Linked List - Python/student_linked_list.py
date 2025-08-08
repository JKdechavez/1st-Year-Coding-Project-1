from student import Student

class Node:
    def __init__(self, student):
        self.student = student
        self.next = None

class Student_Linked_List:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
           yield node
           node = node.next

    def __str__(self):
        str_rep = ""
        node = self.head
        while node is not None:
            str_rep += str(node.student) + "\n"
            node = node.next
        return str_rep

    def is_empty(self):
        return self.head == None

    def insert_at_front(self, student):
        node = Node(student)
        node.next = self.head
        self.head = node

    def insert_at_end(self, student):
        node = Node(student)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def search(self, idno):
        for node in self:
            if node.student.get_idno() == idno:
                return node
        return None

    def delete(self, idno):
        node_to_delete = self.search(idno)
        if node_to_delete:
           if node_to_delete == self.head:
              self.head = self.head.next
           else:
               prev_node = None
               current_node = self.head
               while current_node:
                   if current_node.student.get_idno() == idno:
                       prev_node.next =  current_node.next
                   prev_node = current_node
                   current_node = current_node.next
        else:
            print("Cannot Delete Node.")

