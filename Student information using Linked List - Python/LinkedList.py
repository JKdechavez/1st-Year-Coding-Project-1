from Task import Task
from Assignee import Assignee


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_new_task(self, task):
        new_node = Node(task)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        with open("task.txt", "a") as file:
            data = f'{task.get_task_id()}, {task.get_task_title()}, {task.get_task_description()}, {task.get_task_status()}, {task.get_task_assignee()}, {task.get_task_priorities()}, {task.get_task_comments()}, {task.get_task_due_date()}\n'
            file.write(data)

    def add_new_assignee(self, assignee):
        new_node = Node(assignee)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        with open("assignee.txt", "a") as file:
            data = f'{assignee.get_assignee_id()}, {assignee.get_assignee_name()}, {assignee.get_assignee_email()}, {assignee.get_assignee_task()}\n'
            file.write(data)

    def search_task_by_id(self, task_id):
        current_node = self.head
        if self.is_empty():
            print("List is empty")
            return {}

        while current_node is not None:
            if isinstance(current_node.data, Task) and current_node.data.get_task_id() == task_id:
                data = current_node.data.get_all_details()
                print(data)
                return data
            current_node = current_node.next

        print(f'{task_id} is not found')
        return {}

    def search_assignee_by_name(self, assignee_name):
        current_node = self.head
        if self.is_empty():
            print("List is empty")
            return {}

        while current_node is not None:
            if isinstance(current_node.data, Assignee) and current_node.data.get_assignee_name() == assignee_name:
                data = current_node.data.get_all_details()
                print(data)
                return data
            current_node = current_node.next

        print(f'{assignee_name} is not found')
        return {}

    def load_tasks(self, file_name):
        try:
            with open(file_name, "r") as task_file:
                for line in task_file:
                    task_id, title, description, status, assignee, priorities, comments, due_date = line.strip().split(", ")

                    existing_task = self.search_task_by_id(task_id)
                    if existing_task:
                        continue

                    new_task = Task(task_id, title, description, status, assignee, priorities, comments, due_date)
                    self.add_new_task(new_task)

        except FileNotFoundError:
            print("Error! File not found")

    def load_assignees(self, file_name):
        try:
            with open(file_name, "r") as task_file:
                for line in task_file:
                    assignee_id, name, email, task = line.strip().split(", ")

                    existing_assignee = self.search_assignee_by_name(name)
                    if existing_assignee:
                        continue

                    new_assignee = Assignee(assignee_id, name, email, task)
                    self.add_new_assignee(new_assignee)

        except FileNotFoundError:
            print("Error! File not found")

    def sort_task_by_id(self, file_name):
        try:
            if self.is_empty():
                print("List is empty")
                return

            task_list = []
            current = self.head

            while current is not None:
                task_list.append(current.data.get_task_id())
                current = current.next

            sorted_list = sorted(task_list)

            with open(file_name, "w") as file:
                for task_id in sorted_list:
                    info = ""
                    dictionary = self.search_task_by_id(task_id)
                    if dictionary:
                        for value in dictionary.values():
                            info += str(value) + ", "
                        file.write(info.rstrip(", ") + "\n")

        except FileNotFoundError:
            print("Error! File not found")

    def sort_assignees_by_name(self, file_name):
        try:
            if self.is_empty():
                print("List is empty")
                return

            assignee_list = []
            current = self.head

            while current is not None:
                if isinstance(current.data, Assignee):
                    assignee_list.append(current.data.get_assignee_name())
                current = current.next

            sorted_list = sorted(assignee_list)

            with open(file_name, "w") as file:
                for name in sorted_list:
                    info = ""
                    dictionary = self.search_assignee_by_name(name)
                    if dictionary:
                        for value in dictionary.values():
                            info += str(value) + ", "
                        file.write(info.rstrip(", ") + "\n")

        except FileNotFoundError:
            print("Error! File not found")
        return None

    def track_task_progress(self, task_id):
        current = self.head
        if self.is_empty():
            print("List is empty")
            return

        found = False

        while current is not None:
            if isinstance(current.data, Task) and current.data.get_task_id() == task_id:
                print(f'Task with ID number {task_id} is {current.data.get_task_status()}')
                found = True
                break
            current = current.next

        if not found:
            print("Task not found!")

    def mark_task_completed(self, task_id):
        current = self.head
        if self.is_empty():
            print("List is empty")
            return

        task_found = False

        while current is not None:
            if current.data.get_task_id() == task_id:
                task_found = True
                answer = input("Task is found, would you like to update the status? (y/n): ").lower()
                while answer not in ["y", "n"]:
                    answer = input("Invalid input! Enter again: ")

                if answer == "y":
                    is_done = input("Update the status of the task (ongoing/completed): ").lower()
                    while is_done not in ["ongoing", "completed"]:
                        is_done = input("Invalid input! Enter again: ")
                    current.data.set_task_status(is_done)
                    print("Task status updated successfully.")

                with open("task.txt", "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if not line.startswith(str(task_id)):
                            file.write(line)
                    file.truncate()

                with open("task.txt", "a") as file:
                    updated_data = ""
                    dictionary = self.search_task_by_id(task_id)
                    if dictionary:
                        for value in dictionary.values():
                            updated_data += str(value) + ", "
                        file.write(updated_data.rstrip(", ") + "\n")

            current = current.next

        if not task_found:
            print("Task not found.")

    def generate_task_report(self, task_id):
        task_details = self.search_task_by_id(task_id)
        if task_details:
            pass
        else:
            print(f'Task with ID number {task_id} is not found')

