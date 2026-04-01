
class Solution:
    # in-order left, root, right
    def in_order(self, root, result=None):
        if result is None:
            result = []
        if not root:
            return []
        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)
        return result
    # pre-order root, left, right
    def pre_order(self, root, result=None):
        if result is None:
            result = []
        if not root:
            return []
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)
        return result
    # post-order right, left, root
    def post_order(self, root, result=None):
        if result is None:
            result = []
        if not root:
            return []
        self.post_order(root.right, result)
        self.post_order(root.left, result)
        result.append(root.val)
        return result