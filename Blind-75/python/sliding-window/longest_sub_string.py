class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        seen = set()
        res = 0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            seen.add(ch)
            res = max(res, r - l + 1)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # 3