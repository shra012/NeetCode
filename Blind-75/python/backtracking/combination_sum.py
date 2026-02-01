from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, res, k):
            if k == 0:
                ans.append(res[:])
            if k < 0:
                return
            for i in range(start, len(candidates)):
                res.append(candidates[i])
                backtrack(i, res, k - candidates[i])
                res.pop()

        backtrack(0, [], target)
        return ans

if __name__ == "__main__":
    # Example usage:
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print("Combination Sum results:", result)  # Output: [[7], [2, 2, 3]]