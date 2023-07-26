from node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # Insert a node with the given data at the end of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_max_min(self):
        # Method to display the maximum and minimum data in the linked list
        if not self.head:
            return None, None

        current = self.head
        max_data = current.data
        min_data = current.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data

    def convert_to_binary_search_tree(self, data_list):
        # Method to convert the linked list into a binary search tree
        # The input data_list is a Python list containing the elements to be inserted into the binary search tree.

        # First, sort the data list to ensure that the binary search tree will be balanced.
        data_list.sort()

        # Helper function to convert a sorted list to a binary search tree
        def sorted_list_to_bst(sorted_list):
            if not sorted_list:
                return None

            mid = len(sorted_list) // 2
            root = Node(sorted_list[mid])
            root.left = sorted_list_to_bst(sorted_list[:mid])
            root.right = sorted_list_to_bst(sorted_list[mid + 1:])

            return root

        # Convert the sorted data_list to a binary search tree
        self.head = sorted_list_to_bst(data_list)


class Queue:
    def __init__(self):
        # Initialize the front and rear of the queue
        self.front = None
        self.rear = None

    def is_empty(self):
        # Check if the queue is empty
        return self.front is None

    def enqueue(self, data):
        # Enqueue (insert) an element into the queue
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # Dequeue (remove) an element from the queue
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def display(self):
        # Display the elements of the queue
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def sort(self):
        # Bonus: Sort the elements of the queue (implement any sorting algorithm of your choice)
        # For example, you can use selection sort for simplicity
        def selection_sort(lst):
            for i in range(len(lst) - 1):
                min_idx = i
                for j in range(i + 1, len(lst)):
                    if lst[j] < lst[min_idx]:
                        min_idx = j
                lst[i], lst[min_idx] = lst[min_idx], lst[i]

        # Create a list to store the elements of the queue
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next

        # Sort the list of elements
        selection_sort(elements)

        # Clear the existing queue
        self.front = self.rear = None

        # Enqueue the sorted elements back into the queue
        for element in elements:
            self.enqueue(element)
