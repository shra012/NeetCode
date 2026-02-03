class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if tokens[i] == "#":
                i += 1
                return None
            node = TreeNode(int(tokens[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(5)
    
    ser = Codec()
    print("Serialized Tree:", ser.serialize(root))  # Output: "1,2,#,#,3,#,5,#,#"
    deser = Codec()
    print("Deserialized Tree Root Value:", deser.deserialize(ser.serialize(root)).val)  # Output: 1
    ans = deser.deserialize(ser.serialize(root))
    def print_tree(node):
        if not node:
            return "#"
        return f"{node.val}, {print_tree(node.left)}, {print_tree(node.right)}"
    print("Deserialized Tree Structure:", print_tree(ans))  # Output: "1, 2, #, #, 3, #, 5, #, #"