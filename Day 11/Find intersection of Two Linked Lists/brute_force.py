class Node:
    def __init__(self, val):
        self.num = val
        self.next = None

# Utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if not head:
        head = newNode
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newNode
    return head

# Utility function to check presence of intersection
def intersectionPresent(head1, head2):
    while head2:
        temp = head1
        while temp:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    return None  # No intersection found

# Utility function to print linked list
def printList(head):
    while head and head.next:
        print(f"{head.num}->", end="")
        head = head.next
    if head:
        print(head.num, end="")
    print()

# Driver code
head = Node(1)
insertNode(head, 3)
insertNode(head, 1)
insertNode(head, 2)
insertNode(head, 4)
head1 = head
head = head.next.next.next  # Intersection point
headSec = Node(3)
head2 = headSec
headSec.next = head  # Creating intersection

# Printing of the lists
print("List1: ", end="")
printList(head1)
print("List2: ", end="")
printList(head2)

# Checking if intersection is present
answerNode = intersectionPresent(head1, head2)
if answerNode is None:
    print("No intersection")
else:
    print(f"The intersection point is {answerNode.num}")
