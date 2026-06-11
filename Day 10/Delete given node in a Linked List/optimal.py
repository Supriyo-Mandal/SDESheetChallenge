# Definition of singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    
        self.next = next  

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy value from the next node into this node
        node.val = node.next.val
        
        # Bypass the next node
        node.next = node.next.next

# Driver code
if __name__ == "__main__":
    # Create linked list: 4 -> 5 -> 1 -> 9
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    # Delete node with value 5
    sol = Solution()
    sol.deleteNode(head.next)

    # Print updated list: expected 4 -> 1 -> 9
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
