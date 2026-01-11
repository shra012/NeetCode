from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
    
if __name__ == "__main__":
    # Helper function to create a linked list with a cycle for testing
    def create_linked_list_with_cycle(values, pos):
        head = ListNode(values[0])
        current = head
        cycle_entry = None
        
        for index, value in enumerate(values[1:], start=1):
            current.next = ListNode(value)
            current = current.next
            if index == pos:
                cycle_entry = current
        
        if cycle_entry:
            current.next = cycle_entry
        
        return head

    sol = Solution()
    
    # Test case 1: Linked list with a cycle
    head_with_cycle = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print("Linked list with cycle:", sol.hasCycle(head_with_cycle))  # Expected output: True
    
    # Test case 2: Linked list without a cycle
    head_without_cycle = create_linked_list_with_cycle([1, 2], -1)
    print("Linked list without cycle:", sol.hasCycle(head_without_cycle))  # Expected output: False
    
    # Test case 3: Single node without a cycle
    single_node = create_linked_list_with_cycle([1], -1)
    print("Single node without cycle:", sol.hasCycle(single_node))  # Expected output: False