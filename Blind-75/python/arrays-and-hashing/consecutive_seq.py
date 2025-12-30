from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = set(nums)
        res = 0
        for num in mem:
            if num - 1 in mem:
                continue
            count = 0
            cur = num
            while(cur in mem):
                count += 1
                cur += 1
            res = max(res, count)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([2,20,4,10,3,4,5]))  # 4