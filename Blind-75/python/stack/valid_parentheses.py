class Solution(object):
    def isValid(self, s):
        memo = {}
        def dfs(i, open_count):
            if open_count < 0:
                return False
            if i == len(s):
                return open_count == 0
            if (i, open_count) in memo:
                return memo[(i, open_count)]
            if s[i] == '(':
                ans = dfs(i + 1, open_count + 1)
            elif s[i] == ')':
                ans = dfs(i + 1, open_count - 1)
            else:
                ans = (dfs(i + 1, open_count + 1) or
                        dfs(i + 1, open_count - 1) or
                        dfs(i + 1, open_count))
            memo[(i, open_count)] = ans
            return ans
        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("((***))"))  # True
    print(sol.isValid("()"))  # True
    print(sol.isValid("(*))"))  # True  
    print(sol.isValid("(()"))  # False   