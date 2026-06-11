# Node class represents a
# node in a linked list
class Node:
    # Data stored in the node
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to merge two sorted linked lists
def sort_two_linked_lists(list1, list2):
    # Create a dummy node to serve
    # as the head of the merged list
    dummy_node = Node(-1)
    temp = dummy_node

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    # Return the merged list starting
    # from the next of the dummy node
    return dummy_node.next

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

if __name__ == "__main__":
    # Example Linked Lists
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    print("First sorted linked list: ", end="")
    print_linked_list(list1)

    print("Second sorted linked list: ", end="")
    print_linked_list(list2)

    merged_list = sort_two_linked_lists(list1, list2)

    print("Merged sorted linked list: ", end="")
    print_linked_list(merged_list)