
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(nums[i] * pref[i-1])
        suf = [1] * len(nums)
        suf[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = nums[i] * suf[i+1]
        
        return []
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,4,6]))  # [48, 24, 12, 8]