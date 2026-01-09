from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to print the linked list
    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    sol = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original linked list:")
    print_linked_list(head)
    
    reversed_head = sol.reverseList(head)
    print("Reversed linked list:")
    print_linked_list(reversed_head)