from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next
    
if __name__ == "__main__":
    # Creating first sorted linked list: 1 -> 3 -> 5
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    # Creating second sorted linked list: 2 -> 4 -> 6
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    # Print the merged linked list
    def print_linked_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)
    print("Merged linked list:")
    print_linked_list(merged_head)