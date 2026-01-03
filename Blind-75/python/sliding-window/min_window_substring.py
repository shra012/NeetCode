from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        l = 0
        cnt = 0
        min_window = float('inf')
        s_idx = -1
        for ch in t:
            mem[ch] += 1
        for r, ch in enumerate(s):
            if mem[ch] > 0:
                cnt+=1
            mem[ch] -= 1
            
            while cnt == len(t):
                if r - l + 1 < min_window:
                    s_idx = l
                    min_window = r - l + 1
                mem[s[l]] += 1
                if mem[s[l]] > 0:
                    cnt -= 1
                l += 1

        return "" if s_idx == -1 else s[s_idx:s_idx + min_window]

if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))  # Output: "BANC"