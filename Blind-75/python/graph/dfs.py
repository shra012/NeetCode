class Solution():
    def dfs(self, graph, start, result=None, visited=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []
        if start not in visited:
            visited.add(start)
            result.append(start)
            for next_node in graph[start]:
                if next_node not in visited:
                    self.dfs(graph, next_node, result, visited)
        return result

if __name__ == "__main__":
    # Graph representation
    #       A
    #      / \
    #     B   C
    #     |
    #     D

    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    solution = Solution()
    dfs_result = solution.dfs(graph, 'A')
    print("DFS traversal:", dfs_result)  # Output: ['A', 'B', 'D', 'C'].
