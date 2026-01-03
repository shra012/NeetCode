from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxFreq = 0
        res = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            maxFreq = max(maxFreq, count[ch])
            window_len = r - l + 1
            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            res = max(res, window_len)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))  # 4
    print(sol.characterReplacement("AABABBA", 1))  # 4