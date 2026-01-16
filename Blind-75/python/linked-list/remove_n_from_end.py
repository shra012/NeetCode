from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    
# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # Print the modified linked list
    def print_linked_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")
    n = 2  # Remove the 2nd node from the end
    print("Original linked list:")
    print_linked_list(head)
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)
    print(f"Linked list after removing the {n}th node from the end:")
    print_linked_list(new_head)
    