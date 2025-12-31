class Solution:
    def stockBuySell(self, arr, n):
        l = 0
        r = 1
        maxi = 0
        while r < len(arr):
            if arr[r] > arr[l]:
                maxi = max(maxi, arr[r] - arr[l])
            else:
                l = r
            r += 1
        return maxi
if __name__ == "__main__":
    sol = Solution()
    # assertions
    print(sol.stockBuySell([7,1,5,3,6,4], 6))  # 5
    print(sol.stockBuySell([7,6,4,3,1], 5))  # 0