class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
            
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
if __name__ == "__main__":
    # Example usage:
    # Constructing the following BST:
    #        6
    #       / \
    #      2   8
    #     / \ / \
    #    0  4 7  9
    #      / \
    #     3   5

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left.left  # Node with value 0
    q = root.left.right  # Node with value 4

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of {} and {} is: {}".format(p.val, q.val, lca.val))  # Output: 2