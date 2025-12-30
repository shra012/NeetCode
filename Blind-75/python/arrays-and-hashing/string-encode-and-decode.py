from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        if not strs:
            return result
        for s in strs:
            result += f'{len(s)}#{s}'
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        if not s:
            return result
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            ln = int(s[i:j])
            st, en = j+1, j+1+int(ln)
            result.append(s[st:en])
            i = en
        return result

if __name__ == "__main__":
    solution = Solution()
    strs = ["hello", "world"]
    encoded_str = solution.encode(strs)
    print(f"Encoded: {encoded_str}")
    decoded_strs = solution.decode(encoded_str)
    print(f"Decoded: {decoded_strs}")