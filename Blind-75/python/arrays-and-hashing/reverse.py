class Solution:
    def reverse(self, arr: list, n: int) -> None:
        return arr.reverse()
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print("Original array:", arr)
    solution.reverse(arr, n)
    print("Reversed array:", arr)