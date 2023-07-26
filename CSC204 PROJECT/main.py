from singly_linked_list import SingleLinkedList, Queue

if __name__ == "__main__":
    # Test the Single Linked List
    sll = SingleLinkedList()
    elements = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    for element in elements:
        sll.insert(element)

    print("Linked List:")
    sll.display()

    max_data, min_data = sll.find_max_min()
    print("\nMaximum data:", max_data)
    print("Minimum data:", min_data)

    bst_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    sll.convert_to_binary_search_tree(bst_list)

    print("\nBinary Search Tree (In-order Traversal):")
    sll.display()

    # Test the Queue
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(8)
    queue.enqueue(15)
    queue.enqueue(3)
    queue.enqueue(7)

    print("\nQueue:")
    queue.display()

    print("\nDequeue elements:")
    print(queue.dequeue())
    print(queue.dequeue())

    print("\nUpdated Queue:")
    queue.display()

    print("\nSorting the Queue:")
    queue.sort()
    queue.display()
