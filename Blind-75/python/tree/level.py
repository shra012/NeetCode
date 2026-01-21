from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            level_size = len(q)
            res = []
            while level_size > 0:
                curr = q.popleft()
                res.append(curr.val)
                level_size -= 1
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(res)
        return result

if __name__ == "__main__":
    # Example usage:
    # Constructing the following binary tree:
    #        3
    #       / \
    #      9  20
    #         / \
    #        15  7

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    levels = solution.levelOrder(root)
    print("Level order traversal:", levels)  # Output: [[3], [9, 20], [15, 7]]