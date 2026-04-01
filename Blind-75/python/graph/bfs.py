from collections import deque
class Solution:
    def __init__(self):
        self.graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    def bfs(self, graph, start, result=None, visited=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []
        q = deque()
        q.append(start)
        while q:
            curr = q.popleft()
            if curr not in visited:
                visited.add(curr)
                result.append(curr)
                for next_node in graph[curr]:
                    if next_node not in visited:
                        q.append(next_node)
        return result
if __name__ == "__main__":
    # Graph representation
    #       A
    #      / \
    #     B   C
    #     |
    #     D
    
    solution = Solution()
    bfs_result = []
    solution.bfs(solution.graph, 'A', bfs_result)
    print("BFS traversal:", bfs_result)  # Output: ['A', 'B', 'C', 'D']