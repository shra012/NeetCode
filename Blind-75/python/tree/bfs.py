from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def bfs(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            curr = q.popleft()
            result.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return result
    
if __name__ == "__main__":
    # Example usage:
    # Constructing the following binary tree:
    #        3
    #       / \
    #      9  20
    #     /   / \
    #    12  15  7


    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(12)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    bfs_result = solution.bfs(root)
    print("BFS traversal:", bfs_result)  # Output: [3, 9, 20, 12, 15, 7]