from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

if __name__ == "__main__":
    sol = Solution()
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    inverted_root = sol.invertTree(root)
    # The inverted tree can be verified by traversing it
    def print_tree(root):
        if not root:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.val, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    print_tree(inverted_root)  # You should see the inverted tree structure 1 3 2 7 6 5 4