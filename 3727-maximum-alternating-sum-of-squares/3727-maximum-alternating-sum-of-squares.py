class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        x = [0] * n
        for i in range(n):
            x[i] = nums[i] * nums[i]
        x.sort()
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans -= x[i]
            else:
                ans += x[i]
        return ans